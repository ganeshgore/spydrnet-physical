"""
===========================================
Generate RRGraph from VPR architecture file
===========================================

"""

from spydrnet_physical.util import rrgraph
import logging
from pathlib import Path
import pandas as pd
import numpy as np
from fnmatch import fnmatch
from collections import OrderedDict


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
        "SB_1__*_": "./baseline_l4/switchbox_left.xlsx",
        "SB_6__*_": "./baseline_l4/switchbox_right.xlsx",
        "SB_*__1_": "./baseline_l4/switchbox_bottom.xlsx",
        "SB_*__6_": "./baseline_l4/switchbox_top.xlsx",
        "SB_*__*_": "./baseline_l4/switchbox_main.xlsx",
    }
)

MERGE_ROWS = 5
MERGE_COLS = 4
FPGA_GRID_X = 7
FPGA_GRID_Y = 7


def main():
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

        # Create nodes

        node_id = 0
        for X in range(1, FPGA_GRID_X):
            for Y in range(1, FPGA_GRID_Y):
                sw_name = f"SB_{X}__{Y}_"
                sb_patt = [key for key in SB_MAPS.keys() if fnmatch(sw_name, key)]
                if len(sb_patt) and (sb_patt[0] in sb_df.keys()):
                    logger.info(
                        "Adding pattern %12s %s at locations %d %d",
                        sb_patt[0],
                        Path(SB_MAPS[sb_patt[0]]).name,
                        X,
                        Y,
                    )
                    for row in (
                        sb_df[sb_patt[0]]
                        .iloc[:5, :]
                        .transpose()
                        .itertuples(index=False)
                    ):
                        side, seg_type, _, index, tap = row
                        if side in ("Left", "Right", "Top", "Bottom"):
                            rrgraph_bin.create_node(
                                x=X,
                                y=Y,
                                node_id=node_id,
                                ptc_start=(index-1)*4 + (tap - 1),
                                seg_type=seg_type,
                                side=side,
                                tap=tap,
                            )
                            node_id += 1

    # Create edges

    # Write rrgraph to file
    rrgraph_bin.write_rrgraph_xml("_rrgraph_generated.xml")


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
