"""
===========================================
FPGA Tiles from OpenFPGA Verilog version 02
===========================================

This example demonstrates how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

"""

import glob
import logging
import tempfile
import json
from os import path
from pprint import pprint, pformat
from networkx.readwrite import json_graph

import networkx as nx
import matplotlib.pyplot as plt
import pydot
import spydrnet as sdn
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import (OpenFPGA, run_metis, write_metis_graph)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    proj = '../homogeneous_fabric/*_Verilog'
    source_files = glob.glob(f'{proj}/lb/*.v')
    source_files += glob.glob(f'{proj}/routing/*.v')
    source_files += glob.glob(f'{proj}/sub_module/*.v')
    source_files += glob.glob(f'{proj}/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    for modules in ["cbx_1__0_", "cbx_1__1_", "cbx_1__4_",
                    "cby_0__1_", "cby_1__1_", "cby_4__1_"]:
        # for modules in ['cbx_1__1_', ]:
        cb_module = next(netlist.get_definitions(modules))
        clean_netlist(cb_module)
        cb_module_graph = cb_module.get_connectivity_network()
        annotate_graph(cb_module_graph)

        cb_nodes = list(nx.get_node_attributes(
            cb_module_graph, 'name').values())
        cb_vweights = nx.get_node_attributes(cb_module_graph, "weight")

        # Run using external metis
        write_metis_graph(nx.to_numpy_array(cb_module_graph),
                          eweights=True, vweights=cb_vweights,
                          filename=f"_partition_experiments_{modules}.csr")
        cbx_membership = run_metis(
            filename=f"_partition_experiments_{modules}.csr", cuts=2,
            options="-objtype cut -minconn -niter 100 -ncuts 3 ")
        partitions = [[], []]
        for index, color in enumerate(cbx_membership):
            partitions[color].append(cb_module_graph.nodes[index])

        print_partition_info(partitions)
        json.dump(partitions[0], open(f"_{modules}_0.json", 'w'), indent=6)
        json.dump(partitions[1], open(f"_{modules}_1.json", 'w'), indent=6)

    # Read Fabric Again
    proj = '../homogeneous_fabric'
    source_files = glob.glob(f'{proj}/lb/*.v')
    source_files += glob.glob(f'{proj}/routing/*.v')
    source_files += glob.glob(f'{proj}/sub_module/*.v')
    source_files += glob.glob(f'{proj}/fpga_top.v')
    source_files += glob.glob(
        f'{proj}/*_Task/CustomModules/standard_cell_primitives.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)
    fpga.design_top_stat()

    # Flatten Modules
    # for modules in ["cbx_1__1_", ]:
    for modules in ["cbx_1__0_", "cbx_1__1_", "cbx_1__4_",
                    "cby_0__1_", "cby_1__1_", "cby_4__1_"]:
        cb_module = next(netlist.get_definitions(modules))
        for instance in list(cb_module.get_instances('*ipin*')):
            logger.debug(f"Flattening {instance.name}")
            cb_module.flatten_instance(instance)

        data = json.load(open(f"_{modules}_0.json", "r"))
        cb_module.merge_instance(
            [next(cb_module.get_instances(inst['name']))
                for inst in data if inst['port'] is False],
            new_definition_name=f"{modules}_0")
        tile = next(cb_module._library.get_definitions(f"{modules}_0"))
        tile.OptPins()

        data = json.load(open(f"_{modules}_1.json", "r"))
        cb_module.merge_instance(
            [next(cb_module.get_instances(inst['name']))
                for inst in data if inst['port'] is False],
            new_definition_name=f"{modules}_1")
        tile = next(cb_module._library.get_definitions(f"{modules}_1"))
        tile.OptPins()

    base_dir = (".", "_output")

    # Save netlist
    base_dir = (".", "_output")
    fpga.save_netlist("sb*", path.join(*base_dir, "routing"))
    fpga.save_netlist("cb*", path.join(*base_dir, "routing"))
    fpga.save_netlist("grid*", path.join(*base_dir, "lb"))
    # fpga.save_netlist("*tile*", path.join(*base_dir, "tiles"))
    fpga.save_netlist("fpga_top", path.join(*base_dir))


def print_partition_info(partitions):
    print("============= Parition stats =============")
    f_str = '{:<15s} {:<15} {:<15}'
    print(f_str.format('', 'P1', 'P2'))
    print("==========================================")
    print(f_str.format('chanx_left',
                       len([p for p in partitions[0] if "chanx_left" in p['label']]),
                       len([p for p in partitions[1] if "chanx_left" in p['label']])))
    print(f_str.format('chanx_right',
                       len([p for p in partitions[0] if "chanx_right" in p['label']]),
                       len([p for p in partitions[1] if "chanx_right" in p['label']])))
    print(f_str.format('chany_top',
                       len([p for p in partitions[0] if "chany_top" in p['label']]),
                       len([p for p in partitions[1] if "chany_top" in p['label']])))
    print(f_str.format('chany_bottom',
                       len([p for p in partitions[0]
                            if "chany_bottom" in p['label']]),
                       len([p for p in partitions[1] if "chany_bottom" in p['label']])))
    print(f_str.format('pin_I',
                       len([p for p in partitions[0] if "pin_I" in p['label']]),
                       len([p for p in partitions[1] if "pin_I" in p['label']])))
    print(f_str.format('CCDFF',
                       len([p for p in partitions[0] if "CCDFF" in p['label']]),
                       len([p for p in partitions[1] if "CCDFF" in p['label']])))
    print(f_str.format('top_grid',
                       len([p for p in partitions[0] if "top_grid" in p['label']]),
                       len([p for p in partitions[1] if "top_grid" in p['label']])))
    print(f_str.format('bottom_grid',
                       len([p for p in partitions[0] if "bottom_grid" in p['label']]),
                       len([p for p in partitions[1] if "bottom_grid" in p['label']])))
    pass


def annotate_graph(graph):
    nodes = list(nx.get_node_attributes(graph, 'label').values())

    # Add higher weights to grid input pins
    for pin in [indx for indx, node in enumerate(nodes) if "pin_I" in node]:
        graph.nodes[pin]["weight"] = 999

    # Annotate weight in labels
    for indx, node_name in enumerate(nodes):
        graph.nodes[indx]["label"] = f"{node_name}_[{graph.nodes[indx].get('weight', 0)}]"


def clean_netlist(module):
    # Flattern all the instances (Muxes + Configuration Mem)
    for instance in list(module.get_instances('*ipin*')):
        logger.debug(f"Flattening {instance.name}")
        module.flatten_instance(instance)

    # Remove global ports and signals
    for signal in ["ccff_tail", "ccff_head", "prog_reset", "cfg_done",
                   "prog_clk", "chan*_out"]:
        for port in list(module.get_ports(signal)):
            module.remove_port(port)
        for cable in list(module.get_cables(signal)):
            module.remove_cable(cable)

    # Get unwanted instances
    for instance in ["*ASSIG*", ]:
        module.remove_children_from(module.get_instances(instance))

    # # Disconnect scan_chain
    # for dff in module.get_instances("*_CCDFF_*"):
    #     port = next(dff.get_ports("*Q*"))
    #     if port.pins[0].wire:
    #         port.pins[0].wire.disconnect_pin(port.pins[0])

    # for instance in ["*CCDFF*", ]:
    #     module.remove_children_from(module.get_instances(instance))

    # module.remove_cables_from(list(module.get_cables("*CCDFF*")))
    # module.remove_cables_from(list(module.get_cables("*ccff_tail*")))
    # Split Chanx_ports
    for chan_in_port in list(module.get_ports("chan*_in")):
        chan_in_port.split()

    for dir in ["top", "left", "right", "bottom"]:
        try:
            module.combine_ports(f"{dir}_pin_I",
                                 list(module.get_ports(f"*{dir}_grid_*_pin_I*")))
        except:
            pass


if __name__ == "__main__":
    main()
