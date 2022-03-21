.. _utility_functions:

=================
Utility Functions
=================


Overview
^^^^^^^^

.. currentmodule:: util


Helper methods
~~~~~~~~~~~~~~


.. autosummary::
   :toctree: generated

    get_names
    get_attr

Connectivity Pattern Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated

    ConnectPoint
    ConnectPointList
    ConnectionPattern


OpenFPGA Helper Classes
~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated

    OpenFPGA
    FPGAGridGen
    initial_placement


Rendering and Visualization 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated
    
    FloorPlanViz
    RoutingRender
    cb_renderer
    sb_renderer


Graph Generation and Partitioning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated

    prepare_graph_from_nx
    write_metis_graph
    run_metis


FPGA Tiling Related
~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: generated

    OpenFPGA_Config_Generator
    OpenFPGA_Placement_Generator
    OpenFPGA_Tile_Generator
    openfpga_floorplan

    OpenFPGA_Arch
    Tile01
    config_chain_01
    config_chain_simple
