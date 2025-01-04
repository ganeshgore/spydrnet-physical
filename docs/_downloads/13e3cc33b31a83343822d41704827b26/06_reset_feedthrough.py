"""
=====================================
Create Reset Feedthrough in fpga_top
=====================================

.. image:: ../../../examples/OpenFPGA_clock_tree/_reset_connections.svg
    :width: 220px
    :align: center

"""
import glob
import logging
import sys
import tempfile
from itertools import chain
from pprint import pprint

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import ConnectionPattern, OpenFPGA

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Read FPGA Netlist
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
proj = "../homogeneous_fabric/*_Verilog"
task = "../homogeneous_fabric/*_Task"
source_files = glob.glob(f"{proj}/lb/*.v")
source_files += glob.glob(f"{proj}/routing/*.v")
source_files += glob.glob(f"{proj}/sub_module/*.v")
source_files += glob.glob(f"{task}/CustomModules/standard_cell_primitives.v")
source_files += glob.glob(f"{proj}/fpga_top.v")

# Create OpenFPGA object
fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

# Convert wires to bus structure
fpga.create_grid_clb_bus()
fpga.create_grid_io_bus()
fpga.create_sb_bus()
fpga.create_cb_bus()
fpga.remove_config_chain()
fpga.remove_undriven_nets()

# Top level nets to bus
for i in chain(
    fpga.top_module.get_instances("grid_clb*"),
    fpga.top_module.get_instances("grid_io*"),
    fpga.top_module.get_instances("sb_*"),
):
    for p in filter(lambda x: True, i.reference.ports):
        if p.size > 1 and (i.check_all_scalar_connections(p)):
            cable_list = []
            for pin in p.pins[::-1]:
                cable_list.append(i.pins[pin].wire.cable)
            fpga.top_module.combine_cables(f"{i.name}_{p.name}", cable_list)

fpga.merge_all_grid_ios()
fpga.remove_direct_interc()

top_definition = fpga.top_module

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#  Generate reset connection pattern
# 4x4 FPGA grid is considered as a 9x9 grid during pattern generation
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
p_manager = ConnectionPattern(9, 9)
points = p_manager.get_fishbone(9, 9, steps=2)
reset_conn_patt = p_manager.connections.merge(points)
svg = p_manager.render_pattern(title="Merging option")
svg.saveas("_reset_connections.svg", pretty=True, indent=4)


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
        (x % 2 == 0) and (y % 2 == 1): "cbx",
    }[True]
    return f"{module}_{int(x/2)}__{int(y/2)}_"


# Check mapping byt ptinting 2D grid
for y in range(9, 0, -1):
    for x in range(1, 9 + 1):
        print(f"{get_top_instance_name(x, y):15}", end=" ")
    print("")

# Embedded the connectivity

sdn.compose(
    fpga.netlist,
    "_fpga_top_initial.v",
    definition_list=["fpga_top"],
    skip_constraints=True,
    write_blackbox=False,
)

# reset_cable = top_definition.create_cable("reset_wire", wires=1)
reset_cable = next(top_definition.get_cables("reset"))
reset_conn_patt.get_top_instance_name = get_top_instance_name
pprint(reset_conn_patt.show_stats(fpga.netlist))
reset_conn_patt.create_ft_ports(fpga.netlist, "reset", reset_cable)
reset_conn_patt.create_ft_connection(fpga.netlist, reset_cable)
sdn.compose(
    fpga.netlist,
    "_fpga_top.v",
    definition_list=["fpga_top"],
    skip_constraints=True,
    write_blackbox=False,
)
