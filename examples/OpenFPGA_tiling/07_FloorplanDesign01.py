"""
===========================
Floorplanning Classic Tiles
===========================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

**Deprecated**

"""

import glob
import logging
import math
from itertools import chain

import spydrnet as sdn
from spydrnet_physical.util import (
    FloorPlanViz,
    FPGAGridGen,
    GridFloorplanGen,
    OpenFPGA,
    initial_placement,
)

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"


def main():
    pass
    # proj = "../homogeneous_fabric"
    # source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    # source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    # source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    # source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")

    # # Create OpenFPGA object
    # fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

    # # Convert wires to bus structure
    # fpga.create_grid_clb_bus()
    # fpga.create_grid_io_bus()
    # fpga.create_sb_bus()
    # fpga.create_cb_bus()
    # fpga.merge_all_grid_ios()

    # # Convert top level independent nets to bus
    # for i in chain(
    #     fpga.top_module.get_instances("grid_clb*"),
    #     fpga.top_module.get_instances("grid_io*"),
    #     fpga.top_module.get_instances("sb_*"),
    # ):
    #     for p in filter(lambda x: True, i.reference.ports):
    #         if p.size > 1 and (i.check_all_scalar_connections(p)):
    #             cable_list = []
    #             for pin in p.pins[::-1]:
    #                 cable_list.append(i.pins[pin].wire.cable)
    #             cable = fpga.top_module.combine_cables(f"{i.name}_{p.name}", cable_list)
    #             cable.is_downto = False

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Floorplan visualization
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # fpga.register_placement_creator(initial_placement, areaFile=f"{proj}/area_info.txt")
    # fpga_grid = FPGAGridGen(
    #     design_name="FPGA4x4",
    #     layout="4x4",
    #     arch_file=f"{proj}/FPGA44_Task/arch/k6_N10_tileable.xml",
    #     release_root=None,
    # )
    # fpga_grid.enumerate_grid()
    # fpga.load_grid(fpga_grid)
    # fpga.create_placement()

    # p = fpga.placement_creator

    # # Create grid plan
    # grid_plan = GridFloorplanGen(9, 9, grid_x=200, grid_y=180)

    # grid_plan.offset_x = 10
    # grid_plan.offset_y = 10

    # for i in range(2, 9 + 1, 2):
    #     grid_plan.set_column_width(i, p.CLB_W * 4)

    # for i in range(2, 9 + 1, 2):
    #     grid_plan.set_row_height(i, p.CLB_H * 4)

    # for i in range(1, 9 + 1, 2):
    #     grid_plan.set_column_width(i, (p.CLB_GRID_X - p.CLB_W) * 4)

    # for i in range(1, 9 + 1, 2):
    #     grid_plan.set_row_height(i, (p.CLB_GRID_Y - p.CLB_H) * 4)

    # # dwg = grid_plan.render_grid()
    # # dwg.saveas("_fpga_grid_floorplan.svg", pretty=True, indent=4)

    # for xi in range(1, 10):
    #     for yi in range(1, 10):
    #         X_OFFSET, Y_OFFSET = 0, 0
    #         inst_name = fpga_grid.get_top_instance(xi, yi)
    #         points = grid_plan.get_x_y(xi - 1, yi - 1)
    #         inst = next(fpga.top_module.get_instances(f"*{inst_name}"))
    #         if "cbx" in inst_name:
    #             X_OFFSET, Y_OFFSET = 2 * (p.CLB_W - p.CBX_W), 0
    #         elif "cby" in inst_name:
    #             X_OFFSET, Y_OFFSET = 0, 2 * (p.CLB_H - p.CBY_H)
    #         elif "sb" in inst_name:
    #             PTS = inst.reference.properties["POINTS"]
    #             X_OFFSET, Y_OFFSET = PTS[1] * -1, PTS[-1] * -1
    #         inst.properties["LOC_X"] = math.floor(points[0] + X_OFFSET)
    #         inst.properties["LOC_Y"] = math.floor(points[1] + Y_OFFSET)

    # fpga.top_module.properties["WIDTH"] = grid_plan.width + 20
    # fpga.top_module.properties["HEIGHT"] = grid_plan.height + 20
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Adjust Floorplan
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # for cbx in fpga.top_module.get_definitions("cbx_*"):
    #     cbx.properties["COLOR"] = CBX_COLOR

    # for cby in fpga.top_module.get_definitions("cby_*"):
    #     cby.properties["COLOR"] = CBY_COLOR

    # for sb in fpga.top_module.get_definitions("sb_*"):
    #     sb.properties["COLOR"] = SB_COLOR

    # clb: sdn.Definition = next(fpga.top_module.get_definitions("grid_clb"))
    # clb.properties["COLOR"] = GRID_COLOR

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # fpga.show_placement_data("sb_*")
    # # fpga.design_top_stat()

    # fp = FloorPlanViz(fpga.top_module)
    # fp.compose(skip_connections=True, skip_pins=True)
    # dwg = fp.get_svg()
    # dwg.add(grid_plan.render_grid(return_group=True))
    # dwg.saveas("_classic_tile_floorplan.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
