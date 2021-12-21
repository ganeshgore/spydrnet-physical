"""
===========================
Render FPGA Basic Elements
===========================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

.. hdl-diagram:: ../../../../examples/OpenFPGA/basic/_includes.v
   :type: netlistsvg
   :align: center
   :module: cbx_1__1_

"""

import glob
import logging
import tempfile
from itertools import chain
from os import path

import spydrnet as sdn
from spydrnet.ir import library
from spydrnet_physical.util import (OpenFPGA, Tile01)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f'{proj}/*_Verilog/lb/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/fpga_top.v')
    source_files += glob.glob(
        f'{proj}/*_Task/CustomModules/standard_cell_wrapper.v')

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

    # Remove undriven nets
    fpga.remove_undriven_nets()
    fpga.remove_config_chain()

    # Top level nets to bus
    for i in chain(fpga.top_module.get_instances("grid_clb*"),
                   fpga.top_module.get_instances("grid_io*"),
                   fpga.top_module.get_instances("sb_*")):
        for p in filter(lambda x: True, i.reference.ports):
            if p.size > 1 and (i.check_all_scalar_connections(p)):
                cable_list = []
                for pin in p.pins[::-1]:
                    cable_list.append(i.pins[pin].wire.cable)
                fpga.top_module.combine_cables(
                    f"{i.name}_{p.name}", cable_list)

    fpga.create_grid_clb_feedthroughs()

    cbx11 = next(fpga.library.get_definitions("cbx_1__1_"))
    for instance in list(cbx11.get_instances("*mem*")):
        cbx11.remove_child(instance)

    fpga.save_netlist("cbx_1__1_", "./_tmp")

    # Create include file to render schematic usign yosys
    with open("_includes.v", "w") as fp:
        fp.write('`include "./_tmp/cbx_1__1_.v"\n')
        fp.write(
            f'`include "{proj}/FPGA44_Task/CustomModules/standard_cell_primitives.v"\n')
        fp.write(
            f'`include "{proj}/FPGA44_Verilog/SRC/sub_module/muxes.v"\n')
        fp.write(
            f'`include "{proj}/FPGA44_Verilog/SRC/sub_module/memories.v"\n')
        fp.write(
            f'`include "{proj}/FPGA44_Verilog/SRC/sub_module/inv_buf_passgate.v"\n')


if __name__ == "__main__":
    main()
