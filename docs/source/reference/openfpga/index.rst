.. _openfpga_transformations:

========================
OpenFPGA Transformations
========================

`OpenFPGA_Base` is the base class for OpenFPGA related transformation, expected input for this class in OpenFPGA generated netlist. This provides basic functionality like converting wires to buses or merging GPIO modules with neighboring blocks.


Base Transformations
""""""""""""""""""""
.. toctree::
   :maxdepth: 1

   base

   ../utility_classes/openfpga_arch
   
   routing_render


Tiling APIs
============

.. toctree::
   :maxdepth: 1

   tile01
   tile02


Configuration APIs
===================

Verification APIs
=================

SDC APIs
=========


OpenFPGA Class Generators
'''''''''''''''''''''''''

:doc:`OpenFPGA_Tile_Generator <../utility_classes/openfpga_tile_generator>`
..................................................................


:doc:`OpenFPGA_Config_Generator <../utility_classes/openfpga_config_generator>`
..................................................................

.. toctree::
   :maxdepth: 1
   
   ../utility_classes/config_chain_01
   ../utility_classes/config_chain_simple
   ../utility_classes/sram_configuration


:doc:`OpenFPGA_Placement_Generator <../utility_classes/openfpga_placement_generator>`
..................................................................

.. toctree::
   :maxdepth: 1
   
   ../utility_classes/initial_placement


:doc:`OpenFPGA_Bitstream_Manager <../utility_classes/openfpga_bitstream>`
..................................................................

.. toctree::
   :maxdepth: 1
   
   ../utility_classes/openfpga_bitstream
