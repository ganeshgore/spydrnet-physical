#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================
Generating feedthrough from multiple instances
==============================================

This example demonstrates how to generate feedthrough from multiple instances.
If multiple instances belong to the same reference module it should reuser 
the feedthrough instead of creating independent feedthrough to pass through each instance.

**Before feedthrough**

.. image:: ../../../examples/basic/_basic_hierarchy_design.svg
   :align: center

**After feedthrough**

.. image:: ../../../examples/basic/_Feedthrough_basic_hierarchy_design.svg
    :align: center

"""

import logging
from os import path
from unicodedata import name
import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')

#logger.warning("NotImplemented")


netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
inst1 = next(top.get_instances('inst_1_0'))
inst2 = next(top.get_instances('inst_1_1'))


composer = HTMLComposer()
composer.run(netlist, file_out="_basic_hierarchy_design.html")
composer = SVGComposer()
composer.run(netlist, file_out="_basic_hierarchy_design.svg")

cable = top.create_cable(name= 'A')
wire = cable.create_wire()

inst_list = [(cable,[inst1, inst2])]

top.create_feedthrough_multiple(inst_list)
top.create_unconn_wires()
    
composer = HTMLComposer()
composer.run(netlist, file_out="_Feedthrough_basic_hierarchy_design.html")
composer = SVGComposer()
composer.run(netlist, file_out="_Feedthrough_basic_hierarchy_design.svg")