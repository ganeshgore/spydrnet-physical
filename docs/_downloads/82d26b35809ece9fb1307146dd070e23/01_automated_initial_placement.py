"""
=================================
Auto floorplan homogeneous design
=================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA_Floorplanning/_fpga_auto_initial_placement.svg
   :width: 100%
   :align: center

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
    line {stroke-width: 30}
    text{font-family: Lato; font-style: italic; font-size: 250px;}
"""

SCALE = 100
CPP = math.floor(0.46 * SCALE)
SC_HEIGHT = math.floor(2.72 * SCALE)

PROP = "VERILOG.InlineConstraints"


def main():
    """
    Main method
    """
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")

    # Create OpenFPGA object
    fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

    # Convert wires to bus structure
    fpga.merge_all_grid_ios()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga_grid = FPGAGridGen(
        design_name="FPGA4x4",
        layout="4x4",
        arch_file=f"{proj}/FPGA44_Task/arch/k6_N10_tileable.xml",
        release_root=None,
    )

    fpga.SC_HEIGHT = SC_HEIGHT
    fpga.CPP = CPP
    fpga.SC_GRID = CPP * SC_HEIGHT

    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)
    fpga.annotate_area_information(f"{proj}/area_info.txt", skipline=1)

    fpga.register_placement_creator(initial_hetero_placement)
    fpga.show_utilization_data()

    # Uncomment this to set module dimensions
    # ====================================================================
    # m = {}
    # m["clb_w"], m["clb_h"] = 360, 8
    # m["cbx11_w"], m["cbx11_h"] = 280, 4
    # m["bottom_cbx_w"], m["bottom_cbx_h"] = 280, 4
    # m["top_cbx_w"], m["top_cbx_h"] = 280, 4

    # m["cby11_w"], m["cby11_h"] = 50, 6
    # m["left_cby_w"], m["left_cby_h"] = 50, 6
    # m["right_cby_w"], m["right_cby_h"] = 50, 6
    # fpga.placement_creator.update_shaping_param(m)
    # ====================================================================

    fpga.placement_creator.derive_sb_paramters()
    fpga.placement_creator.create_shapes()

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Adding Margin
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    shapes = fpga.placement_creator.module_shapes

    for module in ["grid_clb"]:
        shapes[module]["POINTS"][0] -= 16
        shapes[module]["POINTS"][1] -= 2
        shapes[module]["PLACEMENT"][0] += 8
        shapes[module]["PLACEMENT"][1] += 1

    for module in ["cbx_1__0_", "cbx_1__1_", "cbx_1__4_"]:
        shapes[module]["POINTS"][0] -= 16
        shapes[module]["PLACEMENT"][0] += 8

    for module in ["cby_0__1_", "cby_1__1_", "cby_4__1_"]:
        shapes[module]["POINTS"][1] -= 2
        shapes[module]["PLACEMENT"][1] += 1

    fpga.create_placement()
    fpga.show_placement_data(filename="_homogeneous_placement.txt")
    fpga.show_utilization_data()
    fpga.design_top_stat()
    fpga.save_shaping_data("*", scale=1/SCALE)

    fpga.update_module_label()
    fpga.show_utilization_data()

    fpga.update_module_label(
        get_label=lambda x: f"{int(x.data[PROP]['WIDTH'])/CPP:.1f}" +
                            f"x{int(x.data[PROP]['HEIGHT'])/SC_HEIGHT:.1f}" +
                            f"[{x.utilization:.2%}]")
    fpga.show_utilization_data()

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Adjust Floorplan
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET
    dwg = fp.get_svg()
    # This adds placment grid markers
    dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))

    # This standard cell grid
    pattern = dwg.pattern(size=(2 * CPP, 2 * SC_HEIGHT),
                          patternUnits="userSpaceOnUse")
    pattern.add(dwg.circle(center=(4, 4), r=4, fill="black"))
    pattern.add(dwg.circle(center=(4, SC_HEIGHT + 4), r=4, fill="red"))
    dwg.defs.add(pattern)
    dwg.defs.elements[0].elements[0].attribs["fill"] = pattern.get_funciri()

    dwg.saveas("_fpga_auto_initial_placement.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()

# %%
#
# **Placement information**
#
# .. literalinclude:: ../../../examples/OpenFPGA_Floorplanning/_homogeneous_placement.txt
