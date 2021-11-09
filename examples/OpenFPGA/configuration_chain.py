"""
=========================================
Creating FPGA Tiles from OpenFPGA verilog
=========================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

import glob
import logging
import os
import tempfile
from itertools import chain

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA
from spydrnet_physical.util import config_chain_simple
from spydrnet_physical.util.get_floorplan import FloorPlanViz
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


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
    # fpga.design_top_stat()
    fpga.placement_creator.gridIO = True
    fpga.create_placement()
    fpga.show_placement_data("*_0__*")

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()

    fpga.remove_config_chain()
    fpga.remove_undriven_nets()

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

    fpga.register_config_generator(config_chain_simple)
    fpga.add_configuration_scheme()

    # ===============================
    # Florrplan
    # ===============================
    next(fpga.top_module.get_ports("ccff_head")).properties["SIDE"] = "right"
    next(fpga.top_module.get_ports("ccff_head")).properties["OFFSET"] = 50

    next(fpga.top_module.get_ports("ccff_tail")).properties["SIDE"] = "right"
    next(fpga.top_module.get_ports("ccff_tail")).properties["OFFSET"] = 1750

    # ===============================
    # Visualise configuration chain
    # ===============================
    fp = FloorPlanViz(fpga.top_module)
    fp.compose(
        filter_cables=(lambda x: "ccff" in x.name),
        skip_pins=False)
    dwg = fp.get_svg()
    dwg.saveas("_fpga_configuration_chain.svg", pretty=True, indent=4)

    # Save netlist
    base_dir = (".", "homogeneous_fabric", "_output_2")
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
