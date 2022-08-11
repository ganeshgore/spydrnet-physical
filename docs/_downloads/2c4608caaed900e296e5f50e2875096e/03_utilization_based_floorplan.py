"""
===============================
Utilisation based floorplanning
===============================

This example demostrated how to set utilisation based constraints for each
module durignfloorplanning.

**Not implemented yet**

"""

import glob
import math
import logging

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA, initial_hetero_placement
from spydrnet_physical.util import FPGAGridGen, FloorPlanViz

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

STYLE_SHEET = """
    .over_util {fill:#b22222 !important}
    text{font-family: Lato; font-style: italic; font-size: 350px;}
"""

SCALE = 100
CPP = math.floor(0.46 * SCALE)
SC_HEIGHT = math.floor(2.72 * SCALE)

PROP = "VERILOG.InlineConstraints"


def main():
    """
    Main method
    """
    print("NotImplementedYet")


if __name__ == "__main__":
    main()
