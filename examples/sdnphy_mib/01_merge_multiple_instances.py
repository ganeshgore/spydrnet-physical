"""
===================================
Merging group of multiple instances
===================================

This example demonstrate how to merge group of instances in the design.

Following example has four instances, ``inst_1_0`` and ``inst_1_1`` are instance of ``module1``
and ``inst_2_0`` and ``inst_2_1`` are instance of ``module2``.

This example merges ``inst_1_0`` and ``inst_2_0``, ``inst_1_1`` and ``inst_2_1`` and replace with instance (``inst_3_0`` and ``inst_3_1``) of newly created defintion ``module3``

**Before merging**

.. image:: ../../../examples/sdnphy_mib/_basic_inst_design.svg
   :align: center

**After merging**

.. image:: ../../../examples/sdnphy_mib/_merged_mul_inst_design.svg
    :align: center

"""

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
inst1 = next(top.get_instances('inst_1_0'))
inst2 = next(top.get_instances('inst_2_0'))
inst3 = next(top.get_instances('inst_1_1'))
inst4 = next(top.get_instances('inst_2_1'))

inst_tup_list = ([inst1, inst2], "inst_3_0"), \
                ([inst3, inst4], "inst_3_1")

composer = HTMLComposer()
composer.run(netlist, file_out="_basic_inst_design.html")
composer = SVGComposer()
composer.run(netlist, file_out="_basic_inst_design.svg")

top.merge_multiple_instance(inst_tup_list, new_definition_name="module3")

sdn.compose(netlist, '_merged_mul_inst_design.v', skip_constraints=True)

composer = HTMLComposer()
composer.run(netlist, file_out="_merged_mul_inst_design.html")

composer = SVGComposer()
composer.run(netlist, file_out="_merged_mul_inst_design.svg")
