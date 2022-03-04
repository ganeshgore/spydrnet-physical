"""
=====================================
Rendering Switch and Connection Boxes
=====================================

This example demostrate how a switch box (SB) and connection box (CB)
can be rendered in a SVG format.

"""

import glob
import os
import logging
import numpy as np

import spydrnet as sdn
from spydrnet_physical.util import cb_renderer, sb_renderer

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG')

scale = 50
SPACING = 150

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(
    LOG_LEVEL='DEBUG', filename="03_render_edge_routing_box")

np.set_printoptions(linewidth=200)


def main():
    gsb = '../homogeneous_fabric/FPGA44_gsb'

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #  This prints horizontal connection box information
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    for indx, conn_box in enumerate(glob.glob(f'{gsb}/cbx_*__*_.xml')):
        module = os.path.splitext(os.path.basename(conn_box))[0]
        cb_render = cb_renderer(module, conn_box)
        print(f"Printing module : ========== {module} ========== ")
        cb_render.report_ipins()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #  This prints vertical connection box information
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    for indx, conn_box in enumerate(glob.glob(f'{gsb}/cby_*__*_.xml')):
        module = os.path.splitext(os.path.basename(conn_box))[0]
        cb_render = cb_renderer(module, conn_box)
        print(f"Printing module : ========== {module} ========== ")
        cb_render.report_ipins()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #  This prints switch box information
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    for indx, conn_box in enumerate(glob.glob(f'{gsb}/sb_*__*_.xml')):
        module = os.path.splitext(os.path.basename(conn_box))[0]
        print(f"Printing module : ========== {module} ========== ")
        sb_render = sb_renderer(module, conn_box)
        sb_render.report_connectivity(filter_direct=True,
                                      in_pin=["chanx_left", "chanx_right",
                                              "chany_top", "chany_bottom"])
        sb_render.report_connectivity(filter_direct=True,
                                      in_pin=["opin_left", "opin_right",
                                              "opin_top", "opin_bottom"])


if __name__ == "__main__":
    main()
