"""
=====================
Partition Conn Box 01
=====================

This example demonstrate how pre tech mapped netlist of connection box 
can be partition based on switch patterns. 

1. Calculate difference beetween top and bottom switches on each channels 
2. Sort each channel based on difference 
3. Partition where difference crosses 0 
4. In case thee are multiple point with 0 difference split them equally in both 
partition

"""

import glob
import logging
from os import path
import numpy as np

import spydrnet as sdn
from spydrnet_physical.util import RoutingRender

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG')

scale = 50
SPACING = 150

np.set_printoptions(linewidth=200)


def sort_input_channels(switch_mat, get_bias=False):
    seq = []
    # Add Channel number, diffference and boolean flag to np array
    for i in range(switch_mat.shape[1]):
        diff = (switch_mat[:, i] == "b").sum() + \
            (switch_mat[:, i] == "r").sum() - \
            (switch_mat[:, i] == "t").sum() - \
            (switch_mat[:, i] == "l").sum()
        seq.append((i, diff, diff > 0))
    seq = sorted(seq, key=lambda x: x[1])
    # Find cut locattion
    cur = [e[2] for e in seq].index(True)
    cur -= int([e[1] for e in seq].count(0) * 0.5)
    # Extract channels
    seq = [e[0] for e in seq]
    if get_bias:
        return (seq[:cur], seq[cur:], [e[1] for e in seq])
    return (seq[:cur], seq[cur:])


def main():
    proj = '../homogeneous_fabric'
    for indx, sb in enumerate(glob.glob(f'{proj}/*_Verilog/routing/sb_1__1_.v')):
        module = path.splitext(path.basename(sb))[0]

        # This creates switch-box rendering class
        sb_render = RoutingRender(module, f"{proj}/FPGA44_gsb/{module}.xml")

        # Print vertical connection box (CBY) information and split
        print(" =========== CBY =========== ")
        sw_left = sb_render.report_ipins("left", show=False)
        sw_left[sw_left == 'x'] = "l"
        sw_right = sb_render.report_ipins("right", show=False)
        sw_right[sw_right == 'x'] = "r"
        sw = np.vstack([sw_left, sw_right])
        left_chan, right_chan = sort_input_channels(sw)
        print(f"left_chan {sorted(left_chan)}")
        print(f"right_chan {sorted(right_chan)}")
        sb_render.render_ipin(sw)
        sb_render.render_ipin(sw[:, left_chan])
        sb_render.render_ipin(sw[:, right_chan])

        # Print vertical connection box (CBX) information and split
        print(" =========== CBX =========== ")
        sw_top = sb_render.report_ipins("top", show=False)
        sw_top[sw_top == 'x'] = "t"
        sw_bottom = sb_render.report_ipins("bottom", show=False)
        sw_bottom[sw_bottom == 'x'] = "b"
        sw = np.vstack([sw_top, sw_bottom])
        top_chan, bottom_chan = sort_input_channels(sw)
        print(f"top_chan {sorted(top_chan)}")
        print(f"bottom_chan {sorted(bottom_chan)}")
        sb_render.render_ipin(sw)
        sb_render.render_ipin(sw[:, top_chan])
        sb_render.render_ipin(sw[:, bottom_chan])


if __name__ == "__main__":
    main()
