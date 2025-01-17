#!/usr/bin/env python3

import capnp  # noqa: F401
import argparse
from os import environ
import pandas as pd
from datetime import datetime
import logging
from numbers import Number
import itertools
from random import random
import ezdxf
from ezdxf import colors
from ezdxf.enums import TextEntityAlignment
from ezdxf.addons import r12writer
import math
from lxml import etree
import rr_graph_uxsdcxx_capnp
from multiprocessing import Pool, freeze_support, get_context, Manager

logger = logging.getLogger("rrgraph_generation")
stream_handler = logging.StreamHandler()
LOG_FORMAT = "%(levelname)6s %(lineno)s - %(message)s"
stream_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


INPUT_GRAPH_BIN = environ.get("INPUT_RRGRAPH_BIN", "_rrgraph_generated.bin")
OUTPUT_RRGRAPH_BIN = environ.get("OUTPUT_RRGRAPH_BIN", "_rrgraph_generated.bin")
ROUTING_RENDER_FILE = environ.get("ROUTING_RENDER_FILE", "_routing-render.dxf")
MERGE_ROWS = 5
MERGE_COLS = 4

MAX_TRACKS = int(environ.get("ROUTE_CHAN_WIDTH", 160))
DISTANCE = 1
BLOCK_MARGIN = 4
BLOCK_WIDTH = MAX_TRACKS * DISTANCE + 2 * BLOCK_MARGIN
BLOCK_HEIGHT = MAX_TRACKS * DISTANCE + 2 * BLOCK_MARGIN
CHAN_SPACING = int(max(BLOCK_WIDTH, BLOCK_HEIGHT) / 10)
GRID_X = BLOCK_WIDTH + CHAN_SPACING
GRID_Y = BLOCK_HEIGHT + CHAN_SPACING


def main():
    now = datetime.now()
    # Read rrgraph
    with open(OUTPUT_RRGRAPH_BIN, "r", encoding="UTF-8") as fp:
        rrgraph_bin = rr_graph_uxsdcxx_capnp.RrGraph.read(
            fp, traversal_limit_in_words=1024 * 1024 * 1024 * 2
        )
    logger.info("Finished reading rrgraph")

    # Create a new DXF document.
    doc = ezdxf.new(dxfversion="R2018")
    msp = doc.modelspace()

    block_names = {}
    for block in rrgraph_bin.blockTypes.blockTypes:
        block_names[block.id] = {"name": block.name, "block": block}

    # This section will create blocks/symbols for each tile
    instance_map = {}
    for grid in rrgraph_bin.grid.gridLocs:
        block = block_names[grid.blockTypeId]
        if not "block_inst" in block.keys():
            block_inst = doc.blocks.new(name=block["name"])
            block["block_inst"] = block_inst
            block["pin_map"] = create_block_in_dxf(block_inst, block["block"])

        my_block_ref = msp.add_blockref(
            block["name"], (grid.x * GRID_X, grid.y * GRID_Y)
        )
        instance_map[f"_{grid.x}__{grid.y}_"] = {
            "block": block,
            "origin": (grid.x * GRID_X, grid.y * GRID_Y),
        }
    node_lookup = {}
    for node in rrgraph_bin.rrNodes.nodes:
        if node.type in ("chanx", "chany"):
            draw_routing_node(msp, node)
        node_lookup[node.id] = node
    # cnt1 = 0
    # cnt2 = 0
    # cnt3 = 0
    for edge in rrgraph_bin.rrEdges.edges:
        sinkNode = node_lookup[edge.sinkNode]
        srcNode = node_lookup[edge.srcNode]
        # chan to chan
        if (str(srcNode.type) in ("chanx", "chany")) and (
            str(sinkNode.type) in ("chanx", "chany")
        ):
            logger.debug(
                f"Adding chan to chan edge {str(srcNode.type)=}[{edge.srcNode}] {str(sinkNode.type)=}[{edge.sinkNode}]"
            )
            draw_edge(msp, srcNode, sinkNode)
            # cnt1 += 1
        # opin to chan
        elif (str(srcNode.type) == "opin") and (
            str(sinkNode.type) in ("chanx", "chany")
        ):
            logger.debug(
                f"Adding opin to chan edge {str(srcNode.type)=}[{edge.srcNode}] {str(sinkNode.type)=}[{edge.sinkNode}]"
            )
            draw_edge(msp, srcNode, sinkNode, instance_map)
            # cnt2 += 1
        # chan to ipin
        elif (str(srcNode.type) in ("chanx", "chany")) and (
            str(sinkNode.type) == "ipin"
        ):
            logger.debug(
                f"Adding chan to ipin edge {str(srcNode.type)=}[{edge.srcNode}] {str(sinkNode.type)=}[{edge.sinkNode}]"
            )
            draw_edge(msp, srcNode, sinkNode, instance_map)
            # cnt3 += 1
        # if cnt1 > 10 and cnt3 > 10:
        #     break
    doc.saveas(ROUTING_RENDER_FILE)


def draw_edge(canvas, srcNode, sinkNode, instance_map={}):
    # logger.debug(f"\t {srcNode.type=}     {srcNode.direction=}")
    # logger.debug(f"\t {sinkNode.type=}    {sinkNode.direction=}")

    if srcNode.direction == "incDir":
        src_pt = (srcNode.loc.xlow, srcNode.loc.ylow)
    else:
        src_pt = (srcNode.loc.xhigh, srcNode.loc.yhigh)
    if sinkNode.direction == "incDir":
        dst_pt = (sinkNode.loc.xlow, sinkNode.loc.ylow)
    else:
        dst_pt = (sinkNode.loc.xhigh, sinkNode.loc.yhigh)

    distance = abs(src_pt[0] - dst_pt[0]) + abs(src_pt[1] - dst_pt[1])
    distance += (
        1 if (sinkNode.direction == "decDir" or str(sinkNode.type) == "ipin") else 0
    )
    # distance -= 1 if srcNode.direction == "decDir" else 0
    logger.debug(f"{distance=} {dst_pt=} {src_pt=}")

    src_incr = 1 if srcNode.direction == "incDir" else -1
    src_side = 1 if srcNode.type == "chanx" else -1
    src_ptc = [get_node_location(srcNode, instance_map)]
    dst_ptc = get_node_location(sinkNode, instance_map)
    ptc = list()
    if str(srcNode.type) == "opin":
        ptc.append(src_ptc[0])
        ptc.append(dst_ptc)
        # logger.debug(f'ptc: {ptc}')
        dxfattribs = {"layer": "TILE_OUT_CONN"}
        canvas.add_lwpolyline(ptc, dxfattribs=dxfattribs)
        arrow_layer = "TILE_OUT_CONN_ARROW"
        for i in range(len(ptc) - 1):
            start = ptc[i]
            end = ptc[i + 1]
            # Calculate direction angle
            angle = math.atan2(end[1] - start[1], end[0] - start[0])
            # Add arrowhead at a fraction (e.g., 80%) of the segment length
            position = (
                start[0] + 0.8 * (end[0] - start[0]),
                start[1] + 0.8 * (end[1] - start[1]),
            )
            add_arrowhead(canvas, position, angle, arrow_layer)
        return 1
    src_ptc.append(
        list(sum(x) for x in zip(src_ptc[-1], (src_incr * CHAN_SPACING, 0)[::src_side]))
    )
    for i in range(0, distance - 1):
        src_ptc.append(
            list(
                sum(x)
                for x in zip(
                    src_ptc[-1], (src_incr * BLOCK_WIDTH, 2 * src_incr)[::src_side]
                )
            )
        )
        src_ptc.append(
            list(
                sum(x)
                for x in zip(src_ptc[-1], (src_incr * CHAN_SPACING, 0)[::src_side])
            )
        )
    logger.debug(f"src_ptc: {src_ptc}")
    last_ptc_index = -1 if srcNode.direction == "incDir" else (distance - 1) * 2 - 1
    if last_ptc_index < -1:
        last_ptc_index = -1
    last_ptc_part = src_ptc[last_ptc_index]
    # last_ptc_part = src_ptc[-1]
    logger.debug(f"last_src_ptc_part: {last_ptc_part}")
    logger.debug(f"dst_ptc: {dst_ptc}")
    ptc.append(last_ptc_part)
    ptc.append(dst_ptc)
    # logger.debug(f'ptc: {ptc}')
    dxfattribs = (
        {"layer": "TILE_IN_CONN"}
        if str(sinkNode.type) == "ipin"
        else {"layer": "ROUTING_CONN"}
    )
    arrow_layer = {
        "TILE_IN_CONN": "TILE_IN_CONN_ARROW",
        "TILE_OUT_CONN": "TILE_OUT_CONN_ARROW",
        "ROUTING_CONN": "ROUTING_CONN_ARROW",
    }[dxfattribs["layer"]]
    canvas.add_lwpolyline(ptc, dxfattribs=dxfattribs)
    for i in range(len(ptc) - 1):
        start = ptc[i]
        end = ptc[i + 1]
        # Calculate direction angle
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        # Add arrowhead at a fraction (e.g., 80%) of the segment length
        position = (
            start[0] + 0.8 * (end[0] - start[0]),
            start[1] + 0.8 * (end[1] - start[1]),
        )
        add_arrowhead(canvas, position, angle, arrow_layer)
    return 1


def add_arrowhead(
    msp,
    position,
    angle,
    layer,
    size=1,
):
    """
    Add a simple arrowhead to the drawing.
    Args:
        msp: The modelspace to add the arrow to.
        position: The (x, y) position of the arrow tip.
        angle: The angle (in radians) of the arrow's orientation.
        size: The size of the arrow.
    """
    # Calculate the base points of the arrowhead triangle
    base1 = (
        position[0] - size * math.cos(angle - math.pi / 6),
        position[1] - size * math.sin(angle - math.pi / 6),
    )
    base2 = (
        position[0] - size * math.cos(angle + math.pi / 6),
        position[1] - size * math.sin(angle + math.pi / 6),
    )
    # Create the arrowhead using a polyline or lines
    dxfattribs = {"layer": layer}
    msp.add_lwpolyline(
        [position, base1, base2, position], close=True, dxfattribs=dxfattribs
    )


def get_node_location(node, instance_map={}):
    if node.direction == "incDir":
        if node.type == "chanx":
            instance_llx = ((node.loc.xlow) * GRID_X, node.loc.ylow * GRID_Y)
        else:
            instance_llx = (node.loc.xlow * GRID_X, (node.loc.ylow) * GRID_Y)
    else:
        instance_llx = (node.loc.xhigh * GRID_X, node.loc.yhigh * GRID_Y)
    if str(node.type) in ("opin", "ipin"):
        instance_llx = ((node.loc.xlow) * GRID_X, (node.loc.ylow) * GRID_Y)
        key = f"_{node.loc.xlow}__{node.loc.ylow}_"
        delta = instance_map[key]["block"]["pin_map"][int(node.loc.ptc)]
        # logger.debug(f"delta: {delta}")
    else:
        first_ptc = (
            int(node.loc.ptc.split(",")[0])
            if node.direction == "incDir"
            else MAX_TRACKS - int(node.loc.ptc.split(",")[-1])
        )
        delta = first_ptc + BLOCK_MARGIN
        delta = {
            "chanx": {"incDir": (BLOCK_WIDTH, delta), "decDir": (0, delta)},
            "chany": {"incDir": (delta, BLOCK_HEIGHT), "decDir": (delta, 0)},
        }[node.type][node.direction]
    return list(sum(x) for x in zip(instance_llx, delta))


def draw_routing_node(canvas, node):
    """
    This method will draw routing on the canvas
    as this is a flat rendering method the first variable `instance_llx`
    try to find the ll location of instance from where the routing channel starts

    `delta`: Computes the track starting location from where track starts
    `ptc`: Series of data points to draw routing
    """
    incr = 1 if node.direction == "incDir" else -1
    side = 1 if node.type == "chanx" else -1
    length = abs(node.loc.xlow - node.loc.xhigh) + abs(node.loc.ylow - node.loc.yhigh)
    # length += 1
    ptc = [get_node_location(node)]
    ptc.append(list(sum(x) for x in zip(ptc[-1], (incr * CHAN_SPACING, 0)[::side])))
    for i in range(length - 1):
        ptc.append(
            list(sum(x) for x in zip(ptc[-1], (incr * BLOCK_WIDTH, 2 * incr)[::side]))
        )
        ptc.append(list(sum(x) for x in zip(ptc[-1], (incr * CHAN_SPACING, 0)[::side])))

    layer = f"{node.type}_{node.direction}_TRACKS"
    dxfattribs = {"layer": layer}
    canvas.add_lwpolyline(ptc[: length * 2], dxfattribs=dxfattribs)
    for i in range(len(ptc[: length * 2]) - 1):
        start = ptc[i]
        end = ptc[i + 1]
        # Calculate direction angle
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        # Add arrowhead at a fraction (e.g., 80%) of the segment length
        position = (
            start[0] + 0.8 * (end[0] - start[0]),
            start[1] + 0.8 * (end[1] - start[1]),
        )
        add_arrowhead(canvas, position, angle, f"{layer}_ARROW")


def create_block_routing_in_dxf(X, Y, canvas, block, df):
    pin_map = {}
    for col in range(MERGE_COLS, df.shape[-1]):
        side = df.iloc[0, col]
        length = int(df.iloc[1, col][1:])
        seg_indx = int(df.iloc[3, col])
        tap = (
            1
            if (pd.isna(df.iloc[4, col]) or not isinstance(df.iloc[4, col], Number))
            else int(df.iloc[4, col])
        )
        low = X if side in ("Left", "Right") else Y
        high = low + length if side in ("Right", "Top") else low + length
        ptc = seg_indx * length * 2 + (tap - 1) + (0 if side in ("Right", "Top") else 1)

        # Create track here
        if not side in ("Left", "Right", "Top", "Bottom"):
            continue
        start = {
            "Left": (0, ptc + 4),
            "Right": (BLOCK_WIDTH, ptc + 4),
            "Top": (ptc + 4, BLOCK_HEIGHT),
            "Bottom": (ptc + 4, 0),
        }[side]
        print(f"{side=} {length=} {seg_indx=} {tap=} {low=} {high=} {start=}")
        canvas.add_lwpolyline(
            [(BLOCK_WIDTH * 0.5, BLOCK_HEIGHT * 0.5), start],
            dxfattribs={"layer": "ROUTING_TRACKS", "lineweight": 2},
        )
    return pin_map


def build_hash(node):
    return (
        str(node.type).upper(),
        str(node.loc.ptc),
        int(node.loc.xlow),
        int(node.loc.xhigh),
        int(node.loc.ylow),
        int(node.loc.yhigh),
    )


def create_block_in_dxf(canvas, block):
    # Create outline
    canvas.add_lwpolyline(
        [
            (0, 0),
            (0, BLOCK_HEIGHT),
            (BLOCK_WIDTH, BLOCK_HEIGHT),
            (BLOCK_WIDTH, 0),
            (0, 0),
        ],
        close=True,
    )
    canvas.add_text(block.name, dxfattribs={"layer": "TEXTLAYER"}).set_placement(
        (BLOCK_WIDTH / 2, BLOCK_HEIGHT / 2), align=TextEntityAlignment.CENTER
    )

    if len(block.pinClasses) == 0:
        return
    input_pins = sum(
        len(port.pins) for port in block.pinClasses if port.type == "input"
    )
    output_pins = sum(
        len(port.pins) for port in block.pinClasses if port.type == "output"
    )

    pin_map = {}
    input_pt = [1, 0]
    output_pt = [1, 0]
    pin_pitch = BLOCK_HEIGHT * 0.08
    for port in block.pinClasses:
        if port.type == "input":
            for pin in port.pins:
                pt_x = (BLOCK_WIDTH / 2) - (input_pt[0] * 4)
                pt_y = pin_pitch * input_pt[1] + (BLOCK_HEIGHT * 0.1)
                pin_map[pin.ptc] = (pt_x, pt_y)
                canvas.add_circle(
                    (pt_x, pt_y), radius=1, dxfattribs={"color": colors.GREEN}
                )
                canvas.add_text(
                    pin.value, dxfattribs={"layer": "PINTEXTLAYER"}
                ).set_placement((pt_x, pt_y), align=TextEntityAlignment.CENTER)
                input_pt[1] += 1
                if input_pt[1] > 10:
                    input_pt[0] += 1
                    input_pt[1] = 0
        if port.type == "output":
            for pin in port.pins:
                pt_x = (BLOCK_WIDTH / 2) + (output_pt[0] * 4)
                pt_y = pin_pitch * output_pt[1] + (BLOCK_HEIGHT * 0.1)
                pin_map[pin.ptc] = (pt_x, pt_y)
                canvas.add_circle(
                    (pt_x, pt_y), radius=1, dxfattribs={"color": colors.BLUE}
                )
                canvas.add_text(
                    pin.value, dxfattribs={"layer": "PINTEXTLAYER"}
                ).set_placement((pt_x, pt_y), align=TextEntityAlignment.CENTER)
                output_pt[1] += 1
                if output_pt[1] > 10:
                    output_pt[0] += 1
                    output_pt[1] = 0
    return pin_map


if __name__ == "__main__":
    main()
