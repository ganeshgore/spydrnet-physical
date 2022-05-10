"""
============================================
Clock tree insertion Example Architecture 1
============================================

16x16 Square homogeneous fabric design

.. image:: ../../../examples/OpenFPGA_clock_tree/_clock_tree_example_arch_01.svg
    :width: 500px
    :align: center

"""
#from turtle import color
#from turtle import color
#from ast import pattern
#from platform import release

import spydrnet as sdn
from svgwrite.container import Group
from spydrnet_physical.util import ConnectionPattern
from copy import deepcopy


WIDTH = 33
HEIGHT = 33
WIDTH_F = 33

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

level3_patt.cursor = (int(WIDTH/2)+1, 0)
level3_patt.move_y(steps=int(WIDTH/2)+1)
level3_patt.merge(p_manager.get_htree(WIDTH))
level3_patt.set_color('red')
#combine_pattern.translate(1, 1)

#combine_pattern.rotate (90)
level3_patt.pull_connection_up(level3_patt.points[0])
while WIDTH_F > 7:
    tree_manager = ConnectionPattern(WIDTH, HEIGHT)
    tree_patt = tree_manager.connections
    for x in range(int(WIDTH_F/4)+1, WIDTH, int(WIDTH_F/2)):  # (5, 33, 9)
        for y in range(int(WIDTH_F/4)+1, WIDTH, int(WIDTH_F/2)):
            tree_patt.merge(p_manager.get_htree(int(WIDTH_F/2)).
                            translate(x-int(WIDTH_F/4), y-int(WIDTH_F/4)))
    if WIDTH_F == 33:
        tree_patt.set_color('black')
        level2_patt.merge(tree_patt)
    elif WIDTH_F == 17:
        tree_patt.set_color('blue')
        level1_patt.merge(tree_patt)
    else:
        tree_patt.set_color('green')
        level0_patt.merge(tree_patt)
    WIDTH_F = int(WIDTH_F/2)+1  # 17, 9, 5


for y in range(2, WIDTH, 30):
    if y == 2:
        level0_patt.cursor = (2, y)
        level0_patt.hold_cursor()
        level0_patt.move_x(-1, color='orange').move_y(-1, color='orange')
    elif y == 32:
        level0_patt.release_cursor()
        level0_patt.cursor = (32, y)
        level0_patt.hold_cursor()
        level0_patt.move_x(1, color='orange').move_y(1, color='orange')

for x in range(2, WIDTH, 30):
    if x == 2:
        level0_patt.cursor = (x, 32)
        level0_patt.hold_cursor()
        level0_patt.move_x(-1, color='orange').move_y(1, color='orange')
    elif x == 32:
        level0_patt.release_cursor()
        level0_patt.cursor = (x, 2)
        level0_patt.hold_cursor()
        level0_patt.move_x(1, color='orange').move_y(-1, color='orange')

for x in range(4, WIDTH-2, 2):
    level0_patt.cursor = (x, 2)
    level0_patt.move_y(-1, color='orange')

for y in range(4, WIDTH-2, 2):
    level0_patt.cursor = (2, y)
    level0_patt.move_x(-1, color='orange')

for x in range(4, WIDTH-2, 2):
    level0_patt.cursor = (x, 32)
    level0_patt.move_y(1, color='orange')

for y in range(4, WIDTH-2, 2):
    level0_patt.cursor = (32, y)
    level0_patt.move_x(1, color='orange')

for x in range(3, WIDTH, 4):
    for y in range(3, HEIGHT, 4):
        pt = level1_patt.search_to_point((x, y))
        if pt:
            level1_patt.push_connection_down(pt)
            level0_patt.points.append(deepcopy(pt))
            level0_patt.pull_connection_up(level0_patt.points[-1])

for x in range(5, WIDTH, 8):
    for y in range(5, HEIGHT, 8):
        pt = level2_patt.search_to_point((x, y))
        if pt:
            level2_patt.push_connection_down(pt)
            level1_patt.points.append(deepcopy(pt))
            level1_patt.pull_connection_up(level1_patt.points[-1])

for x in range(9, WIDTH, 16):
    for y in range(9, HEIGHT, 16):
        pt = level3_patt.search_to_point((x, y))
        if pt:
            level3_patt.push_connection_down(pt)
            level2_patt.points.append(deepcopy(pt))
            level2_patt.pull_connection_up(level2_patt.points[-1])


#level3_patt.crop_edges()
#level2_patt.crop_edges()
#level1_patt.crop_edges()
#level0_patt.crop_edges()
#
#level3_patt.trim_borders()
#level2_patt.trim_borders()
#level1_patt.trim_borders()
#level0_patt.trim_borders()

hyb_pat.merge(level0_patt)
hyb_pat.merge(level1_patt)
hyb_pat.merge(level2_patt)
hyb_pat.merge(level3_patt)

# combine_pattern.merge(lev2_patt)


# combine_pattern.set_color('black')
# lev2_patt.set_color('red')
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Create clock connectivity pattern
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
svg = p_manager.render_pattern(title=f"{WIDTH}x{HEIGHT} design")
skip_points = [(1, 1), (1, HEIGHT), (WIDTH, 1), (WIDTH, HEIGHT)]
sink_pts = p_manager.svg_main.add(Group(id="sink_pts"))
for y in list(range(2, HEIGHT, 2))+[1, HEIGHT]:
    for x in list(range(2, WIDTH, 2))+[1, WIDTH]:
        if not (x, y) in skip_points:
            sink_pts.add(svg.rect(insert=(x*20-10, y*20-10),
                                  size=(20, 20), opacity=0.2,
                                  class_="sink_point"))
svg.saveas("_clock_tree_example_arch_01.svg", pretty=True, indent=4)
