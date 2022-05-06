"""
==============================
Netlist to graph (networkx)
==============================

This example demonstrate how to convert a netlist to a netowrkx graph.

By default each node is assigned weight 1 and each edge is assigned weight 
based on how many wires it represents. In case of bus connected single edge
with weight equal to length of bus is assigned.

**Graph representation**

.. image:: ../../../examples/OpenFPGA_tiling/_nx_graph.svg
    :align: center
    :width: 40% 
"""

import matplotlib.pyplot as plt
import networkx as nx
import spydrnet as sdn
import spydrnet_physical as sdnphy
from networkx.drawing.nx_pydot import to_pydot

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top: sdn.Netlist = netlist.top_instance.reference
graph = top.get_connectivity_network()
nodes = graph.nodes
graph_dot = to_pydot(graph)
graph_dot.write_svg('_nx_graph.svg')

print(" ========== Nodes ==========")
print("\n".join([f"{node:2} {nodes[node]['label']:15} {nodes[node]}"
                 for node in nodes]))
print(" ========== Edges ==========")
print("\n".join(nx.generate_edgelist(graph, data=True)))

# %%
# **Regenerated graph with ports splits into individual nodes**
#
# .. image:: ../../../examples/OpenFPGA_tiling/_nx_graph_split.svg
#     :align: center
#     :width: 50%

graph = top.get_connectivity_network(split_ports=True)
nodes = graph.nodes
graph_dot = to_pydot(graph)
graph_dot.write_svg('_nx_graph_split.svg')

print(" ========== Nodes ==========")
print("\n".join([f"{node:2} {nodes[node]['label']:15} {nodes[node]}"
                 for node in nodes]))
print(" ========== Edges ==========")
print("\n".join(nx.generate_edgelist(graph, data=True)))
