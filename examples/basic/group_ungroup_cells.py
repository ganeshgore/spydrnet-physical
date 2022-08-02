"""
=========================
Grouping ungrouping cells
=========================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

.. image:: ../auto_sample_verilog/nested_hierarchy.svg
    :align: center


**Output1** ungrouped module


.. image:: ../../../examples/basic/_ungrouped_design.svg
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

# Flatten inst_1_0
inst = next(top.get_instances("inst_1_0"))
top.flatten_instance(inst)

# Flatten inst_1_1
inst = next(top.get_instances("inst_1_1"))
top.flatten_instance(inst)
top.create_unconn_wires()

composer = SVGComposer()
composer.run(netlist, file_out="_ungrouped_design.svg")
