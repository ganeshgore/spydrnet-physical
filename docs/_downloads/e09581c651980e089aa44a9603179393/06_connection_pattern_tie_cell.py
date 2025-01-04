"""
=================================
Adding Tie Cells on Floating Pins
=================================

THis example

**Original grided netlist**

.. image:: ../auto_sample_verilog/square_grid.svg
    :align: center

.. image:: ../../../examples/OpenFPGA_clock_tree/_fishbone_pattern_tie_0.svg
    :width: 300px
    :align: center

**After adding tie cells**

.. hdl-diagram:: ../../../examples/OpenFPGA_clock_tree/_tie_cell_added.v
   :type: netlistsvg
   :align: center
   :module: top

"""

from os import path
from pprint import pprint
import spydrnet as sdn
from spydrnet_physical.util import ConnectionPattern
import spydrnet_physical as sdnphy


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
fishbone_pattern = p_manager.connections.merge(p_manager.get_fishbone(4, 4, steps=2))
svg = p_manager.render_pattern(title="Merging option")
svg.saveas("_fishbone_pattern_tie_0.svg", pretty=True, indent=4)


def get_top_instance_name(x, y):
    if 0 in (x, y):
        return "top"
    return f"inst_1_{x}{y}"


fishbone_pattern.get_top_instance_name = get_top_instance_name
clk_port = top_definition.create_port("clk", direction=sdn.IN, pins=1)
clk_cable = top_definition.create_cable("clk", wires=1)
clk_cable.connect_port(clk_port)
fishbone_pattern.create_ft_ports(netlist, "clk", clk_cable)
fishbone_pattern.create_ft_connection(netlist, clk_cable)

portmap = fishbone_pattern.show_stats(netlist)
pprint(dict(portmap))
for module, ports in portmap.items():
    if module == "top":
        continue
    pprint(ports["in"])
    ports = [f"clk_{key}_in" for key, value in ports["in"].items() if value]
    ports = [next(netlist.get_ports(port)).pins[0] for port in ports]
    for instance in next(netlist.get_definitions(module)).references:
        print(f">>>>>>> {instance.name}", end=" ")
        print("" if any(
            [instance.pins[port].wire for port in ports]) else "Tie this")

# fishbone_pattern.print_instance_grid_map()
# fishbone_pattern.print_reference_grid_map(netlist)

top_definition.create_unconn_wires()
sdn.compose(netlist, '_tie_cell_added.v',
            skip_constraints=True,
            write_blackbox=True)

# %%
#
#  **Output Netlist**
#
# .. literalinclude:: ../../../examples/OpenFPGA_clock_tree/_tie_cell_added.v
#    :language: verilog
#
#
