"""
===================================================
Floorplanning Classic Tiles for hetergeneous design
===================================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_hetero_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA_tiling/_fpga_auto_initial_heterogeneous_placement.svg
   :width: 70%
   :align: center

"""
# sphinx_gallery_thumbnail_path = '../../examples/OpenFPGA_tiling/_classic_tile_hetero_floorplan.svg'
import glob
import logging
import os
import tempfile
from itertools import chain
import seaborn as sns

import spydrnet as sdn
from copy import deepcopy
from spydrnet_physical.util import (
    FloorPlanViz,
    FPGAGridGen,
    Tile02,
    GridFloorplanGen,
    OpenFPGA,
    initial_hetero_placement,
)

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

PROP = "VERILOG.InlineConstraints"


CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"


STYLE_SHEET = """
    .over_util {fill:#b22222 !important}
    text{font-family: Lato; font-size: 8px}
"""

CPP = 2
SC_HEIGHT = 10


def main():
    print("Need to debug")
    # proj = "../heterogeneous_fabric"
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

    # inst = fpga.design_top_stat()

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Floorplan visualization
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # fpga_grid = FPGAGridGen(
    #     design_name="FPGA8x8",
    #     layout="8x8",
    #     arch_file=f"{proj}/FPGA88_hetero_Task/arch/k6_N10_tileable.xml",
    #     release_root=None,
    # )
    # fpga_grid.enumerate_grid()
    # fpga.load_grid(fpga_grid)
    # fpga.register_placement_creator(
    #     initial_hetero_placement,
    #     areaFile={"grid_clb": [2500, 24 * 8, 24], "cbx_1__1_": [2500 * 0.6, 0, 0]},
    # )

    # shapes = fpga.placement_creator.module_shapes
    # s_param = fpga.placement_creator.s_param
    # logger.info(set(shapes.keys()))
    # logger.info(set(inst.keys()) - set(shapes.keys()))

    # shapes["cbx_1__8_"] = deepcopy(shapes["cbx_1__4_"])
    # shapes["cbx_2__0_"] = deepcopy(shapes["cbx_1__0_"])
    # shapes["cbx_2__2_"] = deepcopy(shapes["cbx_1__1_"])
    # shapes["cbx_2__8_"] = deepcopy(shapes["cbx_1__4_"])

    # shapes["cby_2__1_"] = deepcopy(shapes["cby_0__1_"])
    # shapes["cby_3__1_"] = deepcopy(shapes["cby_0__1_"])
    # shapes["cby_8__1_"] = deepcopy(shapes["cby_4__1_"])

    # shapes["sb_0__8_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_1__2_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_1__8_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_2__0_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_2__1_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_2__2_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_2__8_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_3__0_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_3__1_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_3__8_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_8__0_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_8__1_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_8__2_"] = deepcopy(shapes["sb_1__1_"])
    # shapes["sb_8__8_"] = deepcopy(shapes["sb_1__1_"])

    # shapes["grid_mult_8"] = deepcopy(shapes["grid_clb"])

    # fpga.create_placement()
    # fpga.show_placement_data("*_0__*")
    # fpga.design_top_stat()

    # # Create Tile-02 structure
    # fpga.register_tile_generator(Tile02)
    # fpga.create_tiles()

    # palette = sns.color_palette("pastel", 15).as_hex()
    # for indx, tile in enumerate(fpga.top_module.get_definitions("*tile*")):
    #     tile.data[PROP]["COLOR"] = palette[indx]

    # fpga.design_top_stat()

    # # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # # #           Adjust Floorplan
    # # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # fpga.update_module_label()

    # fp = FloorPlanViz(fpga.top_module)
    # fp.compose(skip_connections=True, skip_pins=True)
    # fp.custom_style_sheet = STYLE_SHEET
    # dwg = fp.get_svg()
    # dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))

    # pattern = dwg.pattern(size=(4 * CPP, 2 * SC_HEIGHT), patternUnits="userSpaceOnUse")
    # pattern.add(dwg.circle(center=(2, 2), r=1, fill="black"))
    # pattern.add(dwg.circle(center=(2, SC_HEIGHT + 2), r=1, fill="red"))
    # dwg.defs.add(pattern)
    # dwg.defs.elements[0].elements[0].attribs["fill"] = pattern.get_funciri()

    # dwg.saveas("_fpga_auto_initial_heterogeneous_placement.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
