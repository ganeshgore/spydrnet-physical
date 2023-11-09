#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================
Generating feedthrough from multiple instances
==============================================

This example demonstrates how to generate feedthrough from multiple instances.
If multiple instances belong to the same reference module it should reuser
the feedthrough instead of creating independent feedthrough to pass through each instance.

This example creates new wire ``A`` and create feedthrough port and connection
from  ``inst_1_0`` and  ``inst_1_1`` in sequence.


**Before feedthrough**

.. image:: ../../../examples/basic/_basic_hierarchy_design.svg
   :align: center

**After feedthrough**

.. image:: ../../../examples/basic/_Feedthrough_basic_hierarchy_design.svg
    :align: center

"""

import logging
import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

# logger.warning("NotImplemented")


netlist = sdnphy.load_netlist_by_name('grid_example')
top = netlist.top_instance.reference

a_in_port = top.create_port(name='a_in', direction=sdn.IN, pins=1)
a_out_port = top.create_port(name='a_out', direction=sdn.OUT, pins=1)
b_in_port = top.create_port(name='b_in', direction=sdn.IN, pins=1)
b_out_port = top.create_port(name='b_out', direction=sdn.OUT, pins=1)
a_in_cable = top.create_cable(name='a_in', wires=1)
b_in_cable = top.create_cable(name='b_in', wires=1)
a_out_cable = top.create_cable(name='a_out', wires=1)
b_out_cable = top.create_cable(name='b_out', wires=1)

a_in_cable.connect_port(a_in_port)
b_in_cable.connect_port(b_in_port)
a_out_cable.connect_port(a_out_port)
b_out_cable.connect_port(b_out_port)

b_in_cable.assign_cable(b_out_cable)
a_in_cable.assign_cable(a_out_cable)

inst1 = next(top.get_instances('inst_1_11'))
inst11 = next(top.get_instances('inst_2_11'))
inst2 = next(top.get_instances('inst_1_12'))
inst21 = next(top.get_instances('inst_2_12'))

inst_list = (
    (a_in_cable, [inst1, inst11]),
    (b_in_cable, [inst2, inst21]),
)

top.create_parallel_feedthrough(inst_list)
top.create_unconn_wires()

composer = HTMLComposer()
composer.run(netlist, file_out="_Feedthrough_basic_hierarchy_design.html")
composer = SVGComposer()
composer.expand(modules=["module1"])
composer.run(netlist, file_out="_Feedthrough_basic_hierarchy_design.svg",
             netlistsvg="netlistsvg-hierarchy")
sdn.compose(netlist, '_basic_hierarchy_after_multiple_feedthrough.v',
            skip_constraints=True)
