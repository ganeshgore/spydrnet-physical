
Physical Design for 4x4 FPGA
-----------------------------

This tutorial explains a simple 4x4 FPGA design using OpenFPGA and a ``SpyDrNet-Physical`` design flow.


Architecture detail
^^^^^^^^^^^^^^^^^^^

We will consider a 4x4 Homogeneous FPGA with a 4-input LUT and a single FlipFlop as 
a logic element and eight logic elements per logic block. 
Input to every logic element is passed through a fully populated crossbar,
which can reroute any incoming CLB signal to any logic element port.
The following figure illustrates the structure of an FPGA tile.

.. image:: ./figures/SimpleFPGA.svg
   :align: center
   :width: 80%


Generating Netlist from OpenFPGA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenFPGA works based on the task-based structure, which means for generating a netlist, 
you need to create a task and configure all the required parameters. 
A sample task is provided in the ``${REPOSITORY_ROOT}/examples/homogeneous_fabric`` directory.
Some of the important files are described below


Rendering the FPGA View
^^^^^^^^^^^^^^^^^^^^^^^^



Planning Global and Clock signals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Restructuring Netlist 
^^^^^^^^^^^^^^^^^^^^^



Floorplan and Shape the FPGA 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Physical Desing Flow
^^^^^^^^^^^^^^^^^^^^


