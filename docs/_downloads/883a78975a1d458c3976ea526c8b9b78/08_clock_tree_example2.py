"""
============================================
Clock tree insertion Example Architecture 2
============================================

16x24 rectangular homogeneous fabric design

.. image:: ../../../../examples/OpenFPGA/clock_tree/_clock_tree_example_arch_02.svg
    :width: 220px

"""
import spydrnet as sdn
from svgwrite.container import Group
from spydrnet_physical.util import ConnectionPattern


WIDTH = 49
HEIGHT = 33
p_manager = ConnectionPattern(WIDTH, HEIGHT)
combine_pattern = p_manager.connections
combine_pattern.cursor = (int(WIDTH/2), 0)
combine_pattern.move_y()
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
svg.saveas("_clock_tree_example_arch_02.svg", pretty=True, indent=4)
