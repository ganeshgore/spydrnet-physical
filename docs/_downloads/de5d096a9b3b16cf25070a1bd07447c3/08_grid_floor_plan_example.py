"""
=========================
Grid Floorplan Generator
=========================

This example demostrates how the grided floorplan is generated using 
``GridFloorplanGen`` class 


.. image:: ../../../examples/OpenFPGA_basic/_grid_floorplan.svg
   :width: 70%
   :align: center

"""

from spydrnet_physical.util import GridFloorplanGen


def main():
    grid_plan = GridFloorplanGen(8, 8)
    grid_plan.offset_x = 50
    grid_plan.offset_y = 50
    grid_plan.set_column_width(1, 200)
    grid_plan.set_column_width(-1, 200)
    grid_plan.set_row_height(1, 200)
    grid_plan.set_row_height(-1, 200)
    dwg = grid_plan.render_grid()
    print(grid_plan)
    dwg.saveas("_grid_floorplan.svg", pretty=True, indent=4)


if __name__ == "__main__":
    main()
