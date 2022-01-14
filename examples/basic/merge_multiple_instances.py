"""
===========================
Merging group of instances
===========================

This example demonstrate how to merge group of instances in the design

**Initial Design**

.. hdl-diagram:: ../../../examples/basic/_initial_design.v
   :type: netlistsvg
   :align: center
   :module: top

**Output** ``inst_1_0`` and ``inst_2_0`` merged to form ``inst_3_0``
            ``inst_1_1`` and ``inst_2_1`` merged to form ``inst_3_1``

.. hdl-diagram:: ../../../examples/basic/_merge_multiple_instance.v
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
inst_2_0  = next(top.get_instances("inst_2_0"))
inst_2_1  = next(top.get_instances("inst_2_1"))

top.merge_multiple_instance([((inst_1_0, inst_2_0),"_inst_3_0"),
                            (( inst_1_1, inst_2_1),"_inst_3_1")],
                            "new_module_3")

sdn.compose(netlist,'_merge_multiple_instance.v',skip_constraints=True)