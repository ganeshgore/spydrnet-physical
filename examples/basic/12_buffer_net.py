"""
=============
Buffering net
=============

This example demonstrate how to buffer a net with single
``fan_in`` and single ``fan_out``


**Before buffering**

.. image:: ../auto_sample_verilog/nested_hierarchy.svg
   :align: center

**After buffering**

.. image:: ../../../examples/basic/_buffered_netlist.svg
    :align: center

"""
import logging

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.svg.composer import SVGComposer

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

netlist = sdnphy.load_netlist_by_name("nested_hierarchy")
top = netlist.top_instance.reference

# Create buffer dummy module
library = top.library
buffer = library.create_definition("buffer_x1")
buffer.create_port("A", pins=1, direction=sdn.IN)
buffer.create_port("Y", pins=1, direction=sdn.OUT)
a_cable = buffer.create_cable("A", wires=1)
y_cable = buffer.create_cable("Y", wires=1)
a_cable.assign_cable(y_cable)

# Add Buffer on Wire0
inst = next(top.get_instances("inst_1_0"))
out_wire = inst.get_port_cables("out")[0]
top.add_buffer(out_wire, buffer, instance_name="buff0")

# Add Buffer on Input Nets
# Not Implemenetd
# out_wire = inst.get_port_cables("in0")[0]
# top.add_buffer(out_wire, buffer, instance_name="input_bufer")

# Add Buffer on Output Nets
# Not Implemenetd
# out_wire = inst.get_port_cables("out0")[0]
# top.add_buffer(out_wire, buffer, instance_name="output_bufer")

# Add Buffer on Passthrough buffer
# Not Implemenetd
# out_wire = inst.get_port_cables("in_ft")[0]
# top.add_buffer(out_wire, buffer, instance_name="passthrough_bufer")

# Write netlist and render SVG
sdn.compose(netlist, "_buffered_nested_hierarchy.v", skip_constraints=True)
composer = SVGComposer()
composer.run(netlist, file_out="_buffered_netlist.svg", top_module="top")