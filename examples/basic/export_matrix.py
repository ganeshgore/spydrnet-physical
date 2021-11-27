"""
=========================
Grouping ungrouping cells
=========================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

.. hdl-diagram:: ../../../examples/basic/_initial_design.v
   :type: netlistsvg
   :align: center
   :module: top

.. image:: ../../../examples/basic/_graph.svg
    :height: 200px
    :align: center

"""

import logging
import os
import pymetis
import pydot

import matplotlib.pyplot as plt
import networkx as nx
import spydrnet as sdn
import spydrnet_physical as sdnphy
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_pydot import to_pydot

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')
sdn.compose(netlist, '_initial_design.v', skip_constraints=True)

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')


# Create nodes
G = nx.Graph()
top = netlist.top_instance.reference
instance_node_map = [top.name]
G.add_node(0, label=top.name)
for instance in top.children:
    G.add_node(len(instance_node_map), label=instance.name)
    instance_node_map.append(instance.name)


def get_node_name(pin):
    if isinstance(pin, sdn.OuterPin):
        return pin.instance.name
    else:
        return pin.port.definition.name


edges = []
for cable in top.get_cables():
    for wire in cable.wires:
        driver_inst = get_node_name(wire.get_driver()[0])
        for p in wire.pins:
            node = get_node_name(p)
            if node == driver_inst:
                continue
            edges.append(tuple(sorted([
                instance_node_map.index(driver_inst),
                instance_node_map.index(node)])))

for edge in set(edges):
    weight = edges.count(edge)
    G.add_edge(*edge, label=f"[{weight}]")


graph = to_pydot(G)
n_cuts, membership = pymetis.part_graph(2, adjacency=nx.to_numpy_array(G))

subgraph = pydot.Cluster('part1', label=''), \
    pydot.Cluster('part2', label='')

for each in subgraph:
    graph.add_subgraph(each)

for index, color in enumerate(membership):
    node = graph.get_node(str(index))[0]
    node.set_color("red" if color else "green")
    subgraph[color].add_node(node)


graph.write_dot('_graph.dot')
graph.write_png('_graph.png')
graph.write_svg('_graph.svg')
