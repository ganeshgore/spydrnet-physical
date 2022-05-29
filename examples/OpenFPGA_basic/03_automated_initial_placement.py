"""
=================================
Auto Floorplan homogeneous design
=================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA_basic/_fpga_auto_initial_placement.svg
   :width: 100%
   :align: center

"""

import glob
import logging
import os
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA, initial_placement, initial_hetero_placement
from spydrnet_physical.util import FloorPlanViz, FPGAGridGen
from spydrnet_physical import PROP

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

STYLE_SHEET = '''
    .over_util {fill:#b22222 !important}
    text{font-family: Lato;}
'''


def main():
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f'{proj}/*_Verilog/lb/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for each_verilog in source_files:
            with open(each_verilog, "r", encoding="UTF-8") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)

    # Convert wires to bus structure
    fpga.annotate_area_information("./support_files/fpga_top_area.rpt")

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
    fpga.register_placement_creator(initial_hetero_placement,
                                    areaFile=f"{proj}/area_info.txt")
    fpga.create_placement()
    fpga.show_placement_data("*_0__*")
    fpga.design_top_stat()

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Adjust Floorplan
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.update_module_label()

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET
    dwg = fp.get_svg()
    dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))
    dwg.saveas("_fpga_auto_initial_placement.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
