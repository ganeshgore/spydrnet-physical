
Physical Design for 4x4 FPGA
-----------------------------

This tutorial explains a simple 4x4 homogeneous FPGA design using OpenFPGA and 
a ``OpenFPGA-Physical`` design flow.


Directory Structure
^^^^^^^^^^^^^^^^^^^

We will use the following directory structure as a part of this project 
`Openfpga-Physical <https://github.com/ganeshgore/openfpga-physical>`_


Architecture detail
^^^^^^^^^^^^^^^^^^^
In this tutorial, we will consider a 4x4 Homogeneous FPGA with a 4-input LUT and a single FlipFlop as 
a logic element and eight logic elements per logic block (AKA K4N8 architecture). 
Input to every logic element is passed through a fully populated crossbar,
which can reroute any incoming CLB signal to any logic element port.
The following figure illustrates the structure of an FPGA tile.

.. image:: ./figures/SimpleFPGA.svg
   :align: center
   :width: 80%


Generating Netlist from OpenFPGA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenFPGA works based on the project structure (which is referred to as a task in OpenFPGA),
which means for generating a netlist, 
you need to create a task and configure all the required parameters.
Please refer to the OpenFPGA documenation `Getting Started`_ and `OpenFPGA Shortcuts`_ for more detail.
A sample task is provided in the ``${REPOSITORY_ROOT}/examples/homogeneous_fabric`` directory.
Some of the essential files provided in this directory are:

- **FPGA44_Task/arch/k4_N8_tileable.xml**: VPR architecture XML file, this describes the FPGA architecture
- **FPGA44_Task/arch/k4_N8_openfpga.xml**: OpenFPGA architecture XML file maps various physical cells to the described FPGA architecture 
- **FPGA44_Task/config/task_generation.conf**: OpenFPGA task file, it consists of various variable assignement
- **FPGA44_Task/generate_fabric.openfpga**: OpenFPGA script file, which lists the sequence of commands to generate FPGA fabric (Please read comments in the file for more information)


Rendering the FPGA View
^^^^^^^^^^^^^^^^^^^^^^^^



Planning Global and Clock signals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Restructuring Netlist 
^^^^^^^^^^^^^^^^^^^^^



Floorplan and Shape the FPGA 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Physical Design Flow
^^^^^^^^^^^^^^^^^^^^

Yet to finish


.. _Getting Started: https://openfpga.readthedocs.io/en/latest/tutorials/getting_started/
.. _OpenFPGA Shortcuts: https://openfpga.readthedocs.io/en/latest/tutorials/getting_started/shell_shortcuts/