"""
=================================================
Render Placement information from Verilog netlist
=================================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../examples/OpenFPGA/basic/_hetero_design_floorplan.svg
   :width: 70%
   :align: center

"""

import glob
import logging
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import (FloorPlanViz, FPGAGridGen,
                                    GridFloorplanGen, OpenFPGA,
                                    initial_placement)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO', filename="floorplan_heterpgeneous")


PROP = "VERILOG.InlineConstraints"


CBX_COLOR = '#d9d9f3'
CBY_COLOR = '#a8d0db'
SB_COLOR = '#ceefe4'
GRID_COLOR = '#ddd0b1'
HETERO_COLOR = '#6E6858'


def main():
    proj = "../hetrogeneous_fabric/"
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

    fpga = OpenFPGA(grid=(8, 8), netlist=netlist)

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()
    fpga.merge_all_grid_ios()
    fpga.design_top_stat()
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    fpga_grid = FPGAGridGen(design_name='FPGA8x8', layout="8x8",
                            arch_file=f"{proj}/FPGA88_hetero_Task/arch/k6_N10_tileable.xml",
                            release_root=None)
    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)

    # = = = = = = = = = = = = = = = = = = = = = = =
    #         Shaping Information
    # = = = = = = = = = = = = = = = = = = = = = = =
    GRID_X, GRID_Y = 200, 200
    CLB_W, CLB_H = 140, 140
    CBX_WIDTH, CBY_HEIGHT = 100, 100

    # Derived varaiable
    CBY_WIDTH = GRID_X-CLB_W
    CBX_HEIGHT = GRID_Y-CLB_H

    # Edge blocks dimensions
    LEFT_CBY_WIDTH, LEFT_CBY_HEIGHT = CBY_WIDTH, CBY_HEIGHT
    RIGHT_CBY_WIDTH, RIGHT_CBY_HEIGHT = CBY_WIDTH, CBY_HEIGHT
    TOP_CBX_WIDTH, TOP_CBX_HEIGHT = CBX_WIDTH, CBX_HEIGHT
    BOTTOM_CBX_WIDTH, BOTTOM_CBX_HEIGHT = CBX_WIDTH, CBX_HEIGHT

    # Margins
    CLB_MARG_L, CLB_MARG_R, CLB_MARG_T, CLB_MARG_B = 0, 0, 0, 0
    CBX_MARG_L, CBX_MARG_R, CBX_MARG_T, CBX_MARG_B = 0, 0, 0, 0
    CBY_MARG_L, CBY_MARG_R, CBY_MARG_T, CBY_MARG_B = 0, 0, 0, 0

    # SB_1__1_ Dimensions
    a, b, c, d, e, f = [CBX_HEIGHT, 0.5*(CLB_W-CBX_WIDTH),
                        0.5*(CLB_H-CBY_HEIGHT), CBY_WIDTH,
                        0.5*(CLB_W-CBX_WIDTH), 0.5*(CLB_H-CBY_HEIGHT)]

    module_shapes = {
        "cbx_1__0_": {"W": BOTTOM_CBX_WIDTH, "H": BOTTOM_CBX_HEIGHT},
        "cbx_1__1_": {"W": CBX_WIDTH, "H": CBX_HEIGHT},
        "cbx_1__8_": {"W": TOP_CBX_WIDTH, "H": TOP_CBX_HEIGHT},
        "cbx_2__0_": {"W": CBX_WIDTH, "H": CBX_HEIGHT},
        "cbx_2__2_": {"W": CBX_WIDTH, "H": CBX_HEIGHT},
        "cbx_2__8_": {"W": CBX_WIDTH, "H": CBX_HEIGHT},
        "cby_0__1_": {"W": LEFT_CBY_WIDTH, "H": LEFT_CBY_HEIGHT},
        "cby_1__1_": {"W": CBY_WIDTH, "H": CBY_HEIGHT},
        "cby_2__1_": {"W": CBY_WIDTH, "H": CBY_HEIGHT},
        "cby_3__1_": {"W": CBY_WIDTH, "H": CBY_HEIGHT},
        "cby_8__1_": {"W": RIGHT_CBY_WIDTH, "H": RIGHT_CBY_HEIGHT},
        "grid_clb": {"W": CLB_W, "H": CLB_H},
        "grid_mult_8": {"W": CLB_W, "H": GRID_Y+CLB_H},
        "sb_0__0_": {"SHAPE": "cross", "POINTS": [a, 0, c, d, e, 0]},
        "sb_0__1_": {"SHAPE": "cross", "POINTS": [a, 0, c, d, e, f]},
        "sb_0__8_": {"SHAPE": "cross", "POINTS": [a, 0, 0, d, e, f]},
        "sb_1__0_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, 0]},
        "sb_1__1_": {"SHAPE": "cross", "POINTS": [a, b, c, d, 0, f]},
        "sb_1__2_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, f]},
        "sb_1__8_": {"SHAPE": "cross", "POINTS": [a, b, 0, d, e, f]},
        "sb_2__0_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, 0]},
        "sb_2__1_": {"SHAPE": "cross", "POINTS": [a, 0, c, d, e, f]},
        "sb_2__2_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, f]},
        "sb_2__8_": {"SHAPE": "cross", "POINTS": [a, b, 0, d, e, f]},
        "sb_3__0_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, 0]},
        "sb_3__1_": {"SHAPE": "cross", "POINTS": [a, b, c, d, e, f]},
        "sb_3__8_": {"SHAPE": "cross", "POINTS": [a, b, 0, d, e, f]},
        "sb_8__0_": {"SHAPE": "cross", "POINTS": [a, b, c, d, 0, 0]},
        "sb_8__1_": {"SHAPE": "cross", "POINTS": [a, 0, c, d, 0, f]},
        "sb_8__2_": {"SHAPE": "cross", "POINTS": [a, b, c, d, 0, f]},
        "sb_8__8_": {"SHAPE": "cross", "POINTS": [a, b, 0, d, 0, f]},
    }

    for eachm, param in module_shapes.items():
        if param:
            module = next(fpga.top_module.get_definitions(eachm))
            if "SHAPE" in param.keys():
                module.data[PROP]["SHAPE"] = param["SHAPE"]
                module.data[PROP]["POINTS"] = param["POINTS"]
            else:
                module.data[PROP]["WIDTH"] = param["W"]
                module.data[PROP]["HEIGHT"] = param["H"]

        print(eachm, param)

    # Create grid plan
    grid_plan = GridFloorplanGen(17, 17, grid_x=200, grid_y=200)

    grid_plan.offset_x = 100
    grid_plan.offset_y = 100

    for i in range(2, 17+1, 2):
        grid_plan.set_column_width(i, CLB_W)

    for i in range(2, 17+1, 2):
        grid_plan.set_row_height(i, CLB_H)

    for i in range(1, 17+1, 2):
        grid_plan.set_column_width(i, CBY_WIDTH)

    for i in range(1, 17+1, 2):
        grid_plan.set_row_height(i, CBX_HEIGHT)

    # # # dwg = grid_plan.render_grid()
    # # # dwg.saveas("_fpga_grid_floorplan.svg", pretty=True, indent=4)
    fpga_grid.print_grid()
    with open("_complete_metrics.txt", "w") as fp:
        for y in range(2*(fpga_grid.height-1), -1, -1):
            for x in range((fpga_grid.width*2)-1):
                fp.write(" {0:^12} ".format(fpga_grid.get_top_instance(x, y)))
            fp.write("\n")

    for xi in range((2*fpga_grid.width)-3, 0, -1):
        for yi in range((2*fpga_grid.height)-3, 0, -1):
            X_OFFSET, Y_OFFSET = 0, 0
            inst_name = fpga_grid.get_top_instance(xi, yi)
            points = grid_plan.get_x_y(xi-1, yi-1)
            inst = next(fpga.top_module.get_instances(f"*{inst_name}"))
            if "cbx" in inst_name:
                X_OFFSET, Y_OFFSET = 0.5*(CLB_W-CBX_WIDTH), 0
            if "cby" in inst_name:
                X_OFFSET, Y_OFFSET = 0, 0.5*(CLB_H-CBY_HEIGHT)
            if "sb" in inst_name:
                PTS = inst.reference.data[PROP]["POINTS"]
                X_OFFSET, Y_OFFSET = PTS[1]*-1, PTS[-1]*-1
            inst.data[PROP]['LOC_X'] = points[0] + X_OFFSET
            inst.data[PROP]['LOC_Y'] = points[1] + Y_OFFSET

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # #           Adjust Floorplan
    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    for cbx in fpga.top_module.get_definitions("cbx_*"):
        cbx.data[PROP]["COLOR"] = CBX_COLOR

    for cby in fpga.top_module.get_definitions("cby_*"):
        cby.data[PROP]["COLOR"] = CBY_COLOR

    for sb in fpga.top_module.get_definitions("sb_*"):
        sb.data[PROP]["COLOR"] = SB_COLOR

    clb: sdn.Definition = next(fpga.top_module.get_definitions("grid_clb"))
    clb.data[PROP]["COLOR"] = GRID_COLOR

    mult8: sdn.Definition = next(fpga.top_module.get_definitions("*mult*"))
    mult8.data[PROP]["COLOR"] = HETERO_COLOR

    # # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.show_placement_data("*")
    # # fpga.design_top_stat()

    fpga.top_module.data[PROP]["WIDTH"] = 1900
    fpga.top_module.data[PROP]["HEIGHT"] = 1900

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    dwg = fp.get_svg()
    dwg.add(grid_plan.render_grid(return_group=True))
    dwg.saveas("_hetero_design_floorplan.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()

# %%
# Output
# ------
#
# .. literalinclude:: ../../../examples/OpenFPGA_basic/_floorplan_heterpgeneous_spydrnet.log
#
#
