"""
==================================
Create H-Tree Connectivity pattern
==================================

This example demonstrate how to genrate different connection pattern
for routing global signals. By default this library support basic fishbone
and HTree patterns, which can be extended to create desired connectivity
usng transformations like ``rotate``, ``transalate``, ``margin``, ``merge``,
``scale`` and ``sample``


**Output**

.. image:: ../../../examples/OpenFPGA_clock_tree/_htree_pattern.svg
    :width: 500px
    :align: center

"""

from spydrnet_physical.util import ConnectionPattern

WIDTH = 33
WIDTH_F = 33
HEIGHT = 33
p_manager = ConnectionPattern(WIDTH, HEIGHT)
htree_pattern = p_manager.connections
htree_pattern.cursor = (int(WIDTH/2)+1, 0)
htree_pattern.move_y(steps=int(WIDTH/2)+1)
htree_pattern.merge(p_manager.get_htree(WIDTH))

while WIDTH > 6:
    for x in range(int(WIDTH/4)+1, WIDTH_F, int(WIDTH/2)):
        for y in range(int(WIDTH/4)+1, WIDTH_F, int(WIDTH/2)):
            htree_pattern.merge(p_manager.get_htree(
                int(WIDTH/2)).translate(x-int(WIDTH/4), y-int(WIDTH/4)))
    WIDTH = int(WIDTH/2)+1

svg = p_manager.render_pattern(title="HTree Pattern")

# Highlight the clock sink point
for y in range(2, WIDTH_F, 2):
    for x in range(2, WIDTH_F, 2):
        p_manager.svg_main.add(svg.rect(
            color="red", opacity="0.1",
            insert=(x*20 - 10, y*20 - 10),
            size=(20, 20)))
svg.saveas("_htree_pattern.svg", pretty=True, indent=4)
