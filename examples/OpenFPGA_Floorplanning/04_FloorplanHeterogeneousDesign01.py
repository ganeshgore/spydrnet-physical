"""
===============================
Heterogeneous Design Placement
===============================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA_Floorplanning/_hetero_design_floorplan.svg
   :width: 70%
   :align: center

"""

import glob
import logging
import math
from copy import deepcopy

import spydrnet as sdn
from spydrnet_physical.util import (
    FloorPlanViz,
    FPGAGridGen,
    OpenFPGA,
    initial_hetero_placement,
)

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO", filename="floorplan_heterpgeneous")


CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"
HETERO_COLOR = "#6E6858"

FPGA_WIDTH = 8
FPGA_HEIGHT = 8

SCALE = 100
CPP = math.floor(0.46 * SCALE)
SC_HEIGHT = math.floor(2.72 * SCALE)


STYLE_SHEET = """
    symbol {mix-blend-mode: difference;}
    symbol[id*='mult'] * {number:01; fill:#BC85C3;}
    .over_util {fill:#b22222 !important}
    text{font-family: Lato; font-style: italic; font-size: 750px;}
    rect.highlight_box { fill:none; stroke-width:40; stroke:green;}
    text.highlight_box { font-size:500px; font-weight:800; fill:red}
"""

MULT_COLS = [2, 8]


def main():
    """
    Main method
    """

    proj = "../heterogeneous_fabric/"
    source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")

    # Create OpenFPGA object
    fpga = OpenFPGA(grid=(8, 8), verilog_files=source_files)

    # Convert wires to bus structure
    fpga.merge_all_grid_ios()
    fpga.design_top_stat()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    fpga_grid = FPGAGridGen(
        design_name="FPGA8x8",
        layout="8x8",
        arch_file=f"{proj}/FPGA88_hetero_Task/arch/k6_N10_tileable.xml",
        release_root=None,
    )
    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)
    fpga.annotate_area_information(f"{proj}/area_info.txt", skipline=1)

    fpga.SC_HEIGHT = SC_HEIGHT
    fpga.CPP = CPP
    fpga.SC_GRID = CPP * SC_HEIGHT

    # = = = = = = = = = = = = = = = = = = = = = = =
    #         Shaping Information
    # = = = = = = = = = = = = = = = = = = = = = = =

    fpga.register_placement_creator(
        initial_hetero_placement,
        areaFile={},
    )

    m = {}
    m["clb_w"], m["clb_h"] = 340, 60
    m["cbx11_w"], m["cbx11_h"] = 220, 10
    m["bottom_cbx_w"], m["bottom_cbx_h"] = 220, 18
    m["top_cbx_w"], m["top_cbx_h"] = 220, 40

    m["cby11_w"], m["cby11_h"] = 120, 40
    m["left_cby_w"], m["left_cby_h"] = 180, 40
    m["right_cby_w"], m["right_cby_h"] = 160, 40

    fpga.placement_creator.update_shaping_param(m)
    fpga.placement_creator.derive_sb_paramters()
    fpga.placement_creator.create_shapes()

    shapes = fpga.placement_creator.module_shapes

    inst = fpga.design_top_stat()
    logger.info("This are extra modules to floorplan")
    logger.info(set(inst.keys()) - set(shapes.keys()))

    shapes["cbx_2__0_"] = deepcopy(shapes["cbx_1__0_"])
    shapes["cbx_2__2_"] = deepcopy(shapes["cbx_1__1_"])
    shapes["cbx_2__8_"] = deepcopy(shapes["cbx_1__8_"])
    shapes["cby_2__1_"] = deepcopy(shapes["cby_1__1_"])
    shapes["cby_3__1_"] = deepcopy(shapes["cby_1__1_"])
    shapes["sb_1__2_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__0_"] = deepcopy(shapes["sb_1__0_"])
    shapes["sb_2__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__2_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__8_"] = deepcopy(shapes["sb_1__8_"])
    shapes["sb_3__0_"] = deepcopy(shapes["sb_1__0_"])
    shapes["sb_3__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_3__8_"] = deepcopy(shapes["sb_1__8_"])
    shapes["sb_8__2_"] = deepcopy(shapes["sb_8__1_"])

    shapes["grid_mult_8"] = deepcopy(shapes["grid_clb"])
    shapes["grid_mult_8"]["POINTS"][1] += m["clb_h"] + m["cbx11_h"]

    shapes["sb_2__1_"]["POINTS"][1] = 0  # Trim right side
    shapes["sb_2__1_"]["PLACEMENT"][0] = 0  # Reset x offset
    shapes["sb_8__1_"]["POINTS"][1] = 0  # Trim right side
    shapes["sb_8__1_"]["PLACEMENT"][0] = 0  # Reset x offset

    # Make few modules unique to fit in floorplan
    inst_list = []
    for col in MULT_COLS:
        inst_list += [f"sb_{col-1}__{i}_" for i in range(1, FPGA_HEIGHT, 2)]
    fpga.top_module.make_instance_unique(
        next(fpga.top_module.get_instances(inst_list[0])),
        "sb_7__1_",
        instance_list=inst_list,
    )
    shapes["sb_7__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_7__1_"]["POINTS"][-2] = 0  # Trim right side
    shapes.pop("sb_1__1_")

    fpga.create_placement()
    fpga.update_module_label()

    additional_styles = fpga.get_overutils_styles()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.show_placement_data("*")

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET + additional_styles
    dwg = fp.get_svg()
    dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))

    pattern = dwg.pattern(size=(4 * CPP, 2 * SC_HEIGHT), patternUnits="userSpaceOnUse")
    pattern.add(dwg.circle(center=(2, 2), r=1, fill="black"))
    pattern.add(dwg.circle(center=(2, SC_HEIGHT + 2), r=1, fill="red"))
    dwg.defs.add(pattern)
    dwg.defs.elements[0].elements[0].attribs["fill"] = pattern.get_funciri()

    filename = "_hetero_design_floorplan.svg"
    dwg.saveas(filename, pretty=True, indent=4)


if __name__ == "__main__":
    main()
