"""
=====================
Rendering Switch Box
=====================

This example demostrate how a switchbox adn connection box  
can be rendered in a SVG format. 

It also shows a simple switch partitionong scheme which splits 
the connection box switches in to two partition with mnimum 
connectivity.

**Full Switch Box**

.. image:: ../../../examples/OpenFPGA/_sb_1__1_.svg
    :width: 500px
    :align: center

**Left Connection Box**

.. image:: ../../../examples/OpenFPGA/_cbx_1__1_.svg
    :width: 150px
    :align: center

**Top Connection Box** 

.. image:: ../../../examples/OpenFPGA/_cbx_1__2_.svg
    :width: 800px
    :align: center

**Splitting Channels in Left Connection Box**

.. image:: ../../../examples/OpenFPGA/_cbx_1__1_split.svg
    :width: 150px
    :align: center

TODO: Extend it to all the switch boxes 
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


def main():
    proj = 'homogeneous_fabric'
    for indx, sb in enumerate(glob.glob(f'{proj}/*_Verilog/routing/sb_1__1_.v')):
        module = path.splitext(path.basename(sb))[0]

        # This creates switch-box rendering class
        sb_render = RoutingRender(module, f"{proj}/FPGA44_gsb/{module}.xml")
        # Print stats of switch box
        sb_render.get_stats(print_header=bool(indx == 0))
        # Render full switch-box and save as SVG
        sb_render.render_switch_pattern()
        sb_render.save(filename="_sb_1__1_.svg")
        sb_render.render_connection_box('left', filename="_cbx_1__1_.svg")
        sb_render.render_connection_box('top', filename="_cbx_1__2_.svg")

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

        # Splitting channel printing
        sb_render.render_connection_box(
            'top',
            pinmap=lambda x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                              10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                              0, 0, 0, 0, 0,
                              20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                              30, 31, 32, 33, 34, 35, 36, 37, 38, 39].index(x),
            filename="_cbx_1__1_split.svg")


if __name__ == "__main__":
    main()
