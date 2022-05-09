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


Configuration APIs
===================

Verification APIs
=================

SDC APIs
=========



OpenFPGA Class Templates
''''''''''''''''''''''''

:doc:`initial_placement <../utility_classes/initial_placement>`
................................................


:doc:`OpenFPGA_Config_Generator <../utility_classes/openfpga_config_generator>`
..................................................................


:doc:`OpenFPGA_Placement_Generator <../utility_classes/openfpga_placement_generator>`
..................................................................


:doc:`OpenFPGA_Tile_Generator <../utility_classes/openfpga_tile_generator>`
..................................................................

:doc:`config_chain_01 <../utility_classes/config_chain_01>`
..................................................................


:doc:`config_chain_simple <../utility_classes/config_chain_simple>`
..................................................................