"""
==========================================
Genrating feedthrough from single instance
==========================================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

**Initial Design**

.. hdl-diagram:: ../../../examples/basic/_initial_design.v
   :type: netlistsvg
   :align: center
   :module: top


**Output1** ``wire0`` feedthough from ``inst_2_1``

.. hdl-diagram:: ../../../examples/basic/_output_wire.v
   :type: netlistsvg
   :align: center
   :module: top

**Output2** ``bus_in`` feedthrough from ``inst_1_0``

.. hdl-diagram:: ../../../examples/basic/_output_bus.v
   :type: netlistsvg
   :align: center
   :module: top

"""

from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
cable0 = next(top.get_cables("wire0"))
inst2 = next(top.get_instances("inst_2_0"))

sdn.compose(netlist, '_initial_design.v')


top.create_feedthrough(inst2, cable0)
top.create_unconn_wires()
sdn.compose(netlist, '_output_wire.v')


netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
bus_in = next(top.get_cables("bus_in"))
inst1 = next(top.get_instances("inst_1_0"))

cables = top.create_feedthrough(inst1, bus_in)
top.create_unconn_wires()
sdn.compose(netlist, '_output_bus.v')
