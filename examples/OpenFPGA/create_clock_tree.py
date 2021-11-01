'''
============================
Create Clock Tree Embedding
============================


.. hdl-diagram:: ../../../examples/OpenFPGA/_square_grid_design.v
   :type: netlistsvg
   :align: center
   :module: top

.. image:: ../../../examples/OpenFPGA/_fishbone_pattern_0.svg
    :width: 300px
    :align: center

.. image:: ../../../examples/OpenFPGA/_clock_tree_floorplan.svg
    :width: 500px
    :align: center

'''
# .. hdl-diagram:: ../../../examples/OpenFPGA/_feedthrough_design.v
#    :type: netlistsvg
#    :align: center
#    :module: top

from os import path
import spydrnet as sdn
from spydrnet_physical.util.connection_pattern import ConnectionPattern
import spydrnet_physical as sdnphy
from spydrnet_physical.ir.definition import Definition
from pprint import pp, pprint
import yaml
from spydrnet_physical.util.get_floorplan import FloorPlanViz


# Verilog netlist
netlist = sdnphy.load_netlist_by_name('square_grid')
top_definition = netlist.top_instance.reference
top_definition.split_port("in")
top_definition.split_port("out")
top_definition.create_unconn_wires()
sdn.compose(netlist, '_square_grid_design.v')

netlist = sdnphy.load_netlist_by_name('square_grid')
top_definition = netlist.top_instance.reference

# Pattern
p_manager = ConnectionPattern(4, 4)
fishbone_pattern = p_manager.get_fishbone()
svg = p_manager.render_pattern(title="Merging option")
svg.saveas("_fishbone_pattern_0.svg", pretty=True, indent=4)


def get_reference(x, y):
    if 0 in (x, y):
        return "top"
    return next(netlist.get_instances(f"inst_1_{x}{y}")).reference.name


signal = "clk"
p_manager.get_reference = get_reference
stat = p_manager.show_stats()
print(yaml.dump(stat))


# Count required feedthoguhs for the modules and create ports
for module_name, values in stat.items():
    if module_name == "top":
        continue
    module: Definition = next(netlist.get_definitions(module_name))
    pp = next(module.get_ports(signal))
    for inp in [k for k, v in values["in"].items() if v > 0]:
        module.create_port(f"{signal}_{inp}_in",
                           pins=pp.size, direction=sdn.IN)
        module.create_cable(f"{signal}_{inp}_in", wires=pp.size)
    for outp in [k for k, v in values["out"].items() if v > 0]:
        module.create_port(f"{signal}_{outp}_out",
                           pins=pp.size, direction=sdn.OUT)
        module.create_cable(f"{signal}_{outp}_out", wires=pp.size)


module1 = next(netlist.get_definitions("module1"))
module1.remove_port(next(module1.get_ports("clk")))

# Create connetions
cable = top_definition.create_cable(signal+"_ft")
signal_port = top_definition.create_port("clk", direction=sdn.IN, pins=1)
signal_cable = top_definition.create_cable("clk", wires=1)

for point in p_manager._connect._points:
    w = cable.create_wire()
    if 0 in point.from_connection:
        signal_cable.assign_cable(cable, upper=w.get_index, lower=w.get_index)
    else:
        inst_name = "inst_1_%d%d" % point.from_connection
        inst = next(netlist.get_instances(inst_name))
        port_name = f"{signal}_{point.from_dir}_out"
        w.connect_pin(next(inst.get_port_pins(port_name)))

    if 0 in point.to_connection:
        w.connect_pin(signal_port.pins[0])
    else:
        inst = next(netlist.get_instances("inst_1_%d%d" % point.to_connection))
        w.connect_pin(next(inst.get_port_pins(
            f"{signal}_{point.to_dir}_in")))


top_definition.split_port("in")
top_definition.split_port("out")
top_definition.create_unconn_wires()
sdn.compose(netlist, '_feedthrough_design.v', write_blackbox=True)

# following section is just dummy it needs to simplify more
top_definition.properties["WIDTH"] = "700"
top_definition.properties["HEIGHT"] = "700"

next(top_definition.get_cables("row1")).split_cable()
next(top_definition.get_cables("row2")).split_cable()
next(top_definition.get_cables("row3")).split_cable()
next(top_definition.get_cables("row4")).split_cable()

next(top_definition.get_cables("clk_ft")).split_cable()


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
