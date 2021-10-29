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


def main():
    dir_path = path.dirname(path.realpath(__file__))
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

    work = next(netlist.get_libraries("work"))
    topModule = next(work.get_definitions("fpga_top"))

    # work.design_stat()
    # create_grid_clb_bus(work)
    # create_grid_io_bus(work)
    # create_sb_bus(work)
    # create_cb_bus(work)

if __name__ == "__main__":
    main()