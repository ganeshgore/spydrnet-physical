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

    for edge in rrgraph_bin.rrEdges.edges:
        sinkNode = node_lookup[edge.sinkNode]
        srcNode = node_lookup[edge.srcNode]

        # Skip drawing edges from source to sink
        if (str(srcNode.type) == "source") or (str(sinkNode.type) == "sink"):
            continue

        draw_edge(msp, srcNode, sinkNode, instance_map)
    doc.saveas(ROUTING_RENDER_FILE)


def draw_edge(canvas, src_node, sink_node, instance_map=None):
    """
    Draws an edge between two nodes on a given canvas. The destination point is
    fixed and Source node is transalated from any other grid location to
    the destination node grid location,.

    Parameters:
    canvas (Canvas): The canvas object where the edge will be drawn.
    src_node (Node): The source node from which the edge originates.
    sink_node (Node): The sink node where the edge terminates.
    instance_map (dict, optional): A dictionary mapping node instances to their locations. Defaults to an empty dictionary.
    Returns:
    None
    """

    # Get starting location of source and destination node
    src_ptc = get_node_location(src_node, instance_map)
    dst_ptc = get_node_location(sink_node, instance_map)

    if str(src_node.type) in ("chanx", "chany"):
        # Convert source direction to a signed integer
        direction_sign = {
            "incDir": 1,
            "decDir": -1,
        }[src_node.direction]

        # Get Source and destination point
        src_pt = {
            "incDir": (src_node.loc.xlow, src_node.loc.ylow),
            "decDir": (src_node.loc.xhigh, src_node.loc.yhigh),
        }[src_node.direction]

        if str(sink_node.type) == "ipin":
            dst_pt = (sink_node.loc.xlow, sink_node.loc.ylow)
        else:
            dst_pt = {
                "incDir": (sink_node.loc.xlow, sink_node.loc.ylow),
                "decDir": (sink_node.loc.xhigh, sink_node.loc.yhigh),
            }[sink_node.direction]

        # Find distance between source and destination node grid location
        distance = abs(src_pt[0] - dst_pt[0]) + abs(src_pt[1] - dst_pt[1])

        # Transalate source node location to destination grid location
        if src_node.type == "chany":
            src_ptc[0] += (distance - 1) * direction_sign * 2
            src_ptc[1] += (
                (BLOCK_WIDTH + CHAN_SPACING) * (distance - 1)
            ) * direction_sign
            src_ptc[1] += CHAN_SPACING * direction_sign
        if src_node.type == "chanx":
            src_ptc[1] += (distance - 1) * direction_sign * 2
            src_ptc[0] += (
                (BLOCK_WIDTH + CHAN_SPACING) * (distance - 1)
            ) * direction_sign
            src_ptc[0] += CHAN_SPACING * direction_sign

    # Add conenction line in the canvas
    if str(src_node.type) in ("chanx", "chany") and str(sink_node.type) in (
        "chanx",
        "chany",
    ):
        dxfattribs = {"layer": "ROUTING_CONN"}
    else:
        dxfattribs = {"layer": "TILE_CONN"}
    canvas.add_lwpolyline((src_ptc, dst_ptc), dxfattribs=dxfattribs)

    # Add direction arrow on 0.1x of the line
    angle = math.atan2(dst_ptc[1] - src_ptc[1], dst_ptc[0] - src_ptc[0])
    position = (
        src_ptc[0] + 0.1 * (dst_ptc[0] - src_ptc[0]),
        src_ptc[1] + 0.1 * (dst_ptc[1] - src_ptc[1]),
    )
    add_arrowhead(canvas, position, angle, dxfattribs["layer"])


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


def get_node_location(node, instance_map=None):
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
        if instance_map:
            delta = instance_map[key]["block"]["pin_map"][int(node.loc.ptc)]
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
                    pin.value.split(".")[-1], dxfattribs={"layer": "PINTEXTLAYER"}
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
                    pin.value.split(".")[-1], dxfattribs={"layer": "PINTEXTLAYER"}
                ).set_placement((pt_x, pt_y), align=TextEntityAlignment.CENTER)
                output_pt[1] += 1
                if output_pt[1] > 10:
                    output_pt[0] += 1
                    output_pt[1] = 0
    return pin_map


if __name__ == "__main__":
    main()
