"""
================================================
Build Multiplexer (SVG/Interactive)
================================================

This example demonstrates how to build a multiplexer using the `spydrnet-physical` library.

"""

# sphinx_gallery_thumbnail_path = "../../examples/circuit_builder/_mux_builder.svg"

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import circuit_builder as cb

from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

netlist = sdn.Netlist("sample")
library = netlist.create_library("top")

# Build standard 2-to-1 multiplexer
mux2 = library.create_definition("mux2")
mux2.create_port("IN0", direction=sdn.IN, pins=1)
mux2.create_port("IN1", direction=sdn.IN, pins=1)
mux2.create_port("SEL", direction=sdn.IN, pins=1)
mux2.create_port("OUT", direction=sdn.OUT, pins=1)

top_def = library.create_definition("top_module")
top_def.create_port("top_in0", direction=sdn.IN, pins=1)
top_def.create_port("top_in1", direction=sdn.IN, pins=1)
top_def.create_port("top_sel", direction=sdn.IN, pins=1)
top_def.create_port("top_out", direction=sdn.OUT, pins=1)

netlist.set_top_instance(top_def)

# Build a single instance of MUX in this case 2:1 MUX
cb.create_mux_instance(
    top=top_def,
    name="mux2to1",
    reference=mux2,
    inputs_w=[
        top_def.create_cable("top_in0", wires=1).wires[0],
        top_def.create_cable("top_in1", wires=1).wires[0],
    ],
    output_w=top_def.create_cable("top_out", wires=1).wires[0],
    select_w=[
        top_def.create_cable("top_sel", wires=1).wires[0],
    ],
)

# Build a larger MUX using tree-like structure and given list of MUXes
# Note select lines are not computed before and interfered from the structure
mux_size=12
top_def.create_port("input_bus", direction=sdn.IN, pins=mux_size)
top_def.create_port("top_out2", direction=sdn.OUT, pins=1)


out_wire, select_cable = cb.build_tree_like_mux(
    definition=top_def,
    inputs=top_def.create_cable("input_bus", wires=mux_size).wires,
    mux_dictionary={2: mux2},
    select_cable=top_def.create_cable("top_select2"),
    suffix="_OOOOOOO",
)

# Adjust the select port pin count
top_def.create_port("top_select2", direction=sdn.IN, pins=len(select_cable.wires))

# Assign output wire to output port cable
out_wire.cable.assign_cable(top_def.create_cable("top_out2", wires=1))


composer = HTMLComposer()
composer.run(netlist, file_out="_mux_builder.html")

composer = SVGComposer()
composer.expand(modules=["top"])
composer.run(netlist, file_out="_mux_builder.svg", netlistsvg="netlistsvg-hierarchy")
