"""
===================================
Merging two instances in the design
===================================

This example demonstrate how to merge two instance of the design

**Initial Design**

.. hdl-diagram:: ../../../examples/basic/_initial_design.v
   :type: netlistsvg
   :align: center
   :module: top

**Output** ``inst_1_0`` and ``inst_1_1`` merged to form ``merged_inst_1``

.. hdl-diagram:: ../../../examples/basic/_merge_instance.v
   :type: netlistsvg
   :align: center
   :module: top

"""

from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')
top = netlist.top_instance.reference

inst_1_0  = next(top.get_instances("inst_1_0"))
inst_1_1  = next(top.get_instances("inst_1_1"))

top.merge_instance([inst_1_0, inst_1_1], "merged_module_1", "merged_inst_1", lambda ex,pin,instance: f"{pin}_{instance}" )
sdn.compose(netlist,'_merge_instance.v',skip_constraints=True)

