"""
===========================
Render FPGA Basic Elements
===========================

This example demonstates, how to create OpenFPGA object to perform all
basic transformation and then render primitive FPGA elements using yosys
and `netlistSVG <https://github.com/nturley/netlistsvg>`_ program.


.. hdl-diagram:: ../../../examples/OpenFPGA_basic/_includes.v
   :type: netlistsvg
   :align: center
   :module: cbx_1__1_

"""

import glob
import logging
from itertools import chain

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


def main():
    """
    Main method
    """
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #               Reading homogeneous 4x4 FPGA netlist
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")
    source_files += glob.glob(
        f"{proj}/*_Task/CustomModules/standard_cell_wrapper.v")

    # Create OpenFPGA object
    fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()

    # Remove undriven nets
    fpga.remove_undriven_nets()
    fpga.remove_config_chain()

    # Top level nets to bus
    for i in chain(
        fpga.top_module.get_instances("grid_clb*"),
        fpga.top_module.get_instances("grid_io*"),
        fpga.top_module.get_instances("sb_*"),
    ):
        for p in filter(lambda x: True, i.reference.ports):
            if p.size > 1 and (i.check_all_scalar_connections(p)):
                cable_list = []
                for pin in p.pins[::-1]:
                    cable_list.append(i.pins[pin].wire.cable)
                fpga.top_module.combine_cables(
                    f"{i.name}_{p.name}", cable_list)

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                   Start rendering CBX11
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    cbx11 = next(fpga.library.get_definitions("cbx_1__1_"))
    # Remove configuration elements
    for instance in list(cbx11.get_instances("*mem*")):
        cbx11.remove_child(instance)

    fpga.save_netlist("cbx_1__1_", "./_tmp")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #              Create include files to render
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Create include file to render schematic usign yosys
    cust_proj = f"{proj}/FPGA44_Task/CustomModules"
    veri_proj = f"{proj}/FPGA44_Verilog"
    with open("_includes.v", "w", encoding="UTF-8") as file_ptr:
        file_ptr.write('`include "./_tmp/cbx_1__1_.v"\n')
        file_ptr.write(f'`include "{cust_proj}/standard_cell_primitives.v"\n')
        file_ptr.write(f'`include "{veri_proj}/sub_module/muxes.v"\n')
        file_ptr.write(f'`include "{veri_proj}/sub_module/memories.v"\n')
        file_ptr.write(
            f'`include "{veri_proj}/sub_module/inv_buf_passgate.v"\n')


if __name__ == "__main__":
    main()
