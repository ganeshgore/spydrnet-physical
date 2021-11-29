"""
=================
Partitions Study
=================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.


.. image:: ../../../examples/basic/_partition_experiments.svg
    :height: 200px
    :align: center

"""
import networkx as nx
import pydot
import pymetis
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import prepare_graph_from_nx

graph = nx.Graph()

# Create nodes
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

# Create edges
graph.add_edge(0, 2, weight=1)
graph.add_edge(0, 1, weight=4)
graph.add_edge(2, 1, weight=1)
graph.add_edge(3, 2, weight=6)
graph.add_edge(4, 0, weight=1)
graph.add_edge(4, 3)

xadj, adjncy, eweights = prepare_graph_from_nx(nx.to_numpy_array(graph))
vweights = [1, 1, 1, 1, 1]

n_cuts, membership = pymetis.part_graph(
    2, eweights=eweights,
    vweights=vweights,
    xadj=[0, 3, 5, 8, 10, 12],
    adjncy=[2, 3, 5, 1, 3, 1, 2, 4, 3, 5, 1, 4])
print(f"n_cuts {n_cuts}")

# Convert to pydot to render subgraph
graph = to_pydot(graph)
subgraph = pydot.Cluster('part1', label=''), \
    pydot.Cluster('part2', label='')

for each in subgraph:
    graph.add_subgraph(each)

for index, color in enumerate(membership):
    node = graph.get_node(str(index))[0]
    node.set_color("red" if color else "green")
    subgraph[color].add_node(node)
    graph.get_node(str(index))[0].set_label(f"{index} [{vweights[index]}]")

for edge in graph.get_edge_list():
    edge.set_label(f"{edge.get_weight() or 1}")

graph.write_png('_partition_experiments.png')
graph.write_dot('_partition_experiments.dot')
graph.write_svg('_partition_experiments.svg')
