"""
=========================
Grouping ungrouping cells
=========================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

.. hdl-diagram:: ../../../examples/basic/_initial_design.v
   :type: netlistsvg
   :align: center
   :module: top


**Output1** ``wire0`` feedthough from ``inst_2_1``

.. hdl-diagram:: ../../../examples/basic/_merged_design.v
   :type: netlistsvg
   :align: center
   :module: top

"""

from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy
import logging

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')
sdn.compose(netlist, '_initial_design.v', skip_constraints=True)

netlist = sdnphy.load_netlist_by_name('nested_hierarchy')
top = netlist.top_instance.reference
inst = next(top.get_instances("inst_1_0"))
top.flatten_instance(inst)
inst = next(top.get_instances("inst_1_1"))
top.flatten_instance(inst)
top.create_unconn_wires()
sdn.compose(netlist, '_merged_design.v', skip_constraints=True)
