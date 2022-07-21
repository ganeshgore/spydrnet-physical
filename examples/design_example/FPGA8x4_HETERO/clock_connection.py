import logging
import pickle
import os
from glob import glob
from os.path import basename, dirname, realpath

import spydrnet as sdn
from svgwrite.container import Group
from spydrnet_physical.util import ConnectionPattern, ConnectPointList
from copy import deepcopy

logger = logging.getLogger("spydrnet_logs")

PROJ_NAME = basename(dirname(realpath(__file__)))

svg_dir = "/home/users/saad.khalil/Documents/RS/spydrnet-physical/examples/design_example/FPGA8x4_HETERO"

fpga = pickle.load(open(f"/home/users/saad.khalil/Documents/RS/spydrnet-physical/examples/design_example/{PROJ_NAME}/{PROJ_NAME}_fpgagridgen.pickle", "rb"))

def save_svg_with_background(svg, filename, add_marker=False):
    with open(f"/home/users/saad.khalil/Documents/RS/spydrnet-physical/examples/design_example/{PROJ_NAME}/{PROJ_NAME}_fpgagridgen.pickle", 'rb') as fp:
        dwg = pickle.load(fp)
    scalex, scaley = 4.6, 4.6
    # Add main group
    main_group = {ele["id"]: ele for ele in svg.elements
                  if isinstance(ele, Group)}["main"]
    main_group["transform"] = f"scale({scalex},-{scaley})"
    dwg.add(main_group)
    # Add marker
    if add_marker:
        markers = {ele["id"]: ele for ele in svg.elements
                   if isinstance(ele, Group)}["markers"]
        markers["transform"] = f"scale({scalex},-{scaley})"
        dwg.add(markers)
    dwg.elements.extend(svg.defs.elements)
    dwg.saveas(svg_dir+filename, pretty=True, indent=4)


WIDTH = (fpga.get_width()*2)+2
HEIGHT = (fpga.get_height()*2)+3
WIDTH_F = (fpga.get_width()*2)+2
HEIGHT_F = (fpga.get_height()*2)+3

level0_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level0_patt = level0_pmanager.connections
level1_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level1_patt = level1_pmanager.connections
level2_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level2_patt = level2_pmanager.connections
level3_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level3_patt = level3_pmanager.connections

p_manager = ConnectionPattern(WIDTH, HEIGHT)
hyb_pat = p_manager.connections

level0_patt.cursor = (WIDTH/2, 0)
level0_patt.move_y(steps=int(HEIGHT/2)+1)
level0_patt.merge(p_manager.get_htree(WIDTH, root=2, side=-8).translate(0,-(fpga.get_height()-1)))
level0_patt.set_color('green')
#level0_patt.pull_connection_up(level3_patt.points[0])


for x in [int(WIDTH/4)-1, WIDTH-16]:
    for y in [10, HEIGHT-10]:
        if y == HEIGHT-10 and x == int(WIDTH/4)-1:
            level1_patt.merge(p_manager.get_htree(int(WIDTH/2), side = -4).translate(x-17,y-16))
        if y == 10 and x == int(WIDTH/4)-1:
            level1_patt.merge(p_manager.get_htree(int(WIDTH/2), side = -4).translate(x-17,y-17))
        if y == HEIGHT-10 and x == WIDTH-16:
            level1_patt.merge(p_manager.get_htree(int(WIDTH/2), side = -4).translate(x-16,y-16))
        if y == 10 and x == WIDTH-16:
            level1_patt.merge(p_manager.get_htree(int(WIDTH/2), side = -4).translate(x-16,y-17))

for x in [7, 23, 43, 59]:
    for y in [6, 14, 22, 30]:
            level2_patt.merge(level2_pmanager.get_htree(int(WIDTH/4), side= -2).translate(x-8,y-8))

for x in [3, 11, 19, 27, 39, 47, 55, 63]:
    for y in range(4, HEIGHT, 4):
        level3_patt.merge(level3_pmanager.get_htree(int(WIDTH/12)).translate(x-3, y-3))

#level3_patt.merge(level3_pmanager.get_htree(int(WIDTH/12)).translate(39-3, 4-3))
#
#range(3, int(WIDTH/2), 8):


hyb_pat.merge (level0_patt)
hyb_pat.merge (level1_patt)
hyb_pat.merge (level2_patt)
hyb_pat.merge (level3_patt)


svg = p_manager.render_pattern(title="-")
skip_points = [(1, 1), (1, HEIGHT), (WIDTH, 1), (WIDTH, HEIGHT)]
sink_pts = p_manager.svg_main.add(Group(id="sink_pts"))
for y in list(range(3, HEIGHT, 2))+[1, HEIGHT]:
    for x in list(range(2, WIDTH, 2))+[1, WIDTH]:
        if not (x, y) in skip_points:
            sink_pts.add(svg.rect(insert=(x*20-10, y*20-10),
                                  size=(20, 20), opacity=0.2,
                                  class_="sink_point"))

#graph = to_pydot(p_manager.connections.create_graph())
#graph.write_svg(svg_dir+"clk0_pattern_graph.svg")
save_svg_with_background(svg, "FPGA32x16_HETRO_Clock_Tree_bg.svg")

svg.saveas("FPGA32x16_HETRO_Clock_Tree.svg", pretty=True, indent=4)





