'''
============================
Create Clock Tree Embedding
============================

**Original grided netlist**

.. hdl-diagram:: ../../../examples/OpenFPGA_clock_tree/_square_grid_design.v
   :type: netlistsvg
   :align: center
   :module: top

**Connection pattern**

.. image:: ../../../examples/OpenFPGA_clock_tree/_fishbone_pattern_0.svg
    :width: 300px
    :align: center

**Schematic after embedding clock tree**

.. hdl-diagram:: ../../../examples/OpenFPGA_clock_tree/_post_clock_embedding.v
   :type: netlistsvg
   :align: center
   :module: top


**Floorplan after embedding clock tree**

.. image:: ../../../examples/OpenFPGA_clock_tree/_clock_tree_floorplan.svg
    :width: 500px
    :align: center


'''

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import ConnectionPattern

print("WIP")

# # Verilog netlist
# netlist = sdnphy.load_netlist_by_name('square_grid')
# top_definition = netlist.top_instance.reference
# top_definition.split_port("in")
# top_definition.split_port("out")
# top_definition.create_unconn_wires()


# netlist = sdnphy.load_netlist_by_name('square_grid')
# top_definition = netlist.top_instance.reference

# # Pattern
# p_manager = ConnectionPattern(4, 4)
# fishbone_pattern = p_manager.get_fishbone()
# fishbone_pattern.points[4].buffer = True

# svg = p_manager.render_pattern(title="Merging option")
# svg.saveas("_buffered_clock_tree.svg", pretty=True, indent=4)


# def get_top_instance_name(x, y):
#     '''
#     Maps cordinates to instance name
#     '''
#     if 0 in (x, y):
#         return "top"
#     return f"inst_1_{x}{y}"


# fishbone_pattern.get_top_instance_name = get_top_instance_name
# clk_cable = top_definition.create_cable("clk", wires=1)

# fishbone_pattern.create_ft_ports(netlist, "clk", clk_cable)
# fishbone_pattern.create_ft_connection(netlist, clk_cable)
# print("\nInstance Map")
# fishbone_pattern.print_instance_grid_map()
# print("\nModule Map")
# fishbone_pattern.print_reference_grid_map(netlist)

# netlist.compose("_buffered_tree.v", skip_constraints=True, sort_all=True)
