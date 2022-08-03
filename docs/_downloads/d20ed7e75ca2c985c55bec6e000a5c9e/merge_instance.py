"""
===================================
Merging two instances in the design
===================================

This example demonstrate how to merge two instance in the design to create a new
merged definition

.. image:: ../auto_sample_verilog/nested_hierarchy.svg
    :align: center

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
top = netlist.top_instance.reference
inst1 = next(top.get_instances("inst_1_0"))
inst2 = next(top.get_instances("inst_1_1"))

top.merge_instance(
    [inst1, inst2],
    new_definition_name="merged_module",
    new_instance_name="merged_module_instance_0",
)

top.create_unconn_wires()

composer = SVGComposer()
composer.run(netlist, file_out="_merged_design.svg")
