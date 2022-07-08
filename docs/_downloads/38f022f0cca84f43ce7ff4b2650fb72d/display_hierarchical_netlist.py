"""
===============================
Visualise Hierarchical Netlist
===============================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.


.. image:: ../auto_sample_verilog/basic_hierarchy.svg
    :align: center

.. raw:: html

    <iframe width="100%" height="400" scrolling="no" frameBorder="1"
    src="/_images/_initial_design.html"></iframe>


`Open schematic in separate window </_images/_initial_design.html>`_

The renderer is used from this project `Nic30/d3-hwschematic <https://github.com/Nic30/d3-hwschematic>`_

"""
#sphinx_gallery_thumbnail_path = '../../examples/basic/2.png'

import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference


composer = HTMLComposer()
composer.run(netlist, file_out="_initial_design.html")
