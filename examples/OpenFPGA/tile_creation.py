"""
=========================================
Creating FPGA Tiles from OpenFPGA verilog
=========================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

from os import path
import tempfile
import glob
from pprint import pprint
import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import OpenFPGA_Tile01


def main():
    source_files = glob.glob('homogeneous_fabric/*_Verilog/lb/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/routinlg/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/sub_module/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA_Tile01(grid=(4, 4), netlist=netlist)
    fpga.design_top_stat()

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()

    # Save netlist
    base_dir = (".", "homogeneous_fabric", "_output")
    fpga.save_netlist("tile_*", path.join(*base_dir, "tiles"))
    fpga.save_netlist("grid*", path.join(*base_dir, "lb"))
    fpga.save_netlist("*b_*", path.join(*base_dir, "routing"))
    fpga.save_netlist("fpga_top", path.join(*base_dir))


if __name__ == "__main__":
    main()
