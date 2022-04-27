"""
==========================
Partitions Experimentation
==========================

This example aim to demonstrate how to create circuit partition on
post techmapped netlist. Following methods are evaluated.

1. Using pymetis library
2. Generating graph file and executing hmetis externally with system call 

.. image:: ../../../examples/basic/_pymetis_run.svg
    :width: 200px

.. image:: ../../../examples/basic/_external_metis_run.svg
    :width: 200px

"""
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite.json_graph import tree
import pydot
import pymetis
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import (prepare_graph_from_nx, run_metis,
                                    write_metis_graph)

# = = = = = = = = = = = = = = = = = = = = =
#          Create simple graph
# = = = = = = = = = = = = = = = = = = = = =
graph = nx.Graph()

# Create nodes
graph.add_node(0, weight=10)
graph.add_node(1, weight=10)
graph.add_node(2, weight=1)
graph.add_node(3, weight=50)
graph.add_node(4, weight=1)
graph.add_node(5, weight=1)
graph.add_node(6, weight=50)

# Create edges
graph.add_edge(0, 1, weight=1)
graph.add_edge(0, 4, weight=1)
graph.add_edge(2, 1, weight=1)
graph.add_edge(3, 2, weight=1)
graph.add_edge(3, 5, weight=1)
graph.add_edge(0, 5, weight=1)
graph.add_edge(2, 4, weight=1)
graph.add_edge(4, 6, weight=1)
graph.add_edge(1, 5, weight=1)
graph.add_edge(5, 6, weight=1)

# = = = = = = = = = = = = = = = = = = = = =
#         Using pymetis library
# = = = = = = = = = = = = = = = = = = = = =

# Create xadj, adjncy, eweights, vweights
xadj, adjncy, eweights = prepare_graph_from_nx(nx.to_numpy_array(graph))
vweights = nx.get_node_attributes(graph, "weight")
node_names = list(graph.nodes)

print(f"node_names {node_names}")
print(f"xadj {xadj}")
print(f"adjncy {adjncy}")
print(f"eweights {eweights}")
print(f"vweights {vweights}")

n_cuts, membership = pymetis.part_graph(2, eweights=eweights,
                                        vweights=vweights, xadj=xadj,
                                        adjncy=adjncy)
print(f"n_cuts {n_cuts}")

# Convert to pydot to render subgraph
graph_dot = to_pydot(graph)
subgraph = pydot.Cluster('part1', label=''), \
    pydot.Cluster('part2', label='')

for each in subgraph:
    graph_dot.add_subgraph(each)

# Add weights to edge labels
for index, partition in enumerate(membership):
    node = graph_dot.get_node(str(index))[0]
    node.set_color("red" if partition else "green")
    subgraph[partition].add_node(node)
    graph_dot.get_node(str(index))[0].set_label(f"{index} [{vweights[index]}]")

# Add weights to node labels
for edge in graph_dot.get_edge_list():
    edge.set_label(f"{edge.get_weight() or 1}")

graph_dot.write_svg('_pymetis_run.svg')


# = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#   Generating graph file and externally running metis
# = = = = = = = = = = = = = = = = = = = = = = = = = = = =
write_metis_graph(nx.to_numpy_array(graph),
                  eweights=True, vweights=vweights,
                  filename="_partition_experiments_01.csr")
membership = run_metis(
    filename="_partition_experiments_01.csr", cuts=2,
    options="-objtype cut -minconn -niter 100 -ncuts 3 ")

graph_dot2 = to_pydot(graph)
subgraph = pydot.Cluster('part1', label=''), \
    pydot.Cluster('part2', label='')

# Convert to pydot to render subgraph
for each in subgraph:
    graph_dot2.add_subgraph(each)

# Add weights to edge labels
for index, color in enumerate(membership):
    node = graph_dot2.get_node(str(node_names[index]))[0]
    node.set_color("red" if color else "green")
    subgraph[color].add_node(node)
    graph_dot2.get_node(str(index))[0].set_label(
        f"{index} [{vweights[index]}]")

# Add weights to node labels
for edge in graph_dot2.get_edge_list():
    edge.set_label(f"{edge.get_weight() or 1}")

graph_dot2.write_svg('_external_metis_run.svg')
