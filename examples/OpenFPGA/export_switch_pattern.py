"""
===========================
Render FPGA Basic Elements
===========================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

.. hdl-diagram:: ../../../examples/OpenFPGA/_includes.v
   :type: netlistsvg
   :align: center
   :module: cbx_1__1_

"""

import glob
import logging
from itertools import chain
from os import path

import spydrnet as sdn
from spydrnet.ir import library
from spydrnet_physical.util import RoutingRender
from svgwrite import Drawing
from svgwrite.container import Group
from svgwrite.shapes import Polyline

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG')

scale = 50
SPACING = 150


def main():
    for indx, sb in enumerate(glob.glob('homogeneous_fabric/*_Verilog/routing/sb_0__0_.v')):
        module = path.splitext(path.basename(sb))[0]
        sb_render = RoutingRender(
            module,
            f"homogeneous_fabric/FPGA44_gsb/{module}.xml")
        sb_render.get_stats(print_header=bool(indx == 0))
        sb_render.render_switch_pattern()
        sb_render.save()


if __name__ == "__main__":
    main()
