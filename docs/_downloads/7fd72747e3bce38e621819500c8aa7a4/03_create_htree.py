"""
==================================
Create Hybrid Connectivity Pattern
==================================

This example demostrate how to create hybrid connetivity pattern for any 
arbitrary (non square ) tiles.


**Output**

.. image:: ../../../../examples/OpenFPGA/clock_tree/_hybrid_connectivity_pattern.svg
    :width: 500px
    :align: center

"""

from spydrnet_physical.util import ConnectionPattern

WIDTH = 19
HEIGHT = 13
cpat = ConnectionPattern(WIDTH, HEIGHT)
hyb_pat = cpat.connections
hyb_pat.cursor = (int(WIDTH/2)+1, 0)
hyb_pat.move_y(steps=int(HEIGHT/2)+1)
hyb_pat.merge(
    cpat.get_htree(HEIGHT, root=1, side=3, repeat=2).translate((WIDTH-HEIGHT)/2, 0))
hyb_pat.merge(cpat.get_htree(int(HEIGHT/2), side=1, repeat=3).translate(3, 0))
hyb_pat.merge(cpat.get_htree(int(HEIGHT/2), side=1, repeat=3).translate(3, 8))
hyb_pat.merge(cpat.get_htree(int(HEIGHT/2), side=1, repeat=3).translate(11, 0))
hyb_pat.merge(cpat.get_htree(int(HEIGHT/2), side=1, repeat=3).translate(11, 8))

for y in range(1, HEIGHT+1):
    hyb_pat.add_connection(2, y, 1, y)
    hyb_pat.add_connection(WIDTH-1, y, WIDTH, y)

for x in range(3, WIDTH-1):
    hyb_pat.add_connection(x, ((HEIGHT-1)/2)+1, x, ((HEIGHT-1)/2)+2)
    if not x == (int(WIDTH/2)+1):
        hyb_pat.add_connection(x, ((HEIGHT-1)/2)+1, x, ((HEIGHT-1)/2))
    else:
        hyb_pat.cursor = (int(WIDTH/2)+1, int(HEIGHT/2)+2)
        hyb_pat.move_y(steps=int(HEIGHT/2)-1)

svg = cpat.render_pattern(title="Hybrid Pattern")
svg.saveas("_hybrid_connectivity_pattern.svg", pretty=True, indent=4)
