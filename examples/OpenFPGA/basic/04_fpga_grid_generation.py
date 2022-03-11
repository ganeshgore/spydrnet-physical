"""
===========================
FPGA Layout grid generation 
===========================

This class generates the 2D matrix of the FPGA grid.


**Expected Output**:

.. code-block:: text

    EMPTY     io_top     io_top     io_top     io_top     io_top     io_top     EMPTY
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left    ram9k                 ram9k                 ram9k                io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left     dsp                   dsp                   dsp                 io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    EMPTY   io_bottom  io_bottom  io_bottom  io_bottom  io_bottom  io_bottom    EMPTY

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
                       layout="ultimate")
    fpga.enumerate_grid()
    fpga.print_grid()


if __name__ == "__main__":
    main()
