.. _developers_guidlines:

Developers Guidelines
---------------------



Class Structure Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^


.. graphviz::
    :align: center

     digraph example {
        node[shape=box ]
        OpeFPGA [label="OpenFPGA", href="reference/openfpga/base.html", target="_top"];
        grid_matrics [label="grid_matrics"];
        fpga_matrics [label="fpga_matrics"];
        fpga_grid_dimension_matrics [label="fpga_grid_dimension_matrics - This class contains the cordinates of the origins in each grid box in the FPGA"];

        OpeFPGA -> grid_matrics;
        OpeFPGA -> fpga_matrics;
        OpeFPGA -> fpga_grid_dimension_matrics;
     }