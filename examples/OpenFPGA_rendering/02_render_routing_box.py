"""
=====================================
Rendering Switch and Connection Boxes
=====================================

This example demostrate how a switch box (SB) and connection box (CB)
can be rendered in a SVG format.

**Full Switch Box [ SB_1__1_ ]**

  .. image:: ../../../examples/OpenFPGA_rendering/_sb_1__1_.svg
      :width: 500px
      :align: center

  **Horizontal Connection Box**

  .. image:: ../../../examples/OpenFPGA_rendering/_cbx_1__1_.svg
      :width: 150px
      :align: center

  **Vertical Connection Box**

  .. image:: ../../../examples/OpenFPGA_rendering/_cbx_1__2_.svg
      :width: 800px
      :align: center

  **Arbitrary arrangement of vertical connection box channels and pins**

  .. image:: ../../../examples/OpenFPGA_rendering/_cbx_1__1_arrangement.svg
      :width: 800px
      :align: center

"""

import glob
import logging
from os import path

import numpy as np
import spydrnet as sdn
from spydrnet_physical.util import RoutingRender

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="DEBUG", filename="02_render_routing_box")

scale = 50
SPACING = 150

np.set_printoptions(linewidth=200)


def main():
    proj = "../homogeneous_fabric"
    return
    for indx, sb in enumerate(glob.glob(f"{proj}/*_Verilog/routing/sb_1__1_.v")):
        module = path.splitext(path.basename(sb))[0]

        # This creates switch-box rendering class
        sb_render = RoutingRender(module, f"{proj}/FPGA44_gsb/{module}.xml")
        # Print stats of switch box
        sb_render.get_stats(print_header=bool(indx == 0))
        # Render full switch-box and save as SVG
        sb_render.render_switch_pattern()
        sb_render.save(filename=f"_{module}.svg")
        sb_render.render_connection_box("left", filename="_cbx_1__1_.svg")
        sb_render.render_connection_box("top", filename="_cbx_1__2_.svg")

        # Report incoming channel information
        print("\n left incoming channels")
        sb_render.report_incoming_channels("left")
        print("\n right incoming channels")
        sb_render.report_incoming_channels("right")
        print("\n top incoming channels")
        sb_render.report_incoming_channels("top")
        print("\n bottom incoming channels")
        sb_render.report_incoming_channels("bottom")

        # Report outgoing channel information
        print("\nleft outgoing channels")
        sb_render.report_outgoing_channels("left")
        print("\nright outgoing channels")
        sb_render.report_outgoing_channels("right")
        print("\ntop outgoing channels")
        sb_render.report_outgoing_channels("top")
        print("\nbottom outgoing channels")
        sb_render.report_outgoing_channels("bottom")

        # Arbitrary Arrangement of Connection Box
        def channel_map(side, x):
            lbl = side[0].upper() + str(x)
            # fmt: off
            chan_map = [
            "R0", "R1", "R2", "R3", "L0", "L1", "L2", "L3",
            "R4", "R5", "R6", "R7", "", "",
            "L4", "L5", "L6", "L7", "R8", "R9", "L8", "L9", ]
            # fmt: on
            if lbl in chan_map:
                indx = chan_map.index(lbl) if lbl in chan_map else x
                return (20 - indx) if side == "left" else indx
            else:
                return x

        sb_render.render_connection_box(
            "top",
            # fmt: off
            pinmap=lambda x: [0,  2,  4,  6,  8,
                              10,  12, 14,  16,  18,
                              20, 22, 24, 26, 28,
                              30, 32, 34, 36, 38,
                              None, None, None, None, None,
                              1, 3, 5, 7, 9,
                              11, 13, 15, 17, 19,
                              21, 23, 25, 27, 29,
                              31, 33, 35, 37, 39].index(x),

            channel_map=channel_map,
            filename="_cbx_1__1_arrangement.svg",
        )
        # fmt: on


if __name__ == "__main__":
    main()
