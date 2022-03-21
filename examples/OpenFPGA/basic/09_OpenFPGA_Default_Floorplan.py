"""
=================================================
Render Placement information from Verilog netlist
=================================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

"""
import glob
import logging
import os
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import (FloorPlanViz, FPGAGridGen, OpenFPGA,
                                    openfpga_floorplan)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

PROP = "VERILOG.InlineConstraints"


CBX_COLOR = '#ceefe4'
CBY_COLOR = '#a8d0db'
SB_COLOR = '#ceefe4'
GRID_COLOR = '#f4f0e6'


def main():
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f'{proj}/*_Verilog/lb/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()
    fpga.merge_all_grid_ios()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga_grid = FPGAGridGen(design_name='FPGA4x4', layout="4x4",
                            arch_file=f"{proj}/FPGA44_Task/arch/k6_N10_tileable.xml",
                            release_root=None)
    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)
    fpga.register_placement_creator(openfpga_floorplan)
    placement_creator: openfpga_floorplan = fpga.placement_creator
    placement_creator.grid_plan.set_column_width(1, 50)
    placement_creator.grid_plan.set_column_width(-1, 50)
    fpga.create_placement(fpga.netlist)

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.show_placement_data("*_0__*")
    # fpga.design_top_stat()

    fpga.top_module.data[PROP]["WIDTH"] = 2700
    fpga.top_module.data[PROP]["HEIGHT"] = 2700
    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    dwg = fp.get_svg()
    dwg.saveas("_openfpga_floorplan.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
