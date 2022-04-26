"""
============================================
Clock tree insertion Example Architecture 3
============================================

9x12 odd row/column homogeneous fabric design

.. image:: ../../../examples/OpenFPGA_clock_tree/_clock_tree_example_arch_03.svg
    :width: 500px
    :align: center

"""

import spydrnet as sdn
from svgwrite.container import Group
from spydrnet_physical.util import ConnectionPattern, ConnectPoint, ConnectPointList
from copy import deepcopy

# it is a 9x12 clb fabric
# I created only 2 levels one is combine level and the other is level 1
WIDTH = 19
HEIGHT = 25

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Create clock connectivity pattern
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

p_manager = ConnectionPattern(WIDTH, HEIGHT)
combine_pattern = p_manager.connections
combine_pattern.merge(p_manager.get_htree(WIDTH))
combine_pattern.translate(0, 3)
combine_pattern.cursor = (int(WIDTH/2)+1, 0)
combine_pattern.move_y(steps=HEIGHT)


xind = 0
yind = 3
level1_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level1_patt = level1_pmanager.connections
for x in range(int(WIDTH/4)+1, WIDTH, int(WIDTH/2)+1):
    for y in range(int(HEIGHT/4)+2, HEIGHT, int(HEIGHT/2)-2):
        level1_patt.merge(p_manager.get_htree(
            int(WIDTH/2)).translate(xind, yind))
        yind = yind + 10
    yind = 3
    xind = xind + 10

pts = ConnectPointList(3, 3)
pts.cursor = (1, 1)
pts.hold_cursor()
pts.move_x(1).move_x(-1).move_cursor_x()
pts.move_y(steps=2).move_cursor_x(-2)
pts.move_y(steps=2)

# for creating a small 'U' on the level 1 Htree
for x in [3, 7, 13, 17]:
    for y in [6, 10, 16, 20]:
        if y == 6 or y == 16:
            pts2_copy = deepcopy(pts)
            pts2_copy.flip('v')
            level1_patt.merge(pts2_copy.translate(x-1, y+1))
        else:
            pts_copy = deepcopy(pts)
            level1_patt.merge(pts_copy.translate(x-1, y-1))

pts3 = ConnectPointList(2, 4)
pts3.cursor = (1, 1)
pts3.move_y(steps=3, color='black')

# for top CLB and CB connection(extension of the small 'U')
for x in [2, 4, 6, 8, 12, 14, 16, 18]:
    for y in [22]:
        pts3_copy = deepcopy(pts3)
        level1_patt.merge(pts3_copy.translate(x-1, y-1))

# for bottom CLB and CB connection(extension of the small 'U')
for x in [2, 4, 6, 8, 12, 14, 16, 18]:
    for y in [4]:
        pts4_copy = deepcopy(pts3)
        pts4_copy.flip('v')
        level1_patt.merge(pts4_copy.translate(x-1, y+1))

# For connections to the left CBs
for y in range(2, HEIGHT, 2):
    level1_patt.cursor = (2, y)
    level1_patt.move_x(-1)
# For connections to the right CBs
for y in range(2, HEIGHT, 2):
    level1_patt.cursor = (18, y)
    level1_patt.move_x(1)

# for a single connection on the left side, in the middle of the level 1 htree (on all 4 trees)
for x in [3, 13]:
    for y in [8, 18]:
        level1_patt.cursor = (x, y)
        level1_patt.move_x(-1)
# for a single connection on the right side, in the middle of the level 1 htree (on all 4 trees)
for x in [7, 17]:
    for y in [8, 18]:
        level1_patt.cursor = (x, y)
        level1_patt.move_x(1)

# For pushing up and down connections through levels
for x in range(2):
    for y in range(2):
        ydir = -1 if y else 1
        pt = ConnectPoint(5+(x*(int(WIDTH/2)+1)), 8+(y*(int(WIDTH/2)+1)) +
                          ydir, 5+(x*(int(WIDTH/2)+1)), 8+(y*(int(WIDTH/2)+1)))
        combine_pattern.points.append(deepcopy(pt))
        combine_pattern.push_connection_down(combine_pattern.points[-1])
        level1_patt.points.append(deepcopy(pt))
        level1_patt.pull_connection_up(level1_patt.points[-1])

# for x in range(5, WIDTH, 10):
#    for y in range (8, HEIGHT, 10):
#        pt = combine_pattern.search_to_point((x,y))
#        if pt:
#            combine_pattern.push_connection_down(pt)
#            level1_patt.points.append(deepcopy(pt))
#            level1_patt.pull_connection_up(level1_patt.points[-1])

combine_pattern.set_color('red')
level1_patt.set_color('blue')

combine_pattern.merge(level1_patt)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
svg = p_manager.render_pattern(title="-")
skip_points = [(1, 1), (1, HEIGHT), (WIDTH, 1), (WIDTH, HEIGHT)]
sink_pts = p_manager.svg_main.add(Group(id="sink_pts"))
for y in list(range(2, HEIGHT, 2))+[1, HEIGHT]:
    for x in list(range(2, WIDTH, 2))+[1, WIDTH]:
        if not (x, y) in skip_points:
            sink_pts.add(svg.rect(insert=(x*20-10, y*20-10),
                                  size=(20, 20), opacity=0.2,
                                  class_="sink_point"))
svg.saveas("_clock_tree_example_arch_03.svg", pretty=True, indent=4)
