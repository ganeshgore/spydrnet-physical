"""
===========================
Merging group of instances
===========================

This example demonstrate how to merge group of instances in the design

**Before Merging**

.. image:: ../../../examples/basic/_basic_inst_design.svg
   :align: center

**After Merging**

.. image:: ../../../examples/basic/_Merged_mul_inst_design.svg
    :align: center

"""

from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
inst1 = next(top.get_instances('inst_1_0'))
inst2 = next(top.get_instances('inst_2_0'))
inst3= next(top.get_instances('inst_1_1'))
inst4 = next(top.get_instances('inst_2_1'))

inst_tup_list = ([inst1, inst2], "merged_inst1"), ([inst3, inst4], "merged_inst2")

composer = HTMLComposer()
composer.run(netlist, file_out="_basic_inst_design.html")
composer = SVGComposer()
composer.run(netlist, file_out="_basic_inst_design.svg")

top.merge_multiple_instance(inst_tup_list, new_definition_name = "merged_insts")

sdn.compose(netlist, '_merged_mul_inst_design.v', skip_constraints=True)

composer = HTMLComposer()
composer.run(netlist, file_out="_Merged_mul_inst_design.html")

composer = SVGComposer()
composer.run(netlist, file_out="_Merged_mul_inst_design.svg")

