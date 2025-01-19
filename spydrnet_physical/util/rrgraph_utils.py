"""
This script is a placeholder for the rrgraph utility functions that will be used to read and write rrgraph files.
"""

from lxml.etree import XML, parse, XMLParser
from lxml.etree import tostring as etree_tostring
import pandas as pd
import re

import capnp  # noqa: F401
from spydrnet_physical.util import rr_graph_uxsdcxx_capnp as rr_capnp
from spydrnet_physical.util.FPGAGridGen import FPGAGridGen
from spydrnet_physical.util.rrgraph_uncompress import rrgraph_bin2xml


class rrgraph(rrgraph_bin2xml):

    def __init__(self, vpr_arch, routing_chan, layout=None):

        self.routing_chan = routing_chan
        self.edges = []
        self.switches = []
        self.channels = {}
        self.segments = []
        self.block_types = []
        self.grid_locs = []
        self.rrgraph_bin = rr_capnp.RrGraph.new_message()
        self.node_id = 0
        if vpr_arch:
            self.enumerate_rrgraph(vpr_arch, layout)
            self.chan_node_lookup = [
                [{} for _ in range(self.height)] for _ in range(self.width)
            ]
            self.pin_node_lookup = [
                [{} for _ in range(self.height)] for _ in range(self.width)
            ]
            self.channels["X"] = list(routing_chan for _ in range(self.width))
            self.channels["Y"] = list(routing_chan for _ in range(self.width))
            self.create_channels()

    def enumerate_rrgraph(self, filename, layout):
        """
        Enumerate the routing resource graph (RRGraph) from a VPR architecture file.
        """
        parser = XMLParser(remove_comments=True, remove_blank_text=True)
        tree = parse(filename, parser)
        root = tree.getroot()

        self.width = int(
            root.find(f'.//fixed_layout[@name="{layout}"]').attrib["width"]
        )
        self.height = int(
            root.find(f'.//fixed_layout[@name="{layout}"]').attrib["height"]
        )

        # Adding switchlist
        self.create_switch("__vpr_delayless_switch__", "mux")
        for switch in root.find("switchlist"):
            # Pre calculation
            buf_size = switch.attrib.get("buf_size", 0)
            self.create_switch(
                switch.attrib["name"],
                switch.attrib["type"],
                cin=float(switch.attrib.get("Cin", 0)),
                cout=float(switch.attrib.get("Cout", 0)),
                r=float(switch.attrib.get("R", 0)),
                tdel=float(switch.attrib.get("Tdel", 0)),
                buf_size=0 if buf_size == "auto" else float(buf_size),
                mux_trans_size=float(switch.attrib.get("mux_trans_size", 0)),
            )

        # Adding segments
        for segments in root.find("segmentlist"):
            self.create_segment(
                segments.attrib["name"], segments.attrib["length"], res_type="general"
            )

        # Adding block types
        self.create_block(
            "EMPTY",
            (),
            height=1,
            width=1,
        )

        tile_dim = {}
        for tile in root.findall("tiles/tile"):
            tile_name = tile.attrib["name"]
            tile_dim[tile.attrib["name"]] = {
                "width": tile.attrib.get("width", 1),
                "height": tile.attrib.get("height", 1),
            }

            pins = []
            block_capacity = int(tile.find("sub_tile").attrib.get("capacity", 1))
            for t_idx in range(block_capacity):
                t_idx = f"[{t_idx}]" if block_capacity > 1 else ""
                for pin in tile.findall("sub_tile/input"):
                    p_name = pin.attrib["name"]
                    p_num = int(pin.attrib.get("num_pins", 1))
                    if pin.attrib.get("equivalent", "none") == "full":
                        pins.append(("I", f"{tile_name}{t_idx}.{p_name}[0:{p_num}]"))
                    else:
                        for p_num in range(p_num):
                            pins.append(("I", f"{tile_name}{t_idx}.{p_name}[{p_num}]"))

                for pin in tile.findall("sub_tile/output"):
                    p_name = pin.attrib["name"]
                    p_num = int(pin.attrib.get("num_pins", 1))
                    if pin.attrib.get("equivalent", "none") == "full":
                        pins.append(("O", f"{tile_name}{t_idx}.{p_name}[0:{p_num}]"))
                    else:
                        for p_num in range(p_num):
                            pins.append(("O", f"{tile_name}{t_idx}.{p_name}[{p_num}]"))

                for pin in tile.findall("sub_tile/clock"):
                    p_name = pin.attrib["name"]
                    for p_num in range(int(pin.attrib.get("num_pins", 1))):
                        pins.append(("I", f"{tile_name}{t_idx}.{p_name}[{p_num}]"))

            self.create_block(
                tile.attrib["name"],
                pins,
                height=tile.attrib.get("height", 1),
                width=tile.attrib.get("width", 1),
            )

        # Adding block instances
        fpga_grid = FPGAGridGen(
            design_name="example_design",
            arch_file=filename,
            release_root="_release",
            layout=layout,
        )
        fpga_grid.enumerate_grid()
        for x in range(self.width):
            for y in range(self.height):
                self.add_grid_block(
                    fpga_grid.grid[y][x], x, y, layer=0, x_offset=0, y_offset=0
                )

    def _print_node_metrics(self):
        """
        Print the metrix of the nodes in the rrgraph.
        """
        for row in range(self.height - 2)[::-1]:
            # print(self.chan_node_lookup[0][row])
            print(
                " ".join(
                    [
                        f"{len(self.chan_node_lookup[col][row]):4d} [{col:2d},{row:2d}]"
                        for col in range(self.width - 2)
                    ]
                )
            )

    def create_ipin_node(self, x, y, node_id, side, ptc):
        """
        Create an IPIN (input pin) node in the RR graph.
        Alias for create_pin_node
        """
        self.create_pin_node(x, y, node_id, side, ptc, node_type="ipin")

    def create_opin_node(self, x, y, node_id, side, ptc):
        """
        Create an OPIN (output pin) node in the RR graph.
        Alias for create_pin_node
        """
        self.create_pin_node(x, y, node_id, side, ptc, node_type="opin")

    def create_pin_node(self, x, y, node_id, side, ptc, node_type="ipin"):
        """
        Creates a pin node with the specified parameters and adds it to
        the pin node lookup.
        Args:
            x (int): The x-coordinate of the node.
            y (int): The y-coordinate of the node.
            node_type (str): The type of the node.
            node_id (int): The unique identifier for the node.
            side (str): The side of the node.
            ptc (int): The pin-to-channel index.
        Returns:
            rr_capnp.Node: The created pin node.
        """
        node = rr_capnp.Node.new_message(
            id=node_id,
            capacity=1,
            type=node_type.lower(),
            side=side,
            loc=rr_capnp.NodeLoc.new_message(
                xlow=x,
                xhigh=x,
                ylow=y,
                yhigh=y,
                ptc=ptc,
            ),
            timing=rr_capnp.NodeTiming.new_message(r=0, c=0),
            segment=rr_capnp.NodeSegment.new_message(),
        )
        self.pin_node_lookup[x - 1][y - 1][(int(ptc), side)] = node
        return node

    def create_chan_node(self, x, y, node_id, index, seg_type, side, tap=1):
        """
        index: 0
        seg_type: L4
        side: Left/Right/Top/Bottom
        tap: Represents the truncation at the source
        """
        # Get the segment expected length
        length = int(seg_type[1:]) - tap + 1

        # Compute (xlow, ylow, xhigh, yhigh) for the node
        # fmt: off
        xlow, ylow, xhigh, yhigh = {
            "Left"  : (x-length, y, x, y),
            "Right" : (x, y, x+length, y),
            "Top"   : (x, y, x, y+length),
            "Bottom": (x, y-length, x, y)}[side]
        # fmt: on

        # Truncate wire length on edges
        xlow = max(xlow, 1)
        ylow = max(ylow, 1)
        xhigh = min(xhigh, self.width - 2)
        yhigh = min(yhigh, self.height - 2)

        phy_length = int((xhigh - xlow) + (yhigh - ylow))
        direction_sign = -1 if side in ("Left", "Bottom") else 1

        # Compute the index point
        ptc_start = ((index + tap - 1) * 2) + (1 if side in ("Left", "Bottom") else 0)
        ptc_end = int(ptc_start + (length * 2))
        ptc_sequence = ",".join(
            map(
                str,
                range(
                    int(ptc_start),
                    ptc_end,
                    2,
                )[
                    :phy_length
                ][::direction_sign],
            )
        )

        node = rr_capnp.Node.new_message(
            id=node_id,
            capacity=1,
            type=["chanx", "chany"][int(side in ("Top", "Bottom"))],
            direction=["incDir", "decDir"][int(side in ("Left", "Bottom"))],
            loc=rr_capnp.NodeLoc.new_message(
                xlow=xlow,
                xhigh=xhigh,
                ylow=ylow,
                yhigh=yhigh,
                twist=2,
                ptc=ptc_sequence,
            ),
            timing=rr_capnp.NodeTiming.new_message(r=0, c=0),
            segment=rr_capnp.NodeSegment.new_message(),
        )
        # Instead of doing calculation again take hashid as an argument
        self.chan_node_lookup[x - 1][y - 1][(int(index), int(tap), side)] = node
        return node

    def create_edge(self, source, destination, swith_id):
        """
        Creates an edge between a source node and a destination node with a specified switch ID.
        Args:
            source (int): The source node identifier.
            destination (int): The destination node identifier.
            swith_id (int): The switch ID to be used for the edge.
        Returns:
            rr_capnp.Edge: The created edge object.
        """

        edge = rr_capnp.Edge.new_message(
            sinkNode=int(destination),
            srcNode=int(source),
            switchId=int(swith_id),
        )
        self.edges.append(edge)
        return edge

    def create_block(
        self,
        block_name,
        pins,
        height=1,
        width=1,
    ):
        # Block Types
        rr = self.rrgraph_bin

        block_type_ux = rr_capnp.BlockType.new_message(
            id=len(rr.blockTypes.blockTypes),
            height=height,
            name=block_name,
            width=width,
        )

        ptc = 0
        pinClasses = []
        for pin in pins:
            pin_direction = {"I": "INPUT", "O": "OUTPUT"}[pin[0]]
            match = re.search("[0-9]*:[0-9]*", pin[1])

            pins_list = []
            if match:
                for p in range(*map(int, match.group().split(":"))):
                    pins_list.append(pin[1].replace(match.group(), f"{p}"))
            else:
                pins_list.append(pin[1])

            pinClasses.append(
                rr_capnp.PinClass.new_message(
                    type=pin_direction.lower(),
                    pins=[
                        rr_capnp.Pin.new_message(ptc=ptc + indx, value=each)
                        for indx, each in enumerate(pins_list)
                    ],
                )
            )
            ptc += len(pins_list)
        block_type_ux.pinClasses = pinClasses

        self.block_types.append(block_type_ux)
        rr.blockTypes.blockTypes = self.block_types
        return block_type_ux

    def add_grid_block(self, block, x, y, layer=0, x_offset=0, y_offset=0):
        block_id = [b.name for b in self.block_types].index(block)
        grid = rr_capnp.GridLoc.new_message(
            blockTypeId=block_id,
            x=x,
            y=y,
            heightOffset=y_offset,
            widthOffset=x_offset,
            layer=layer,
        )
        self.grid_locs.append(grid)
        self.rrgraph_bin.grid = rr_capnp.GridLocs.new_message()
        self.rrgraph_bin.grid.gridLocs = self.grid_locs
        return grid

    def create_segment(
        self, name, length, res_type="uxsdInvalid", c_per_meter=0, r_per_meter=0
    ):
        rr = self.rrgraph_bin
        rr.segments = rr_capnp.Segments.new_message()

        segment_ux = rr_capnp.Segment.new_message(
            id=len(self.segments),
            length=int(length),
            name=name,
            resType=res_type,
            timing=rr_capnp.SegmentTiming.new_message(
                cPerMeter=c_per_meter, rPerMeter=r_per_meter
            ),
        )
        self.segments.append(segment_ux)
        return segment_ux

    def create_channels(self):
        # Channels
        rr = self.rrgraph_bin
        rr.channels = rr_capnp.Channels.new_message()
        rr.channels.channel = rr_capnp.Channel.new_message(
            xMax=max(self.channels["X"]),
            xMin=min(self.channels["X"]),
            yMax=max(self.channels["Y"]),
            yMin=min(self.channels["Y"]),
            chanWidthMax=max(self.channels["X"] + self.channels["Y"]),
        )
        x_lists, y_lists = [], []
        for indx, chan in enumerate(self.channels["X"]):
            x_lists.append(rr_capnp.XList.new_message(index=indx, info=chan))
        for indx, chan in enumerate(self.channels["Y"]):
            y_lists.append(rr_capnp.YList.new_message(index=indx, info=chan))
        rr.channels.xLists = x_lists
        rr.channels.yLists = y_lists
        return rr.channels

    def create_switch(
        self,
        sw_name,
        sw_type,
        cin=0,
        cinternal=0,
        cout=0,
        r=0,
        tdel=0,
        buf_size=0,
        mux_trans_size=0,
    ):
        """
        Create a new switch and add it to the list of switches.
        Args:
            sw_name (str): Name of the switch.
            sw_type (str): Type of the switch. [uxsdInvalid mux tristate passGate short buffer]
            cin (float, optional): Input capacitance. Defaults to 0.
            cinternal (float, optional): Internal capacitance. Defaults to 0.
            cout (float, optional): Output capacitance. Defaults to 0.
            r (float, optional): Resistance. Defaults to 0.
            tdel (float, optional): Time delay. Defaults to 0.
            buf_size (float, optional): Buffer size. Defaults to 0.
            mux_trans_size (float, optional): Multiplexer transistor size. Defaults to 0.
        Returns:
            rr_capnp.Switch: The created switch object.
        """

        switch = rr_capnp.Switch.new_message(
            id=len(self.switches),
            name=sw_name,
            type=sw_type,
            timing=rr_capnp.Timing.new_message(
                cin=cin, cinternal=cinternal, cout=cout, r=r, tdel=tdel
            ),
            sizing=rr_capnp.Sizing.new_message(
                bufSize=buf_size, muxTransSize=mux_trans_size
            ),
        )
        self.switches.append(switch)
        return switch

    # Reading and writing related methods
    def read_rrgraph_xml(self, filename):
        pass

    def read_rrgraph_bin(self, filename):
        pass

    def _update_nodes_edges(self):
        # Add nodes
        if len(self.rrgraph_bin.rrNodes.nodes) == 0:
            self.rrgraph_bin.rrNodes.nodes = [
                n for col in self.pin_node_lookup for row in col for n in row.values()
            ] + [
                n for col in self.chan_node_lookup for row in col for n in row.values()
            ]

        # Add edges
        if len(self.rrgraph_bin.rrEdges.edges) == 0:
            self.rrgraph_bin.rrEdges.edges = self.edges

    def _gen_rrgraph_xml(
        self, tool_comment="", tool_name="openfpga-physical", tool_version="v1.0"
    ):
        root = XML("<rr_graph></rr_graph>")
        # Basic information
        root.attrib["tool_comment"] = tool_comment
        root.attrib["tool_name"] = tool_name
        root.attrib["tool_version"] = tool_version

        # Add blocks related information to the graph
        channels = self._channels_bin2xml(self.rrgraph_bin.channels)
        switches = self._switches_bin2xml(self.switches)
        segments = self._segments_bin2xml(self.segments)
        block_types = self._block_types_bin2xml(self.rrgraph_bin.blockTypes.blockTypes)
        grids = self._grid_bin2xml(self.rrgraph_bin.grid.gridLocs)

        # Update_nodes and edges
        self._update_nodes_edges()

        # Add nodes and edges to XML file
        rr_nodes = self._nodes_bin2xml(self.rrgraph_bin.rrNodes.nodes)
        rr_edges = self._edges_bin2xml(self.rrgraph_bin.rrEdges.edges)

        root.append(channels)
        root.append(switches)
        root.append(segments)
        root.append(block_types)
        root.append(grids)
        root.append(rr_nodes)
        root.append(rr_edges)
        return root

    def write_rrgraph_xml(
        self, filename, tool_comment="", tool_name="", tool_version=""
    ):
        """
        Writes the routing resource graph (RRGraph) to an XML file.
        Args:
            filename (str): The path to the output XML file.
            tool_comment (str): A comment or description of the tool generating the RRGraph.
            tool_name (str): The name of the tool generating the RRGraph.
            tool_version (str): The version of the tool generating the RRGraph.
        Returns:
            None
        """

        root = self._gen_rrgraph_xml(tool_comment, tool_name, tool_version)
        with open(filename, "w", encoding="UTF-8") as fp:
            fp.write(etree_tostring(root, pretty_print=True).decode())

    def write_rrgraph_bin(self, filename):
        """Write the routing resource graph (RRGraph) to a binary file."""
        self._update_nodes_edges()
        with open(filename, "w", encoding="UTF-8") as fp:
            self.rrgraph_bin.write(fp)
