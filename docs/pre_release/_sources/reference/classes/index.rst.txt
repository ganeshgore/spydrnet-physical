.. _api_summary:

SpyDrNet-Physical API Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SpyDrNet API can be used to create, analyze, and transform a netlist. Netlists are represented in memory in an Intermediate Representation. The figure shows the
representation of a simple circuit in the SpyDrNet Intermediate Representation.
If you would like an example of using the SpyDrNet tool to create a netlist like this


Basic object types
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   element
   bundle
   pin
   innerpin
   outerpin
   cable
   definition
   library

Example Netlist in the Intermediate Representation

The API calls documented here can be used in Python as follows:

>>> # create an empty netlist and add an empty library to it
>>> import spydrnet as sdn
>>> netlist = sdn.ir.Netlist()
>>> library = netlist.create_library()
>>>

If the parser is used, the calls can be made in the same way:

>>> # parse an edif file in and add an empty library to the netlist.
>>> import spydrnet as sdn
>>> netlist = sdn.parse('four_bit_counter.edf')

>>> library = netlist.create_library
>>>

.. _fig:ExampleIR:
.. figure:: ../../figures/ExampleCircuit.png
   :align: center
   :alt: Example Netlist in a SpyDrNet Intermediate Representation
