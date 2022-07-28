"""
===============================
Split CBs and SBs across fabric
===============================

Given two set of channels, split all the CBs and SBs in the design 
This script expects external input of how vertical and horizontal channels 
are grouped.

Partitions are provided thoguh variable ``h_chan`` and ``v_chan``
And partition modules are placed in ``cbx_1__1__0.v`` and ``cbx_1__1__1.v``

.. program-output:: bash -c "cd ../../../ && pwd && ls"
   :ellipsis: 50

"""

import fnmatch as fn
import glob
import json
import logging
import tempfile
from os import path
from pathlib import Path
from pprint import pprint

import matplotlib.pyplot as plt
import networkx as nx
import pydot
import spydrnet as sdn
from networkx.classes.function import nodes
from networkx.drawing.nx_pydot import to_pydot
from networkx.readwrite import json_graph
from networkx.relabel import convert_node_labels_to_integers
from sklearn import cluster
from spydrnet_physical.util import (OpenFPGA, get_names, run_metis,
                                    write_metis_graph)
from spydrnet_physical.util.shell import launch_shell

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG', filename="module_partition")


def main():
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Read FPGA Netlist
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
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

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Vertical and Horizontal channel groups
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
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

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Split routing resources
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    for module in list(netlist.get_definitions("*_1__1*")):
        # Flatten the netlist
        for instance in list(module.get_instances('*_ipin_*')):
            module.flatten_instance(instance)
        for instance in list(module.get_instances('*_track_*')):
            module.flatten_instance(instance)

        # Create Graph
        graph = module.get_connectivity_network(split_ports=True)

        # Annotate graph
        if module.name.startswith("sb"):
            graph = clean_and_annotate_sb_graph(graph, h_chan, v_chan)
            cuts = 4
        else:
            graph = clean_and_annotate_cb_graph(graph, h_chan, v_chan)
            cuts = 2

        save_graph(f"_{module.name}_graph_pre", graph=graph)
        # json.dump(json_graph.node_link_data(graph),
        #           open(f"_{module.name}_graph.json", 'w'), indent=6)

        vweights = nx.get_node_attributes(graph, "weight")

        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        # Run using external metis engine
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        write_metis_graph(nx.to_numpy_array(graph.to_undirected()),
                          eweights=True, vweights=vweights,
                          filename=f"_module_experiments_{module.name}.csr")
        cbx_membership = run_metis(
            filename=f"_module_experiments_{module.name}.csr", cuts=cuts,
            options=f"-objtype cut -minconn -niter 10000")
        # save_paritioned_graph(module.name, graph, cbx_membership)
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        # pprint(list(zip(list(nx.get_node_attributes(
        #     graph, 'label').values()), list(nx.get_node_attributes(
        #         graph, 'weight').values()), cbx_membership)))
        instance_list = [[] for _ in range(cuts)]
        for index, color in enumerate(cbx_membership):
            node = graph.nodes[index]
            if not node.get("port", True):
                instance_list[color].append(node["label"])

        for part in range(cuts):
            # Save partition data in json file
            json.dump(instance_list[part], open(
                f"_{module.name}_part_{part}.json", 'w'), indent=6)
            # Create Submodules
            module.merge_instance([next(module.get_instances(i)) for i in instance_list[part]],
                                  new_definition_name=f'{module.name}_{part}',
                                  new_instance_name=f'{module.name}_{part}_1')

        print_partition_info(instance_list)

        Path("_output/routing").mkdir(parents=True, exist_ok=True)
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


def save_partitioned_graph(graph):
    # Save graph
    graph_dot = to_pydot(graph)
    graph_dot.set_rankdir("LR")

    inputs = (pydot.Cluster('inputs1', label='', rank="source"),
              pydot.Cluster('inputs2', label='', rank="source"))
    outputs = (pydot.Cluster('outputs1', label='', rank="sink"),
               pydot.Cluster('outputs2', label='', rank="sink"))
    part1 = pydot.Cluster('part1', label='',
                          style='filled', color='red')
    part2 = pydot.Cluster('part2', label='',
                          style='filled', color='green')
    pass


def show_graph_stats(graph):
    nodes = graph.nodes
    print(" ========== Nodes ==========")
    print("\n".join([f"{node:2} {nodes[node]['label']:15} {nodes[node]}"
                     for node in nodes]))
    print(" ========== Edges ==========")
    print("\n".join(nx.generate_edgelist(graph, data=True)))


def print_partition_info(partitions):
    print("============ Partition stats =============")
    f_str = '{:<15s} ' + ' {:<15}'*len(partitions)
    print(f_str.format('', *[f"P{i+1}" for i in range(len(partitions))]))
    print("==========================================")
    print(f_str.format('mux',
                       *[len([p for p in partition if "mux" in p])
                         for partition in partitions]))
    print(f_str.format('mem',
                       *[len([p for p in partition if "mem" in p])
                         for partition in partitions]))
    print(f_str.format('CCDFF',
                       *[len([p for p in partition if "CCDFF" in p])
                         for partition in partitions]))
    print(f_str.format('ASSIGN',
                       *[len([p for p in partition if "ASSIGN" in p])
                         for partition in partitions]))


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


def clean_and_annotate_sb_graph(graph, h_chan, v_chan):
    logger.info("Splitting switch box structure")
    # Get list of Nodes in the current graph
    nodes = list(nx.get_node_attributes(graph, 'label').values())
    node_indx = len(nodes)

    channel_map = {
        ("top", "left"): h_chan["P1"] + v_chan["P1"],
        ("left", "bottom"): h_chan["P2"] + v_chan["P1"],
        ("bottom", "right"): h_chan["P2"] + v_chan["P2"],
        ("right", "top"): h_chan["P1"] + v_chan["P2"]
    }

    # Merge Input Nodes
    for dir in [("top", "left"), ("left", "bottom"),
                ("bottom", "right"), ("right", "top")]:
        graph.add_node(node_indx, weight=100,
                       label=f"{dir[0]}_{dir[1]}_input_ports")
        in_indx = node_indx
        node_indx += node_indx

        for in_pins in fn.filter(nodes, f"{dir[0]}_{dir[1]}_grid*_pin_O*"):
            graph = nx.contracted_nodes(graph, in_indx, nodes.index(in_pins))
        for in_pins in fn.filter(nodes, f"{dir[1]}_{dir[0]}_grid*_pin_O*"):
            graph = nx.contracted_nodes(graph, in_indx, nodes.index(in_pins))

        for track in channel_map[dir]:
            label = {"T": "chany", "B": "chany",
                     "L": "chanx", "R": "chanx"}[track[0]]
            if track[0] in (dir[0][0].upper(), dir[1][0].upper()):
                label = fn.filter(nodes,
                                  f"{label}_{track[0].lower()}*_in*_{track[1]}")[0]
                graph = nx.contracted_nodes(graph, in_indx,
                                            nodes.index(label))
            else:
                track_0 = {"l": "r", "r": "l", "t": "b",
                           "b": "t"}[track[0].lower()]
                label = fn.filter(nodes,
                                  f"{label}_{track_0}*_out*_{track[1]}")[0]
                graph = nx.contracted_nodes(graph, in_indx,
                                            nodes.index(label))

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


def save_paritioned_graph(module, graph, cbx_membership):
    # Save graph
    cuts = max(cbx_membership)+1
    nodes = list(nx.get_node_attributes(graph, 'label').values())
    graph_dot = to_pydot(graph)
    graph_dot.set_rankdir("LR")

    inputs = tuple(pydot.Cluster(f'inputs{i}', label='', rank="source")
                   for i in range(cuts))
    outputs = tuple(pydot.Cluster(f'outputs{i}', label='', rank="sink")
                    for i in range(cuts))

    clusters = []
    for part in range(cuts):
        print(part)
        clusters.append(pydot.Cluster(f'part{part}', label='', style='filled',
                                      color=['azure', 'beige', 'bisque', 'aquamarine'][part]))

    for indx, node in enumerate(nodes):
        if fn.fnmatch(node, "chan*"):
            inputs[cbx_membership[indx]].add_node(
                graph_dot.get_node(str(indx))[0])
        elif fn.fnmatch(node, "*pin_I*"):
            outputs[cbx_membership[indx]].add_node(
                graph_dot.get_node(str(indx))[0])
        else:
            clusters[int(cbx_membership[indx])].add_node(
                graph_dot.get_node(str(indx))[0])

    for part in range(cuts):
        graph_dot.add_subgraph(clusters[part])
        clusters[part].add_subgraph(inputs[part])
        clusters[part].add_subgraph(outputs[part])

    graph_dot.write_dot(f'_{module}_nx_graph.dot')
    graph_dot.write_svg(f'_{module}_nx_graph.svg')
    print(f'_{module}_nx_graph.svg')
    logger.debug(f"Saved partition graph in _{module}_nx_graph.svg")


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
