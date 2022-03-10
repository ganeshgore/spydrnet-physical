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

.. image:: ../../../../examples/OpenFPGA/clock_tree/_htree_pattern.svg
    :width: 500px
    :align: center

"""

from spydrnet_physical.util import ConnectionPattern

WIDTH = 7
HEIGHT = 7
p_manager = ConnectionPattern(WIDTH, HEIGHT)
htree_pattern = p_manager.connections
htree_pattern.merge(p_manager.get_htree(WIDTH))
htree_pattern.merge(p_manager.get_htree(int(WIDTH/2)).translate(0, 0))
htree_pattern.merge(p_manager.get_htree(int(WIDTH/2)).translate(4, 0))
htree_pattern.merge(p_manager.get_htree(int(WIDTH/2)).translate(4, 4))
htree_pattern.merge(p_manager.get_htree(int(WIDTH/2)).translate(0, 4))
svg = p_manager.render_pattern(title="HTree Pattern")
svg.saveas("_htree_pattern.svg", pretty=True, indent=4)
