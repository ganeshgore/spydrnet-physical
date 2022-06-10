"""
============================================
Clock tree insertion Example Architecture 2
============================================

16x24 rectangular homogeneous fabric design

.. image:: ../../../examples/OpenFPGA_clock_tree/_clock_tree_example_arch_02.svg
    :width: 500px
    :align: center

"""
import spydrnet as sdn
from svgwrite.container import Group
from spydrnet_physical.util import ConnectionPattern, ConnectPointList
from copy import deepcopy

WIDTH = 49
HEIGHT = 33
level0_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level0_patt = level0_pmanager.connections
level1_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level1_patt = level1_pmanager.connections
level2_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level2_patt = level2_pmanager.connections
level3_pmanager = ConnectionPattern(WIDTH, HEIGHT)
level3_patt = level3_pmanager.connections
level3_patt.cursor = (int(WIDTH/2)+1, 0)
level3_patt.move_y(steps=int(HEIGHT/2)+1)
level3_patt.merge(level3_pmanager.get_htree(WIDTH).translate(0, -8))
level3_patt.set_color('red')
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Create clock connectivity pattern
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
for x in range(int(WIDTH/4)+1, WIDTH, int(WIDTH/2)):  # W
    for y in range(int(HEIGHT/6), HEIGHT, int(HEIGHT/2)+8):
        level2_patt.merge(level3_pmanager.get_htree(int(WIDTH/2)).
                          translate(x-int(WIDTH/4), y-int(WIDTH/4)))
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

for x in range(int(WIDTH/8)+1, WIDTH, int(WIDTH/4)):  # W
    for y in range(int(HEIGHT/3), HEIGHT, int(HEIGHT/3)+1):
        level1_patt.merge(level3_pmanager.get_htree(int(WIDTH/4)).
                          translate(x-int(WIDTH/8), y-int(WIDTH/8)))
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
for x in range(int(WIDTH/10), WIDTH, int(WIDTH/8)):  # W
    for y in range(int(HEIGHT/4), HEIGHT-4, int(HEIGHT/6)+1):
        level0_patt.merge(level3_pmanager.get_htree(int(WIDTH/6)).
                          translate(x-int(WIDTH/10), y-int(WIDTH/10)))
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

pts = ConnectPointList(5, 5)
pts.cursor = (3, 0)
pts.move_y(steps=2)
pts.hold_cursor()
pts.move_x(2).move_x(-2).move_y(3).move_cursor_x(2)
pts.move_y(steps=3)
pts.move_cursor_x(-4)
pts.move_y(steps=3)
pts.release_cursor()

for x in range(1, WIDTH, 6):
    for y in [28]:
        pts_cp = deepcopy(pts)
        level0_patt.merge(pts_cp.translate(x, y))

for x in range(1, WIDTH, 6):
    for y in [6]:
        pts_cp = deepcopy(pts)
        pts_cp.flip('v')
        level0_patt.merge(pts_cp.translate(x, y))

# For connections to the left CBs
for y in range(2, HEIGHT, 2):
    level0_patt.cursor = (2, y)
    level0_patt.move_x(-1)

# For connections to the right CBs
for y in range(2, HEIGHT, 2):
    level0_patt.cursor = (48, y)
    level0_patt.move_x(1)


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

pts2 = ConnectPointList(1, 3)
pts2.cursor = (3, 0)
pts2.move_y(steps=2)


for x in range(1, WIDTH, 6):
    for y in [14, 26]:
        pts2_cp = deepcopy(pts2)
        level0_patt.merge(pts2_cp.translate(x, y))

for x in range(1, WIDTH, 6):
    for y in [8, 20]:
        pts2_cp = deepcopy(pts2)
        pts2_cp.flip('v')
        level0_patt.merge(pts2_cp.translate(x, y))
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

for x in [10, 16, 34, 40]:
    for y in [5, 29]:
        level0_patt.short_through((x, y))
# = = = = = = = = Pull up and Push down connections= = = = = = = = = = = =

for x in range(13, WIDTH, 24):
    for y in range(5, HEIGHT, 24):
        pt = level3_patt.search_to_point((x, y))
        if pt:
            level3_patt.push_connection_down(pt)
            level2_patt.points.append(deepcopy(pt))
            level2_patt.pull_connection_up(level2_patt.points[-1])

for x in range(7, WIDTH, 12):
    for y in range(11, HEIGHT, 12):
        pt = level2_patt.search_to_point((x, y))
        if pt:
            level2_patt.push_connection_down(pt)
            level1_patt.points.append(deepcopy(pt))
            level1_patt.pull_connection_up(level1_patt.points[-1])

for x in range(4, WIDTH, 6):
    for y in range(8, HEIGHT-2, 6):
        pt = level1_patt.search_to_point((x, y))
        if pt:
            level1_patt.push_connection_down(pt)
            level0_patt.points.append(deepcopy(pt))
            level0_patt.pull_connection_up(level0_patt.points[-1])

level0_patt.set_color('brown')
level1_patt.set_color('blue')
level2_patt.set_color('black')

level3_patt.merge(level0_patt)
level3_patt.merge(level1_patt)
level3_patt.merge(level2_patt)

level3_patt.crop_edges()
level3_patt.trim_borders()

svg = level3_pmanager.render_pattern(title="-")
skip_points = [(1, 1), (1, HEIGHT), (WIDTH, 1), (WIDTH, HEIGHT)]
sink_pts = level3_pmanager.svg_main.add(Group(id="sink_pts"))
for y in list(range(2, HEIGHT, 2))+[1, HEIGHT]:
    for x in list(range(2, WIDTH, 2))+[1, WIDTH]:
        if not (x, y) in skip_points:
            sink_pts.add(svg.rect(insert=(x*20-10, y*20-10),
                                  size=(20, 20), opacity=0.2,
                                  class_="sink_point"))
svg.saveas("_clock_tree_example_arch_02.svg", pretty=True, indent=4)
