"""
===============================
Visualise Hierarchical Netlist
===============================

This example demonstrates how to visualize a netlist
In SVG format, which uses Yosys and netlist SVG to render
Interactive viewer, which render hierarchical SVG using the `d3-hwschematic` project

.. image:: ../auto_sample_verilog/basic_hierarchy.svg
    :align: center

.. rst-class:: hidden

.. image:: ../../../examples/basic/_initial_design.html
    :align: center

.. raw:: html

    <iframe width="100%" height="400" scrolling="no" frameBorder="1"
    src="/_images/_initial_design.html"></iframe>


`Open schematic in separate window </_images/_initial_design.html>`_

The renderer is used from this project
`Nic30/d3-hwschematic <https://github.com/Nic30/d3-hwschematic>`_

"""
# sphinx_gallery_thumbnail_path = 'auto_sample_verilog/basic_hierarchy.svg'
import spydrnet_physical as sdnphy
from spydrnet_physical.composers.html.composer import HTMLComposer
from spydrnet_physical.composers.svg.composer import SVGComposer

netlist = sdnphy.load_netlist_by_name("basic_hierarchy")

composer = HTMLComposer()
composer.run(netlist, file_out="_initial_design.html")

composer = SVGComposer()
composer.run(netlist, file_out="_initial_design.svg")
