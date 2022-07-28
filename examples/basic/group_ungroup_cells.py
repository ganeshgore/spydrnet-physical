"""
=========================
Grouping ungrouping cells
=========================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

.. image:: ../auto_sample_verilog/nested_hierarchy.svg
    :align: center


**Output1** ungrouped module

.. hdl-diagram:: ../../../examples/basic/_ungrouped_design.v
   :type: netlistsvg
   :align: center
   :module: top

"""

import logging

import spydrnet as sdn
import spydrnet_physical as sdnphy

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')
top = netlist.top_instance.reference
inst = next(top.get_instances("inst_1_0"))
top.flatten_instance(inst)
inst = next(top.get_instances("inst_1_1"))
top.flatten_instance(inst)
top.create_unconn_wires()

FILENAME = "_ungrouped_design.v"
sdn.compose(netlist, FILENAME, skip_constraints=True)
logger.info("Saving merged version to %s", FILENAME)
