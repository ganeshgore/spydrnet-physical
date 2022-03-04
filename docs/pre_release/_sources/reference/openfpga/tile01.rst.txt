
.. _openfpga_tile01:


========
Tile-01
========

This tiling method performance minimal modification in the OpenFPGA generated netlist. After performing base manipulation to convert wires to buses, this tiling scheme merges neighboring instances to form a structure like shown below.
This scheme is biased toward the top and right side connections boxes and right-top side switch box, as it merges connection boxes on top and right and sb on the right-top corner for flat design.

The flat design of the merged module allows setting tighter timing constraints on all internal paths.

.. image:: ./Tile01/figure/tile-01.svg
   :width: 500px
   :align: center

Detail of each Tile
----------------------

.. toctree::
   :maxdepth: 1

   Tile01/tile
   Tile01/left-tile
   Tile01/right-tile
   Tile01/top-tile
   Tile01/bottom-tile
   Tile01/top-left-tile
   Tile01/top-right-tile
   Tile01/bottom-left-tile
   Tile01/bottom-right-tile


Methods
=======
.. currentmodule:: spydrnet_physical.util
.. autoclass:: Tile01
   :private-members:
   :members:
   :member-order: bysource