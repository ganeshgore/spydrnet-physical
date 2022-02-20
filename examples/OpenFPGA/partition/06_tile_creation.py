"""
================================
FPGA Tiles from OpenFPGA Verilog
================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

import glob
import json
import logging
from pathlib import Path
import tempfile
from itertools import chain
from os import path

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA
from spydrnet_physical.util.get_names import get_names


logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    proj = '../homogeneous_fabric'
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

    # fpga.create_grid_clb_feedthroughs()

    # Before Creating Tiles
    fpga.design_top_stat()

    # fpga.register_tile_generator(Tile02)
    # fpga.create_tiles()
    for module in list(netlist.get_definitions("*b_1__1*")):
        # Flatten the netlist
        for instance in list(module.get_instances('*_ipin_*')):
            module.flatten_instance(instance)
        for instance in list(module.get_instances('*_track_*')):
            module.flatten_instance(instance)

        parts_files = glob.glob(f"./tiles_data/{module.name}_part_*.json")
        for part, each_file in enumerate(parts_files):
            instance_list = json.load(open(each_file))
            module.merge_instance([next(module.get_instances(i)) for i in instance_list],
                                  new_definition_name=f'{module.name}_{part}',
                                  new_instance_name=f'{module.name}_{part}_1')

        for eachInst in module.references:
            print(f"Flatterning {eachInst.name}")
            fpga.top_module.flatten_instance(eachInst)

    # After Tile creation
    fpga.design_top_stat()

    # Save netlist
    base_dir = "_output_tile02"
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    fpga.save_netlist("sb*", path.join(base_dir, "routing"))
    fpga.save_netlist("cb*", path.join(base_dir, "routing"))
    fpga.save_netlist("grid*", path.join(base_dir, "lb"))
    fpga.save_netlist("*tile*", path.join(base_dir, "tiles"))
    fpga.save_netlist("fpga_top", path.join(base_dir))


if __name__ == "__main__":
    main()
