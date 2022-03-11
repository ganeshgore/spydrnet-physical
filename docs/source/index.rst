.. figure:: figures/spydrnet-physical-logo.svg
    :align: center
    :width: 50%
    :class: main_image

.. TODO: Add readme here and small snippets hoe to use
.. .. include:: ../../README.rst

.. .. only:: html

..     :Release: |version|
..     :Date: |today|

================================
SpyDrNet-Physical Documentation
================================

`SpyDrNet <https://github.com/byuccl/spydrnet>`_ is a flexible framework for 
analyzing and transforming structural Verilog netlists. 
It allows users to design a complete structural Verilog netlist 
using python scripting or parser an existing Verilog netlist.
The structural Verilog netlist is represented as a python class
that simplifies the netlist modification process.
The ``SpyDrNet`` is purely designed as a python package, keeping scalability in mind.
In ``SpyDrNet-Physical`` is an extension for ``SpyDrNet`` framework,
which adds functionality to perform physical design-related
netlist transformations.


Essential characteristics of ``SpyDrNet-Physical``


.. rst-class:: circlelist

* Appends features like `create_feedthrough`, `create_feedthrough_multiple`, `merge_instance` 
  which are important during netlist restructuring for physical design
* Includes some `html` and `graph-based` visualization features
* Only supports Verilog netlist, no support for EDIF or any other formats


Table of Contents
=================


.. toctree::
   :maxdepth: 1

   introduction/install
   introduction/tutorial
   reference/index
   auto_sample_verilog/index
   example

.. .. toctree::
..    :maxdepth: 1

..    introduction/install
..    introduction.rst
..    tests/index


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
