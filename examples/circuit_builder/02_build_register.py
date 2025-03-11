"""
================================================
Build Multiplexer (SVG/Interactive)
================================================

This example demonstrates how to build a multiplexer using the `spydrnet-physical` library.

"""

# sphinx_gallery_thumbnail_path = "../../examples/circuit_builder/_mux_builder.svg"

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import circuit_builder as circ_builder

from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

netlist = sdnphy.load_netlist_by_name("std_genlib")
library = netlist.create_library("top")

top_def = library.create_definition("top_module")
top_def.create_port("shift_in", direction=sdn.IN, pins=4)
top_def.create_port("shift_out", direction=sdn.IN, pins=4)
top_def.create_port("reset", direction=sdn.IN, pins=1)
top_def.create_port("enable", direction=sdn.IN, pins=1)
top_def.create_port("clock", direction=sdn.IN, pins=1)
top_def.create_port("bitout", direction=sdn.OUT, pins=16)

netlist.set_top_instance(top_def)
netlist.top_instance.reference.name = "top_module"

# Build a single instance of MUX in this case 2:1 MUX
sipo_reg = circ_builder.build_sipo_register(
    library=library,
    flop_module=next(netlist.get_definitions("DFF_NR_EN")),
    width=4,
    depth=4,
)

sipo_reg_inst = top_def.create_child("sipo_reg", reference=sipo_reg)
top_def.create_cable("shift_in", wires=4).connect_instance_port(
    sipo_reg_inst, next(sipo_reg.get_ports("shift_in"))
)
top_def.create_cable("shift_out", wires=4).connect_instance_port(
    sipo_reg_inst, next(sipo_reg.get_ports("shift_out"))
)
top_def.create_cable("bitout", wires=16).connect_instance_port(
    sipo_reg_inst, next(sipo_reg.get_ports("out"))
)
top_def.create_cable("clock", wires=1).connect_instance_port(
    sipo_reg_inst, next(sipo_reg.get_ports("clock"))
)


sipo_reg.create_unconn_wires()

composer = HTMLComposer()
composer.run(netlist, file_out="_sipo_builder.html")

composer = SVGComposer()
composer.expand(modules=["top"])
composer.run(
    netlist,
    file_out="_sipo_builder.svg",
    netlistsvg="netlistsvg-hierarchy",
    top_module="sipo_reg",
)

sdn.compose(
    netlist, filename="_sipo_builder.v", write_blackbox=False, skip_constraints=True
)
