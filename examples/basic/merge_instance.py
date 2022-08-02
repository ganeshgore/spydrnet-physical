"""
===================================
Merging two instances in the design
===================================

This example demonstrate how to merge two instance in the design to create a new
merged definition

.. hdl-diagram:: ../../../spydrnet_physical/support_files/sample_verilog/nested_hierarchy.v
   :type: netlistsvg
   :align: center
   :module: top


**Output1** Merged design Instance

.. image:: ../../../examples/basic/_merged_design.svg
    :align: center

"""


import logging

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.svg.composer import SVGComposer

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

netlist = sdnphy.load_netlist_by_name("nested_hierarchy")
sdn.compose(netlist, "_initial_design_merge.v", skip_constraints=True)

netlist = sdnphy.load_netlist_by_name("nested_hierarchy")
top = netlist.top_instance.reference
inst1 = next(top.get_instances("inst_1_0"))
inst2 = next(top.get_instances("inst_1_1"))

top.merge_instance(
    [inst1, inst2],
    new_definition_name="merged_module",
    new_instance_name="merged_module_instance_0",
)

top.create_unconn_wires()

FILENAME = "_merged_design.v"
composer = SVGComposer()
composer.run(netlist, file_out=FILENAME)
