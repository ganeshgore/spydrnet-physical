"""
This script is a placeholder for the rrgraph utility functions that will be used to read and write rrgraph files.
"""
from lxml import etree
import pandas as pd

import capnp  # noqa: F401
from spydrnet_physical.util import rr_graph_uxsdcxx_capnp


class rrgraph:

    def __init__(self, width, height, vpr_arch, routing_chan):
        self.width = width
        self.height = height
        self.node_lookup = []
        self.rrgraph_bin = rr_graph_uxsdcxx_capnp.RrGraph.new_message()

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
        ptc_start += ((2*length)-1) if side in ("Left", "Bottom") else 0
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

        node = rr_graph_uxsdcxx_capnp.Node.new_message(
            id=node_id,
            capacity=1,
            type=["chanx", "chany"][int(side in ("Top", "Bottom"))],
            direction=["incDir", "decDir"][int(side in ("Left", "Bottom"))],
            loc=rr_graph_uxsdcxx_capnp.NodeLoc.new_message(
                xlow=xlow,
                xhigh=xhigh,
                ylow=ylow,
                yhigh=yhigh,
                twist=2,
                ptc=ptc_sequence,
            ),
            timing=rr_graph_uxsdcxx_capnp.NodeTiming.new_message(r=0, c=0),
            segment=rr_graph_uxsdcxx_capnp.NodeSegment.new_message(),
        )
        return node

    def create_switch(self):
        pass

    def read_rrgraph_xml(self, filename):
        pass

    def read_rrgraph_bin(self, filename):
        pass

    def write_rrgraph_xml(self, filename):
        pass

    def write_rrgraph_bin(self, filename):
        pass
