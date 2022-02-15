"""
==========================
Split all the CBs and SBs 
==========================

Given two groups of channels, split all the CBs and SBs in the design 
This script expects external input of how vertical and horizontal channels 
are grouped.

Partitions are provided thoguh variable `h_chan` and `v_chan`
And partition modules are placed in `cbx_1__1__0.v` and `cbx_1__1__1.v`

"""

import glob
import logging
import tempfile
import json
import fnmatch as fn
from os import path, makedirs
from pprint import pprint, pformat
from networkx.classes.function import nodes
from networkx.readwrite import json_graph
from networkx.relabel import convert_node_labels_to_integers

import networkx as nx
import matplotlib.pyplot as plt
import pydot
import spydrnet as sdn
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import get_names
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import (OpenFPGA, run_metis, write_metis_graph)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG', filename="module_partition")


def main():
    # Read FPGA Netlist
    proj = '../homogeneous_fabric/*_Verilog'
    task = '../homogeneous_fabric/*_Task'
    source_files = glob.glob(f'{proj}/lb/*.v')
    source_files += glob.glob(f'{proj}/routing/*.v')
    source_files += glob.glob(f'{proj}/sub_module/*.v')
    source_files += glob.glob(f'{task}/CustomModules/standard_cell_primitives.v')
    source_files += glob.glob(f'{proj}/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    # Vertical and Horizontal channel groups
    h_chan = {"P1": [('L', 0), ('L', 1), ('L', 2), ('L', 3), ('L', 4),
                     ('L', 5), ('L', 6), ('L', 7), ('L', 8), ('L', 9),
                     ('R', 10), ('R', 11), ('R', 12), ('R', 13), ('R', 14),
                     ('R', 15), ('R', 16), ('R', 17), ('R', 18), ('R', 19)],
              "P2": [('L', 10), ('L', 11), ('L', 12), ('L', 13), ('L', 14),
                     ('L', 15), ('L', 16), ('L', 17), ('L', 18), ('L', 19),
                     ('R', 0), ('R', 1), ('R', 2), ('R', 3), ('R', 4),
                     ('R', 5), ('R', 6), ('R', 7), ('R', 8), ('R', 9)]}
    v_chan = {"P1": [('T', 0), ('T', 1), ('T', 2), ('T', 3), ('T', 4),
                     ('T', 5), ('T', 6), ('T', 7), ('T', 8), ('T', 9),
                     ('B', 10), ('B', 11), ('B', 12), ('B', 13), ('B', 14),
                     ('B', 15), ('B', 16), ('B', 17), ('B', 18), ('B', 19)],
              "P2": [('T', 10), ('T', 11), ('T', 12), ('T', 13), ('T', 14),
                     ('T', 15), ('T', 16), ('T', 17), ('T', 18), ('T', 19),
                     ('B', 0), ('B', 1), ('B', 2), ('B', 3), ('B', 4),
                     ('B', 5), ('B', 6), ('B', 7), ('B', 8), ('B', 9)]}

    # Split CBX
    for module in list(netlist.get_definitions("cbx_1__1*")):
        for instance in list(module.get_instances('*_ipin_*')):
            module.flatten_instance(instance)

        graph = module.get_connectivity_network(split_ports=True)
        graph = clean_and_annotate_cb_graph(graph, h_chan, v_chan)

        save_graph(f"_{module.name}_graph_pre", graph=graph)

        vweights = nx.get_node_attributes(graph, "weight")
        print(f"********************")
        print(f"nodes {len(graph)}")

        # Run using external metis
        write_metis_graph(nx.to_numpy_array(graph.to_undirected()),
                          eweights=True, vweights=vweights,
                          filename=f"_module_experiments_{module.name}.csr")
        cbx_membership = run_metis(
            filename=f"_module_experiments_{module.name}.csr", cuts=2,
            options="-objtype cut -minconn -niter 100 -ncuts 3 ")
        instance_list = [[], []]
        for index, color in enumerate(cbx_membership):
            node = graph.nodes[index]
            if not node.get("port", True):
                instance_list[color].append(node["label"])

        json.dump(instance_list[0], open(
            f"_{module.name}_part_0.json", 'w'), indent=6)
        json.dump(instance_list[1], open(
            f"_{module.name}_part_1.json", 'w'), indent=6)

        print_partition_info(instance_list)

        # Create submodule
        module.merge_instance([next(module.get_instances(i)) for i in instance_list[0]],
                              new_definition_name=f'{module.name}_0',
                              new_instance_name=f'{module.name}_0_1')
        module.merge_instance([next(module.get_instances(i)) for i in instance_list[1]],
                              new_definition_name=f'{module.name}_1',
                              new_instance_name=f'{module.name}_1_1')

        makedirs("_output/routing")
        sdn.compose(netlist, f"_output/routing/{module.name}.v",
                    definition_list=[module.name], skip_constraints=True)
        sdn.compose(netlist, f"_output/routing/{module.name}_0.v",
                    definition_list=[f"{module.name}_0"], skip_constraints=True)
        sdn.compose(netlist, f"_output/routing/{module.name}_1.v",
                    definition_list=[f"{module.name}_1"], skip_constraints=True)


def save_graph(fllename, graph=None, graph_dot=None):
    if not graph_dot:
        graph_dot = to_pydot(graph)
    graph_dot.set_rankdir("LR")
    graph_dot.write_svg(f'{fllename}.svg')
    graph_dot.write_dot(f'{fllename}.dot')


def show_graph_stats(graph):
    nodes = graph.nodes
    print(" ========== Nodes ==========")
    print("\n".join([f"{node:2} {nodes[node]['label']:15} {nodes[node]}"
                     for node in nodes]))
    print(" ========== Edges ==========")
    print("\n".join(nx.generate_edgelist(graph, data=True)))


def print_partition_info(partitions):
    print("============ Partition stats =============")
    f_str = '{:<15s} {:<15} {:<15}'
    print(f_str.format('', 'P1', 'P2'))
    print("==========================================")
    print(f_str.format('mux',
                       len([p for p in partitions[0] if "mux" in p]),
                       len([p for p in partitions[1] if "mux" in p])))
    print(f_str.format('CCDFF',
                       len([p for p in partitions[0] if "CCDFF" in p]),
                       len([p for p in partitions[1] if "CCDFF" in p])))
    print(f_str.format('ASSIGN',
                       len([p for p in partitions[0] if "ASSIGN" in p]),
                       len([p for p in partitions[1] if "ASSIGN" in p])))


def clean_and_annotate_cb_graph(graph, h_chan, v_chan):
    # Get list of Nodes in the current graph
    nodes = list(nx.get_node_attributes(graph, 'label').values())
    node_indx = len(nodes)

    # Merge Output Nodes
    for dir in ["top", "left", "right", "bottom"]:
        if fn.filter(nodes, f"{dir}_grid*_pin_I*"):
            graph.add_node(node_indx, label=f"{dir}_pin_I", weight=999)
            for node in fn.filter(nodes, f"{dir}_grid*_pin_I*"):
                graph = nx.contracted_nodes(graph,
                                            node_indx, nodes.index(node))
            node_indx += 1

    # Merge Input Nodes as per provided partitions list
    for dir in ["chanx", "chany"]:
        if fn.filter(nodes, f"{dir}_*"):
            for lbl, tracks in {"chanx": h_chan, "chany": v_chan}[dir].items():
                graph.add_node(node_indx, label=f"{dir}_{lbl}", weight=10000)
                for track in tracks:
                    side, pin = track
                    oside = {"L": "R", "R": "L", "T": "B", "B": "T"}
                    # print(fn.filter(nodes, f"{dir}_{side.lower()}*_{pin}"))
                    for node in fn.filter(nodes, f"{dir}_{side.lower()}*_in_{pin}"):
                        graph = nx.contracted_nodes(graph, node_indx,
                                                    nodes.index(node))
                    for node in fn.filter(nodes, f"{dir}_{oside[side].lower()}*_out_{pin}"):
                        graph = nx.contracted_nodes(graph, node_indx,
                                                    nodes.index(node))
                node_indx += 1

    # Added weights for less important nets
    for from_n, to_n in graph.edges:
        if "ccff_tail" in graph[from_n][to_n]["edge_name"]:
            graph[from_n][to_n]["weight"] = 99

    # Remove global signals
    mapping = {graph.nodes[i]["label"]: i for i in graph.nodes}
    for signal in ["prog_reset", "cfg_done", "prog_clk"]:
        for name in fn.filter(mapping, signal):
            graph.remove_node(mapping[name])

    graph.remove_nodes_from(list(nx.isolates(graph)))
    graph.remove_edges_from(list(nx.selfloop_edges(graph)))
    graph = convert_node_labels_to_integers(graph)
    return graph


def annotate_graph(graph):
    nodes = list(nx.get_node_attributes(graph, 'label').values())

    # Add higher weights to grid input pins
    for pin in [indx for indx, node in enumerate(nodes) if "pin_I" in node]:
        graph.nodes[pin]["weight"] = 999

    for dir in ["top", "left", "right", "bottom"]:
        if f"{dir}_pin_I" in nodes:
            for edge in graph.in_edges(nodes.index(f"{dir}_pin_I"), data=True):
                graph[edge[0]][edge[1]]["weight"] = 999

    # Annotate weight in labels
    for indx, node_name in enumerate(nodes):
        graph.nodes[indx]["label"] = f"{node_name}_[{graph.nodes[indx].get('weight', 0)}]"


def prepare_netlist(module):
    # Flattern all the instances (Muxes + Configuration Mem)
    for instance in list(module.get_instances('*_ipin_*')):
        module.flatten_instance(instance)

    # Split input channel ports
    for chan_in_port in list(module.get_ports("chan*_in")):
        chan_in_port.split()


if __name__ == "__main__":
    main()
