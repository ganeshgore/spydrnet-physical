"""
=========================================
Creating FPGA Tiles from OpenFPGA verilog
=========================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

import glob
import logging
import tempfile
from itertools import chain
from os import path
from pprint import pformat, pprint

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA, Tile01, get_names

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG')


def main():
    source_files = glob.glob('homogeneous_fabric/*_Verilog/lb/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/routing/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/sub_module/*.v')
    source_files += glob.glob('homogeneous_fabric/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)
    fpga.design_top_stat()

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

    # Before Creating Tiles
    fpga.design_top_stat()

    fpga.register_tile_generator(Tile01)
    fpga.create_tiles()

    # After Tile creation
    fpga.design_top_stat()

    # Save netlist
    base_dir = (".", "homogeneous_fabric", "_output")
    fpga.save_netlist("sb*", path.join(*base_dir, "routing"))
    fpga.save_netlist("cb*", path.join(*base_dir, "routing"))
    fpga.save_netlist("grid*", path.join(*base_dir, "lb"))
    fpga.save_netlist("*tile*", path.join(*base_dir, "tiles"))
    fpga.save_netlist("fpga_top", path.join(*base_dir))


if __name__ == "__main__":
    main()
