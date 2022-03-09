"""
==================================
Partition Conn Box 02 - Simplified
==================================

This is simplified script Partition Conn Box 02

**cbx_1__1_ Split**

.. image:: ../../../../examples/OpenFPGA/partition/_cbx_1__1__nx_graph.svg
    :align: center
    :width: 50% 

**cby_1__1_ Split**

.. image:: ../../../../examples/OpenFPGA/partition/_cby_1__1__nx_graph.svg
    :align: center
    :width: 50% 

.. program-output:: ls
   :ellipsis: 2 

"""

import glob
import logging
import tempfile
import json
import fnmatch as fn
from os import path
from pprint import pprint, pformat
from networkx.classes.function import nodes
from networkx.readwrite import json_graph
from networkx.relabel import convert_node_labels_to_integers

import networkx as nx
import matplotlib.pyplot as plt
import pydot
import spydrnet as sdn
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import (OpenFPGA, run_metis, write_metis_graph)

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='DEBUG', filename="switch_partition_03")


def main():
    proj = '../homogeneous_fabric/*_Verilog'
    task = '../homogeneous_fabric/*_Task'
    source_files = glob.glob(f'{proj}/lb/*.v')
    source_files += glob.glob(f'{proj}/routing/*.v')
    source_files += glob.glob(f'{proj}/sub_module/*.v')
    source_files += glob.glob(f'{proj}/fpga_top.v')
    source_files += glob.glob(f'{task}/CustomModules/standard_cell_wrapper.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    for modules in ['cbx_1__1_', 'cby_1__1_']:
        cb_module = next(netlist.get_definitions(modules))
        prepare_netlist(cb_module)
        sdn.compose(netlist, f"_{modules}_temp.v",
                    skip_constraints=True, definition_list=[modules])
        graph = cb_module.get_connectivity_network(split_ports=True)
        graph = clean_cb_graph(graph)
        logger.info(f"graph {len(graph)}")
        save_graph(f"_{modules}_nx_graph_pre", graph=graph)

        print(f"nodes {len(graph)}")
        # show_graph_stats(graph)
        annotate_graph(graph)

        nodes = list(nx.get_node_attributes(graph, 'label').values())
        cb_vweights = nx.get_node_attributes(graph, "weight")

        # Run using external metis
        write_metis_graph(nx.to_numpy_array(graph.to_undirected()),
                          eweights=True, vweights=cb_vweights,
                          filename=f"_partition_experiments_{modules}.csr")
        cbx_membership = run_metis(
            filename=f"_partition_experiments_{modules}.csr", cuts=2,
            options="-objtype cut -minconn -niter 100 -ncuts 3 ")
        partitions = [[], []]

        for index, color in enumerate(cbx_membership):
            partitions[color].append(graph.nodes[index])

        print_partition_info(partitions)

        # Store partition information in the external JSON file
        json.dump(partitions[0], open(f"_{modules}_0.json", 'w'), indent=6)
        json.dump(partitions[1], open(f"_{modules}_1.json", 'w'), indent=6)

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

        for indx, node in enumerate(nodes):
            if fn.fnmatch(node, "chan*"):
                inputs[cbx_membership[indx]].add_node(
                    graph_dot.get_node(str(indx))[0])
            elif fn.fnmatch(node, "*pin_I*"):
                outputs[cbx_membership[indx]].add_node(
                    graph_dot.get_node(str(indx))[0])
            elif cbx_membership[indx] == 1:
                part1.add_node(graph_dot.get_node(str(indx))[0])
            elif cbx_membership[indx] == 0:
                part2.add_node(graph_dot.get_node(str(indx))[0])

        graph_dot.add_subgraph(part1)
        graph_dot.add_subgraph(part2)
        part2.add_subgraph(inputs[0])
        part1.add_subgraph(inputs[1])
        part2.add_subgraph(outputs[0])
        part1.add_subgraph(outputs[1])

        graph_dot.write_dot(f'_{modules}_nx_graph.dot')
        graph_dot.write_svg(f'_{modules}_nx_graph.svg')


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


def clean_cb_graph(graph):
    nodes = list(nx.get_node_attributes(graph, 'label').values())
    node_indx = len(nodes)
    # Merge Output Nodes
    for dir in ["top", "left", "right", "bottom"]:
        if fn.filter(nodes, f"{dir}_grid*_pin_I*"):
            graph.add_node(node_indx, label=f"{dir}_pin_I")
            for node in fn.filter(nodes, f"{dir}_grid*_pin_I*"):
                graph = nx.contracted_nodes(graph,
                                            node_indx, nodes.index(node))
            node_indx += 1

    mapping = {graph.nodes[i]["label"]: i for i in graph.nodes}
    for signal in ["prog_reset", "cfg_done", "prog_clk", "chan*_out*", "*ASSIGNMENT*"]:
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
