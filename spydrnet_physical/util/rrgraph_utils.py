"""
This script is a placeholder for the rrgraph utility functions that will be used to read and write rrgraph files.
"""

from lxml import etree
import pandas as pd
import re

import capnp  # noqa: F401
from spydrnet_physical.util import rr_graph_uxsdcxx_capnp as rr_capnp
from spydrnet_physical.util.rrgraph_uncompress import rrgraph_bin2xml


class rrgraph(rrgraph_bin2xml):

    def __init__(self, width, height, vpr_arch, routing_chan):
        self.width = width
        self.height = height
        self.routing_chan = routing_chan
        self.node_lookup = [[[] for _ in range(height)] for _ in range(width)]
        self.switches = []
        self.channels = {}
        self.channels["X"] = list(routing_chan for _ in range(width))
        self.channels["Y"] = list(routing_chan for _ in range(width))
        self.segments = []
        self.block_types = []
        self.gridLocs = []
        self.rrgraph_bin = rr_capnp.RrGraph.new_message()
        self.create_channels()

    def _compute_cordinates(self, direction, index, length):
        pass

    def create_node(self, x, y, node_id, ptc_start, seg_type, side, tap=1):
        """
        index: 0
        seg_type: L4
        side: Left/Right/Top/Bottom
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
        xhigh = min(xhigh, self.width)
        yhigh = min(yhigh, self.height)

        phy_length = (xhigh - xlow) + (yhigh - ylow)
        direction_sign = -1 if side in ("Left", "Bottom") else 1

        # Compute the ptc_start point
        ptc_start *= 2
        ptc_start += ((2 * length) - 1) if side in ("Left", "Bottom") else 0
        ptc_end = int(ptc_start + (direction_sign * ((length * 2) + 2)))
        ptc_sequence = ",".join(
            map(
                str,
                range(
                    ptc_start,
                    ptc_end,
                    2 * direction_sign,
                )[:phy_length],
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
        self.node_lookup[x - 1][y - 1].append(node)
        return node

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
        grid = rr_capnp.GridLoc.new_message(
            blockTypeId=block,
            x=x,
            y=y,
            heightOffset=y_offset,
            widthOffset=x_offset,
            layer=layer,
        )
        self.gridLocs.append(grid)
        self.rrgraph_bin.grid = rr_capnp.GridLocs.new_message()
        self.rrgraph_bin.grid.gridLocs = self.gridLocs
        return grid

    def create_segment(
        self, name, length, res_type="uxsdInvalid", c_per_meter=0, r_per_meter=0
    ):
        rr = self.rrgraph_bin
        rr.segments = rr_capnp.Segments.new_message()

        segment_ux = rr_capnp.Segment.new_message(
            id=len(self.segments),
            name=name,
            length=int(length),
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
            chanWidthMax=max(rr.channels.channel.xMax, rr.channels.channel.yMax),
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

    def read_rrgraph_xml(self, filename):
        pass

    def read_rrgraph_bin(self, filename):
        pass

    def _gen_rrgraph_xml(
        self, tool_comment="", tool_name="openfpga-physical", tool_version="v1.0"
    ):
        root = etree.XML("<rr_graph></rr_graph>")
        # Basic information
        root.attrib["tool_comment"] = tool_comment
        root.attrib["tool_name"] = tool_name
        root.attrib["tool_version"] = tool_version

        # Add elements to rrgraph
        channels = self._channels_bin2xml(self.rrgraph_bin.channels)
        switches = self._switches_bin2xml(self.switches)
        segments = self._segments_bin2xml(self.segments)
        block_types = self._block_types_bin2xml(self.rrgraph_bin.blockTypes.blockTypes)
        grids = self._grid_bin2xml(self.rrgraph_bin.grid.gridLocs)
        # rrgraph_segments_bin2xml(self.rrgraph_bin.channels, etree.Element("channels"))
        # rrgraph_block_types_bin2xml(self.rrgraph_bin.channels, etree.Element("channels"))
        # rrgraph_grid_bin2xml(self.rrgraph_bin.channels, etree.Element("channels"))
        # rrgraph_rr_nodes_bin2xml(self.rrgraph_bin.channels, etree.Element("channels"))
        # rrgraph_rr_edges_bin2xml(self.rrgraph_bin.channels, etree.Element("channels"))
        root.append(channels)
        root.append(switches)
        root.append(segments)
        root.append(block_types)
        root.append(grids)
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
            fp.write(etree.tostring(root, pretty_print=True).decode())

    def write_rrgraph_bin(self, filename):
        pass
