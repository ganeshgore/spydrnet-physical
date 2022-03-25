'''
============================
Create Clock Tree Embedding
============================


.. hdl-diagram:: ../../../../examples/OpenFPGA/clock_tree/_square_grid_design.v
   :type: netlistsvg
   :align: center
   :module: top

.. image:: ../../../../examples/OpenFPGA/clock_tree/_fishbone_pattern_0.svg
    :width: 300px
    :align: center

.. image:: ../../../../examples/OpenFPGA/clock_tree/_clock_tree_floorplan.svg
    :width: 500px
    :align: center

'''

from os import path
import spydrnet as sdn
from spydrnet_physical.util import ConnectionPattern
import spydrnet_physical as sdnphy
from spydrnet_physical.ir.definition import Definition
from pprint import pp, pprint
import yaml
from spydrnet_physical.util import FloorPlanViz


# Verilog netlist
netlist = sdnphy.load_netlist_by_name('square_grid')
top_definition = netlist.top_instance.reference
top_definition.split_port("in")
top_definition.split_port("out")
top_definition.create_unconn_wires()
sdn.compose(netlist, '_square_grid_design.v', skip_constraints=True)

netlist = sdnphy.load_netlist_by_name('square_grid')
top_definition = netlist.top_instance.reference

# Pattern
p_manager = ConnectionPattern(4, 4)
fishbone_pattern = p_manager.get_fishbone()
svg = p_manager.render_pattern(title="Merging option")
svg.saveas("_fishbone_pattern_0.svg", pretty=True, indent=4)


def get_top_instance_name(x, y):
    if 0 in (x, y):
        return "top"
    return f"inst_1_{x}{y}"


fishbone_pattern.get_top_instance_name = get_top_instance_name
clk_cable = top_definition.create_cable("clk", wires=1)
pprint(fishbone_pattern.show_stats(netlist))
fishbone_pattern.create_ft_ports(netlist, "clk", clk_cable)
fishbone_pattern.create_ft_connection(netlist, clk_cable)
fishbone_pattern.print_instance_grid_map()
print()
fishbone_pattern.print_reference_grid_map(netlist)

top_definition.split_port("in")
top_definition.split_port("out")
top_definition.create_unconn_wires()
sdn.compose(netlist, '_feedthrough_design.v',
            skip_constraints=True, write_blackbox=True)

# following section is just dummy it needs to simplify more
top_definition.properties["WIDTH"] = "700"
top_definition.properties["HEIGHT"] = "700"

next(top_definition.get_cables("row1")).split()
next(top_definition.get_cables("row2")).split()
next(top_definition.get_cables("row3")).split()
next(top_definition.get_cables("row4")).split()

next(top_definition.get_cables("clk_ft")).split()


next(top_definition.get_ports("in_3")).properties["SIDE"] = "left"
next(top_definition.get_ports("in_3")).properties["OFFSET"] = 200
next(top_definition.get_ports("in_2")).properties["SIDE"] = "left"
next(top_definition.get_ports("in_2")).properties["OFFSET"] = 300
next(top_definition.get_ports("in_1")).properties["SIDE"] = "left"
next(top_definition.get_ports("in_1")).properties["OFFSET"] = 400
next(top_definition.get_ports("in_0")).properties["SIDE"] = "left"
next(top_definition.get_ports("in_0")).properties["OFFSET"] = 500

next(top_definition.get_ports("out_0")).properties["SIDE"] = "right"
next(top_definition.get_ports("out_0")).properties["OFFSET"] = 150
next(top_definition.get_ports("out_1")).properties["SIDE"] = "right"
next(top_definition.get_ports("out_1")).properties["OFFSET"] = 200
next(top_definition.get_ports("out_2")).properties["SIDE"] = "right"
next(top_definition.get_ports("out_2")).properties["OFFSET"] = 250
next(top_definition.get_ports("out_3")).properties["SIDE"] = "right"
next(top_definition.get_ports("out_3")).properties["OFFSET"] = 300


module1 = next(netlist.get_definitions("module1"))

module1.properties["WIDTH"] = "100"
module1.properties["HEIGHT"] = "100"

next(module1.get_ports("in0")).properties["SIDE"] = "left"
next(module1.get_ports("in0")).properties["OFFSET"] = 10
next(module1.get_ports("out0")).properties["SIDE"] = "right"
next(module1.get_ports("out0")).properties["OFFSET"] = 40
next(module1.get_ports("clk_left_in")).properties["SIDE"] = "left"
next(module1.get_ports("clk_left_in")).properties["OFFSET"] = 20
next(module1.get_ports("clk_left_out")).properties["SIDE"] = "left"
next(module1.get_ports("clk_left_out")).properties["OFFSET"] = 30
next(module1.get_ports("clk_right_in")).properties["SIDE"] = "right"
next(module1.get_ports("clk_right_in")).properties["OFFSET"] = 30
next(module1.get_ports("clk_right_out")).properties["SIDE"] = "right"
next(module1.get_ports("clk_right_out")).properties["OFFSET"] = 20

next(module1.get_ports("clk_bottom_in")).properties["SIDE"] = "bottom"
next(module1.get_ports("clk_bottom_in")).properties["OFFSET"] = 35
next(module1.get_ports("clk_top_out")).properties["SIDE"] = "top"
next(module1.get_ports("clk_top_out")).properties["OFFSET"] = 35

for x in range(1, 5):
    for y in range(1, 5):
        next(netlist.get_instances(
            f"inst_1_{x}{y}")).properties["LOC_X"] = 125*x
        next(netlist.get_instances(
            f"inst_1_{x}{y}")).properties["LOC_Y"] = 125*y

fp = FloorPlanViz(top_definition)
fp.compose()
dwg = fp.get_svg()
dwg.saveas("_clock_tree_floorplan.svg", pretty=True, indent=4)
