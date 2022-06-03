"""
==============================
RenderFPGA Pre Generation Grid
==============================

This class generates the 2D matrix of the FPGA grid.


**layout section of Architecture file**


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

    fpga.render_layout()


if __name__ == "__main__":
    main()
