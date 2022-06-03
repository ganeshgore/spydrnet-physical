"""
==============================
RenderFPGA Pre Generation Grid
==============================

This class generates the 2D matrix of the FPGA grid.


**layout section of Architecture file**

.. image:: ../../../examples/OpenFPGA_basic/_small_layout_render.svg
   :width: 90%
   :align: center

.. image:: ../../../examples/OpenFPGA_basic/_ultimate_layout_render.svg
   :width: 90%
   :align: center

"""

import logging

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    fpga = FPGAGridGen(design_name="example_design",
                       arch_file="./support_files/vpr_arch_render_demo.xml",
                       release_root="_release",
                       layout="small")
    fpga.enumerate_grid()

    fpga.render_layout(filename="_small_layout_render.svg")

    fpga = FPGAGridGen(design_name="example_design",
                       arch_file="./support_files/vpr_arch_render_demo.xml",
                       release_root="_release",
                       layout="ultimate")
    fpga.enumerate_grid()

    fpga.render_layout(filename="_ultimate_layout_render.svg")


if __name__ == "__main__":
    main()
