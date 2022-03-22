"""
===============================
Visualise Hierarchical Netlist
===============================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.


.. image:: ../../../examples/basic/_initial_design.html
   :width: 0px
   :class: hidden

.. raw:: html

    <iframe width="100%" height="400" scrolling="no" frameBorder="1"
    src="/_images/_initial_design.html"></iframe>


`Open schematic in separate window </_images/_initial_design.html>`_

The renderer is used from this project `Nic30/d3-hwschematic <https://github.com/Nic30/d3-hwschematic>`_

"""
from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
sdn.compose(netlist, '_initial_design.v', skip_constraints=True)

composer = HTMLComposer()
composer.run(netlist, file_out="_initial_design.html")
