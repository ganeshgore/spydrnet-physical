"""
=================================================
Render Placement information from Verilog netlist
=================================================

This example demonstate how to render FPGA Tile using ``FloorPlanViz`` class
User can provide external script to render tiles, by default the rendering is
based on ``initial_placement`` class.

This script can be used for shaping and placement of the modules before place and route.

.. image:: ../../../../examples/OpenFPGA/basic/_design_floorplan.svg
   :width: 70%
   :align: center

"""

import glob
import logging
import os
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA, initial_placement
from spydrnet_physical.util.get_floorplan import FloorPlanViz

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
    fpga.register_placement_creator(initial_placement,
                                    areaFile='area_info.txt')
    fpga.create_placement()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Adjust Floorplan
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    cbx11: sdn.Definition = next(fpga.top_module.get_definitions("cbx_1__1_"))
    cbx11.data[PROP]["HEIGHT"] = 100
    cbx11.data[PROP]["WIDTH"] = 200
    cbx11.data[PROP]["COLOR"] = CBX_COLOR

    cby11: sdn.Definition = next(fpga.top_module.get_definitions("cby_1__1_"))
    cby11.data[PROP]["HEIGHT"] = 200
    cby11.data[PROP]["WIDTH"] = 100
    cby11.data[PROP]["COLOR"] = CBY_COLOR

    sb11: sdn.Definition = next(fpga.top_module.get_definitions("sb_1__1_"))
    sb11.data[PROP]["SHAPE"] = 'RectL'
    sb11.data[PROP]["POINTS"] = [100, 50, 50, 100, 50, 50]
    sb11.data[PROP]["COLOR"] = SB_COLOR

    clb: sdn.Definition = next(fpga.top_module.get_definitions("grid_clb"))
    clb.data[PROP]["HEIGHT"] = 300
    clb.data[PROP]["WIDTH"] = 300
    clb.data[PROP]["COLOR"] = GRID_COLOR

    for each in fpga.top_module.get_instances():
        if each.reference is cbx11:
            print(each.data[PROP])
            each.data[PROP]["LOC_X"] += 0
            each.data[PROP]["LOC_Y"] += 50
        if each.reference is cby11:
            print(each.data[PROP])
            each.data[PROP]["LOC_X"] += 50
            each.data[PROP]["LOC_Y"] += 0
        if each.reference is clb:
            print(each.data[PROP])
            each.data[PROP]["LOC_X"] -= 50
            each.data[PROP]["LOC_Y"] -= 50

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.show_placement_data("*_0__*")
    fpga.design_top_stat()

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    dwg = fp.get_svg()
    dwg.saveas("_design_floorplan.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
