"""
=======================================
Two layer H-Tree insertion in 4x4 FPGA 
=======================================

This example demonstrates how to insert H-Tree in tileable FPGA grid.

In this example we try to implement 2-layer HTree in 2x2 FPGA grid.
First we create 2 different connection patterns to implement on each level of
the clock tree, and then embed these pattern using ``create_ft_ports`` and 
``create_ft_connection`` methods. 

.. Note: the dotted line indicates that the connection is either coming from 
   upper layer or going to lower layer.

.. image:: ../../../../examples/OpenFPGA/clock_tree/_clock_tree_connections_l0.svg
    :width: 220px

.. image:: ../../../../examples/OpenFPGA/clock_tree/_clock_tree_connections_l1.svg
    :width: 220px

.. image:: ../../../../examples/OpenFPGA/clock_tree/_clock_tree_connections.svg
    :width: 220px

"""

import glob
import logging
import sys
import tempfile
from itertools import chain

import spydrnet as sdn
from spydrnet_physical.util import ConnectionPattern, OpenFPGA
from spydrnet_physical.util.ConnectPoint import ConnectPoint


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Generate Level-1 (top level) connectivity pattern
# 4x4 FPGA grid is considered as a 9x9 grid during pattern generation
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
WIDTH = 9
HEIGHT = 9
p_manager = ConnectionPattern(WIDTH, HEIGHT)
l1_patt = p_manager.connections
l1_patt.cursor = (int(WIDTH/2)+1, 0)
l1_patt.move_y(steps=int(WIDTH/2)+1)
l1_patt.merge(p_manager.get_htree(WIDTH))
l1_patt.set_color("red")
# This is important step to indicate on which connection is transitioning
# to the next level
for x in range(2):
    for y in range(2):
        l1_patt.push_connection_down((3+(x*4), 3+(y*4)))
svg = p_manager.render_pattern(title="L1 Pattern")
svg.saveas("_clock_tree_connections_l0.svg", pretty=True, indent=4)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Generate Level-0 connectivity pattern
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
p_manager = ConnectionPattern(WIDTH, HEIGHT)
l0_patt = p_manager.connections
l0_patt.merge(p_manager.get_htree(4).translate(1, 1))
l0_patt.merge(p_manager.get_htree(4).translate(5, 1))
l0_patt.merge(p_manager.get_htree(4).translate(5, 5))
l0_patt.merge(p_manager.get_htree(4).translate(1, 5))

for x in range(2):
    for y in range(2):
        ydir = -1 if y else 1
        pt = ConnectPoint(3+(x*4), 3+(y*4)+ydir, 3+(x*4), 3+(y*4))
        l0_patt.add_connect_point(pt)
        l0_patt.pull_connection_up(pt)
l0_patt.set_color("grey")
svg = p_manager.render_pattern(title="L0 Pattern")
svg.saveas("_clock_tree_connections_l1.svg", pretty=True, indent=4)

p_manager = ConnectionPattern(WIDTH, HEIGHT)
combine_pattern = p_manager.connections
combine_pattern.merge(l0_patt)
combine_pattern.merge(l1_patt)
svg = p_manager.render_pattern(title="Combined Pattern")
svg.saveas("_clock_tree_connections.svg", pretty=True, indent=4)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Prepare cordinate mapping function for embedding
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


def get_top_instance_name(x, y):
    if 0 in (x, y):
        return "top"
    module = {
        True: "sb",
        (x % 2 == 0) and (y % 2 == 0): "grid_clb",
        (x % 2 == 1) and (y % 2 == 0): "cby",
        (x % 2 == 0) and (y % 2 == 1): "cbx"}[True]
    return f"{module}_{int(x/2)}__{int(y/2)}_"


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Read FPGA Netlist
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
proj = '../homogeneous_fabric/*_Verilog'
task = '../homogeneous_fabric/*_Task'
source_files = glob.glob(f'{proj}/lb/*.v')
source_files += glob.glob(f'{proj}/routing/*.v')
source_files += glob.glob(f'{proj}/sub_module/*.v')
source_files += glob.glob(f'{task}/CustomModules/standard_cell_primitives.v')
source_files += glob.glob(f'{proj}/fpga_top.v')

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

# Temporary fix to read multiple verilog files
with tempfile.NamedTemporaryFile(suffix=".v") as fp:
    for eachV in source_files:
        with open(eachV, "r") as fpv:
            fp.write(str.encode(" ".join(fpv.readlines())))
    fp.seek(0)
    netlist = sdn.parse(fp.name)


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Cleanup FPGA netlist for printing
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

fpga = OpenFPGA(grid=(4, 4), netlist=netlist)

# Convert wires to bus structure
fpga.create_grid_clb_bus()
fpga.create_grid_io_bus()
fpga.create_sb_bus()
fpga.create_cb_bus()
fpga.remove_config_chain()
fpga.remove_undriven_nets()

# Top level nets to bus
for i in chain(fpga.top_module.get_instances("grid_clb*"),
               fpga.top_module.get_instances("grid_io*"),
               fpga.top_module.get_instances("sb_*")):
    for p in filter(lambda x: True, i.reference.ports):
        if p.size > 1 and (i.check_all_scalar_connections(p)):
            cable_list = []
            for pin in p.pins[::-1]:
                cable_list.append(i.pins[pin].wire.cable)
            fpga.top_module.combine_cables(
                f"{i.name}_{p.name}", cable_list)
fpga.merge_all_grid_ios()
fpga.remove_direct_interc()

top_definition = fpga.top_module

sdn.compose(netlist, '_fpga_top_initial.v', definition_list=["fpga_top"],
            skip_constraints=True, write_blackbox=False)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Embed L0 pattern and the L1 pattern
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

clk_l0_cable = top_definition.create_cable("clk_l0", wires=1)
l0_patt.get_top_instance_name = get_top_instance_name
l0_patt.create_ft_ports(netlist, "clk_l0", clk_l0_cable)
l0_patt.create_ft_connection(netlist, clk_l0_cable)

clk_l1_cable = top_definition.create_cable("clk_l1", wires=1)
l1_patt.get_top_instance_name = get_top_instance_name
l1_patt.create_ft_ports(netlist, "clk_l1", clk_l1_cable)
l1_patt.create_ft_connection(netlist, clk_l1_cable, down_port="clk_l0")

sdn.compose(netlist, '_fpga_top.v', definition_list=["fpga_top"],
            skip_constraints=True, write_blackbox=False)
