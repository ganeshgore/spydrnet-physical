""" 
"""
import logging
import pickle
import os
from glob import glob
from os.path import basename, dirname, realpath

import spydrnet as sdn
from spydrnet_physical.util import FabricKeyGenCCFF, FPGAGridGen

logger = logging.getLogger("spydrnet_logs")


class custom_fabric_key(FabricKeyGenCCFF):
    pass

    # def create_fabric_key(self, pattern=None):
    # Extend or replace if you want


def main():
    """
    Main method to execute function
    """
    # Parse architecture file and get layput block
    try:
        VPR_ARCH_FILE = glob(("task/arch/*vpr*"))[0]
        PROJ_NAME = basename(dirname(realpath(__file__)))
    except IndexError:
        logger.exception("Architecture file not found ['task/arch/*vpr*']")

    # Load the existing grid from generate shapes
    fpga = pickle.load(open(f"{PROJ_NAME}_fpgagridgen.pickle", "rb"))

    # Uncomment this to recreate the FPGA grid
    # fpga.enumerate_grid()
    # fpga.render_layout(grid_io=True)

    fabric_key = custom_fabric_key(fpga)
    fabric_key.create_fabric_key("vertical")

    filename = os.path.join(f"{PROJ_NAME}_CCFF_Chain.svg")
    fabric_key.render_svg(filename=filename)
    fabric_key.save_fabric_key(filename="fabric_key.xml")


if __name__ == "__main__":
    main()
