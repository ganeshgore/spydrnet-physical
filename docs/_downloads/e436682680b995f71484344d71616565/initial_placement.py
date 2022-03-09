"""
=========================================
Creating FPGA Tiles from OpenFPGA verilog
=========================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

import glob
import os
import logging
import tempfile


import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA
from spydrnet_physical.util.get_floorplan import FloorPlanViz
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


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
    # fpga.design_top_stat()

    fpga.create_placement()
    fpga.show_placement_data("*_0__*")

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()

    fpga.design_top_stat()
    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    dwg = fp.get_svg()
    dwg.saveas("_fpga_initial_placement.svg", pretty=True, indent=4)

    # Save netlist
    base_dir = ("..", "homogeneous_fabric", "_output_2")
    fpga.save_netlist("sb*", os.path.join(*base_dir, "routing"),
                      skip_constraints=False)
    fpga.save_netlist("cb*", os.path.join(*base_dir, "routing"),
                      skip_constraints=False)
    fpga.save_netlist("grid*", os.path.join(*base_dir, "lb"),
                      skip_constraints=False)
    fpga.save_netlist("*tile*", os.path.join(*base_dir, "tiles"),
                      skip_constraints=False)
    fpga.save_netlist("fpga_top", os.path.join(*base_dir),
                      skip_constraints=False)


if __name__ == "__main__":
    main()
