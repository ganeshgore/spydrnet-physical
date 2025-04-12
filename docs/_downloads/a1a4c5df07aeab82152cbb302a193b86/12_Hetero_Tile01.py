"""
===================================================
Floorplanning Classic Tiles for hetergeneous design
===================================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_hetero_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA_tiling/_classic_tile_hetero_floorplan.svg
   :width: 70%
   :align: center

"""

import glob
import logging
import os
import tempfile
from itertools import chain

import spydrnet as sdn
from spydrnet_physical.util import (
    FloorPlanViz,
    FPGAGridGen,
    Tile02,
    GridFloorplanGen,
    OpenFPGA,
)

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"


def main():
    proj = "../heterogeneous_fabric"
    source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")

    # Create OpenFPGA object
    fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()
    fpga.merge_all_grid_ios()

    # Convert top level independent nets to bus
    for i in chain(
        fpga.top_module.get_instances("grid_clb*"),
        fpga.top_module.get_instances("grid_io*"),
        fpga.top_module.get_instances("sb_*"),
    ):
        for p in filter(lambda x: True, i.reference.ports):
            if p.size > 1 and (i.check_all_scalar_connections(p)):
                cable_list = []
                for pin in p.pins[::-1]:
                    cable_list.append(i.pins[pin].wire.cable)
                cable = fpga.top_module.combine_cables(f"{i.name}_{p.name}", cable_list)
                cable.is_downto = False

    fpga.design_top_stat()

    # Create Tile-02 structure
    fpga.register_tile_generator(Tile02)
    fpga.create_tiles()

    fpga.design_top_stat()


if __name__ == "__main__":
    main()
