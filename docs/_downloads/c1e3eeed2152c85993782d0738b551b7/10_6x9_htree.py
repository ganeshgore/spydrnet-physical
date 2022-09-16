"""
=========================
Grouping ungrouping cells
=========================

This example is for creating Htree for 6x9 fabric. Our main constraints for clocktrees are to connect all the CLBs to the lowest level of Htree to have same clock delays to each cell.

.. image:: ../examples/OpenFPGA_clock_tree/_hybrid_connectivity_pattern_graph.svg
    :align: center


**Output1** ungrouped module


.. image:: ../../../examples/OpenFPGA_clock_tree/_6x9_clock_tree.svg
    :align: center

"""






from spydrnet_physical.util import ConnectionPattern, ConnectPointList, ConnectPoint
from svgwrite.container import Group
from copy import deepcopy
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import to_pydot

#Setting the size of clock tree
FPGA_WIDTH = 6
GRID_WIDTH = (FPGA_WIDTH *2)+3
FPGA_HEIGHT = 9
GRID_HEIGHT = (FPGA_HEIGHT* 2)+3

#creating bigger Htree
p_manager = ConnectionPattern(GRID_WIDTH, GRID_HEIGHT)
level0_patt = p_manager.connections
level0_patt.merge(p_manager.get_htree(GRID_WIDTH,2,-1,1))
level0_patt.translate(3,0)
level0_patt.cursor = (int(GRID_HEIGHT/2)+1, 0)
level0_patt.move_y(steps=int(GRID_WIDTH/2)+1)
level0_patt.rotate(90)
level0_patt.set_color('blue')

##creating level 1 Htrees
level1_pmanager = ConnectionPattern(GRID_WIDTH, GRID_HEIGHT)
level1_patt = level1_pmanager.connections
for x in range (0, GRID_WIDTH, 12):
    for y in range (0, FPGA_HEIGHT, 6):
        level1_patt.merge(p_manager.get_htree(int(GRID_HEIGHT/2)).translate(x,y-5).rotate(90))
        level1_patt.set_color('red')


#creating level 2 Htress

# for small Htrees
level2_pmanager = ConnectionPattern(GRID_WIDTH, GRID_HEIGHT)
level2_patt = level2_pmanager.connections
for x in range (0, GRID_WIDTH+4, 4):
    for y in range (0, GRID_WIDTH, 10):
        if (x!= 8):
            level2_patt.merge(p_manager.get_htree(int(GRID_HEIGHT/4)).translate(x,y-10).rotate(90))

##for vertical u-shaped structures on left
for x in range (5, int(GRID_WIDTH/2)+1, 9):
    for y in range (0, GRID_HEIGHT-1, 4):
        if (y!=8):
            level2_patt.merge(p_manager.get_htree(int(GRID_HEIGHT/4)).translate(x,y))

        

for y in range(2, GRID_HEIGHT, 2):
    if (y!=10) & (y!=12):
        level2_patt.cursor = (7,y)
        level2_patt.move_x(-1)

    

for y in range(2, GRID_HEIGHT, 2):
    if (y!=10) & (y!=12):
        level2_patt.cursor = (9,y)
        level2_patt.move_x(1) 

       



remove_points = []
for y in range(-1, GRID_HEIGHT-1, 4):
    remove_points.append((8, y))
    for point in remove_points:
        point = level2_patt.search_from_point(point)
        if point:
            level2_patt._points.remove(point)






    
for x in range (2, GRID_WIDTH, 2):
    if (x != 8):
        level2_patt.cursor = (x,14)
        level2_patt.move_y(-2)
        level2_patt.cursor = (x,8)
        level2_patt.move_y(2)

#for connecting middle vertical points
for x in range (2, GRID_HEIGHT, 18):
    level2_patt.cursor = (7,x)
    level2_patt.move_x(1)

for x in range (4, GRID_HEIGHT-1, 14):
    level2_patt.cursor = (9,x)
    level2_patt.move_x(-1)

#for io connections



for y in range (2, GRID_HEIGHT, 2):
    level2_patt.cursor = (2,y)
    level2_patt.move_x(-1)
    level2_patt.cursor = (GRID_WIDTH-1,y)
    level2_patt.move_x(1)


for x in range (2, GRID_WIDTH, 2):
    level2_patt.cursor = (x,2)
    level2_patt.move_y(-1)
    level2_patt.cursor = (x,GRID_HEIGHT-1)
    level2_patt.move_y(1)
level2_patt.set_color('green')
#
##merging the levels
level1_patt.merge(level2_patt)
level0_patt.merge(level1_patt)


graph = level0_patt.create_graph()

# TODO Annotate graph with wire length  from source


def leaf_node_weight(x, y):
    return 4


for node_lbl in graph.nodes:
    if graph.out_degree(node_lbl) == 0:
        _, x, y, _ = node_lbl.split("_")
        node = graph.nodes[node_lbl]
        node["weight"] = leaf_node_weight(x, y)
        node["color"] = "red"
        node["label"] = f"{node_lbl}_{leaf_node_weight(x, y)}"


def get_leaf_sum(graph, node):
    total_weight = 0
    for node_lbl in nx.dfs_preorder_nodes(graph, node):
        if node_lbl == node:
            continue
        node = graph.nodes[node_lbl]
        if "weight" in node:
            total_weight += int(node["weight"])
    return total_weight


for node_lbl in nx.dfs_preorder_nodes(graph):
    if graph.out_degree(node_lbl) > 1:
        node = graph.nodes[node_lbl]
        node["label"] = f"{node_lbl}_[{get_leaf_sum(graph, node_lbl)}]"


graph = to_pydot(graph)
graph.write_dot("_hybrid_connectivity_pattern_graph.dot")
graph.write_svg("_hybrid_connectivity_pattern_graph.svg")
graph.write_png("_hybrid_connectivity_pattern_graph.png")


svg = p_manager.render_pattern(title="6X9 CT")
skip_points = [(1, 1), (1, GRID_HEIGHT), (GRID_WIDTH, 1), (GRID_WIDTH, GRID_HEIGHT)]
sink_pts = p_manager.svg_main.add(Group(id="sink_pts"))
for y in list(range(2, GRID_HEIGHT, 2))+[1, GRID_HEIGHT]:
    for x in list(range(2, GRID_WIDTH, 2))+[1, GRID_WIDTH]:
        if not (x, y) in skip_points:
            sink_pts.add(svg.rect(insert=(x*20-10, y*20-10),
                                  size=(20, 20), opacity=0.2,
                                  class_="sink_point"))
svg.saveas("_6x9_clock_tree.svg", pretty=True, indent=4)