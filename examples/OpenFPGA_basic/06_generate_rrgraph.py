""" ===========================================
Generate RRGraph from VPR architecture file ===========================================

"""

from spydrnet_physical.util import rrgraph
import logging
from pathlib import Path
import pandas as pd
import numpy as np
from fnmatch import fnmatch
from pprint import pprint
from collections import OrderedDict
from itertools import product


logger = logging.getLogger("rrgraph_generation")
stream_handler = logging.StreamHandler()
LOG_FORMAT = "%(levelname)6s %(lineno)s - %(message)s"
stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Global constants
SB_MAPS = OrderedDict(
    {
        "SB_*__0_": None,
        "SB_0__*_": None,
        "SB_6__6_": None,
        "SB_1__1_": None,
        "SB_1__6_": None,
        "SB_6__1_": None,
        # "SB_1__*_": None,
        # "SB_*__1_": None,
        # "SB_*__6_": None,
        # "SB_6__*_": None,
        "SB_1__*_": "./baseline_l4/switchbox_left.xlsx",
        "SB_*__1_": "./baseline_l4/switchbox_bottom.xlsx",
        "SB_*__6_": "./baseline_l4/switchbox_top.xlsx",
        "SB_6__*_": "./baseline_l4/switchbox_right.xlsx",
        "SB_*__*_": "./baseline_l4/switchbox_main.xlsx",
    }
)

MERGE_ROWS = 5
MERGE_COLS = 4
FPGA_GRID_X = 7
FPGA_GRID_Y = 7


def main():
    global SB_MAPS
    # Read all excel file and process them to create a sb_df map
    rrgraph_bin = rrgraph("vpr-rendered.xml", 16, "FPGA44")
    sb_df = {}

    for k, v in SB_MAPS.items():
        try:
            if v is None:
                continue
            else:
                dataframe = process_dataframe(
                    pd.read_excel(v, index_col=None, header=None),
                    merge_row=MERGE_ROWS,
                    merge_cols=MERGE_COLS,
                )
                dataframe.source_file = Path(v).stem
                dataframe.connetions = (
                    dataframe.iloc[MERGE_ROWS:, MERGE_COLS:].count().sum()
                )
                logger.info(
                    "Processed %5d connections in %s file",
                    dataframe.connetions,
                    Path(v).name,
                )
        except Exception as error:
            msg = f"An error has occurred while reading the excel sheet: {error}"
            logger.error(msg)
            exit(1)
        sb_df[k] = dataframe

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                           Create nodes
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    node_id = 0
    for X in range(1, rrgraph_bin.width - 1):
        for Y in range(1, rrgraph_bin.height - 1):
            sw_name = f"SB_{X}__{Y}_"
            sb_patt = [key for key in SB_MAPS.keys() if fnmatch(sw_name, key)]
            if len(sb_patt) and (sb_patt[0] in sb_df.keys()):
                for row in (
                    sb_df[sb_patt[0]].iloc[:5, :].transpose().itertuples(index=False)
                ):
                    side, seg_type, _, index, tap = row
                    if side in ("Left", "Right", "Top", "Bottom"):
                        index, tap = int(index), int(tap)
                        node = rrgraph_bin.create_chan_node(
                            x=X,
                            y=Y,
                            node_id=node_id,
                            index=(index - 1) * 4,
                            seg_type=seg_type,
                            side=side,
                            tap=tap,
                        )
                        node_id += 1
                logger.info(
                    "Creating Nodes %12s %s at locations %d %d [%d-%d nodes]",
                    sb_patt[0],
                    Path(SB_MAPS[sb_patt[0]]).name,
                    X - 1,
                    Y - 1,
                    node_id,
                    len(
                        [
                            n
                            for col in rrgraph_bin.chan_node_lookup
                            for row in col
                            for n in row.values()
                        ]
                    ),
                )

    rrgraph_bin._print_node_metrics()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Create edges
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # for X, Y in product(range(1, FPGA_GRID_X), range(1, FPGA_GRID_Y)):
    for X, Y in ((2, 2),):
        sw_name = f"SB_{X}__{Y}_"
        sb_patt = [key for key in SB_MAPS.keys() if fnmatch(sw_name, key)]
        # Skip is pattern is not found
        if not (len(sb_patt) and (sb_patt[0] in sb_df.keys())):
            continue

        logger.info(
            "Creating edge %s %s at locations %d %d",
            sb_patt[0],
            Path(SB_MAPS[sb_patt[0]]).name,
            X - 1,
            Y - 1,
        )

        source_nodes = []
        sink_nodes = []
        df = sb_df[sb_patt[0]]

        # Find node for horizontal values
        for col in range(MERGE_COLS, df.shape[-1]):
            side = df.iloc[0, col]
            seg_type = df.iloc[1, col]
            seg_indx = int(df.iloc[3, col])
            tap = (
                int(df.iloc[4, col])
                if side in ("Left", "Right", "Top", "Bottom")
                else 1
            )
            try:
                if side in ("Left", "Right", "Top", "Bottom"):
                    sink_nodes.append(
                        rrgraph_bin.chan_node_lookup[X - 1][Y - 1][
                            ((seg_indx - 1) * 4, tap, side)
                        ]
                    )
            except KeyError:
                pprint(rrgraph_bin.chan_node_lookup[X - 1][Y - 1].keys())
                raise KeyError

        # Find node for vertical columns
        for row in range(MERGE_ROWS, df.shape[0]):
            side = df.iloc[row, 0]
            seg_type = df.iloc[row, 1]
            seg_indx = int(df.iloc[row, 2])
            tap = (
                int(df.iloc[row, 3])
                if side in ("Left", "Right", "Top", "Bottom")
                else 1
            )

            if side in ("Left", "Right", "Top", "Bottom"):
                x_shift = {
                    "Left": X - tap,
                    "Right": X + tap,
                    "Bottom": X,
                    "Top": X,
                }[side] - 1
                y_shift = {
                    "Left": Y,
                    "Right": Y,
                    "Bottom": Y - tap,
                    "Top": Y + tap,
                }[side] - 1
                x_shift_src = max(0, min(x_shift, rrgraph_bin.width - 3))
                y_shift_src = max(0, min(y_shift, rrgraph_bin.height - 3))
                trunc = abs((x_shift - x_shift_src) + (y_shift - y_shift_src)) + 1
                try:
                    source_nodes.append(
                        rrgraph_bin.chan_node_lookup[x_shift_src][y_shift_src][
                            (
                                (seg_indx - 1) * 4,
                                trunc,
                                {
                                    "Left": "Right",
                                    "Right": "Left",
                                    "Bottom": "Top",
                                    "Top": "Bottom",
                                }[side],
                            )
                        ]
                    )
                except KeyError:
                    print(
                        x_shift,
                        y_shift,
                        rrgraph_bin.chan_node_lookup[x_shift][y_shift].keys(),
                    )
                    raise KeyError

        print(f"Source Nodes: {[i.id for i in source_nodes]}")
        print(f"Sink Nodes: {[i.id for i in sink_nodes]}")

        for eachrow in df.itertuples(index=True):
            col_indx = eachrow[0]
            if col_indx < MERGE_ROWS:
                continue
            for row_indx, df_value in enumerate(eachrow):
                if row_indx <= MERGE_COLS:
                    continue
                row_indx -= 1
                if not pd.isna(df_value):
                    col_i, row_i = col_indx - MERGE_ROWS, row_indx - MERGE_COLS
                    switch_id = 1 if isinstance(df_value, str) else int(df_value)
                    rrgraph_bin.create_edge(
                        source_nodes[col_i].id, sink_nodes[row_i].id, switch_id
                    )

    # Write rrgraph to file
    rrgraph_bin.write_rrgraph_xml("_rrgraph_generated.xml")
    rrgraph_bin.write_rrgraph_bin("_rrgraph_generated.bin")


def process_dataframe(df, merge_row=1, merge_cols=1):
    """
    Process a pandas DataFrame by merging rows and columns and updating values based on certain conditions.
    Parameters:
    df (pd.DataFrame): The DataFrame to be processed.
    merge_row (int): The number of rows to merge. Default is 1.
    merge_cols (int): The number of columns to merge. Default is 1.
    Returns:
    pd.DataFrame: The processed DataFrame with merged rows and columns and updated values.
    """

    # merge rows
    for row in range(merge_row):
        value = np.nan
        for col in range(df.shape[-1]):
            value = value if pd.isna(df.iloc[row, col]) else df.iloc[row, col]
            df.iloc[row, col] = value
    # merge cols
    for col in range(merge_cols):
        value = np.nan
        for row in range(df.shape[0]):
            value = value if pd.isna(df.iloc[row, col]) else df.iloc[row, col]
            df.iloc[row, col] = value
    return df


if __name__ == "__main__":
    main()
