"""
==========================================
Genrating feedthrough from single instance
==========================================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.


.. hdl-diagram:: ../../../../examples/basic/_output_wire.v
   :type: netlistsvg
   :align: center


"""

from os import path
import spydrnet as sdn
import spydrnet_physical as sdnphy

netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

top = netlist.top_instance.reference
cable0 = next(top.get_cables("wire0"))
inst2 = next(top.get_instances("inst_2_1"))

top.create_feedthrough(inst2, cable0)
sdn.compose(netlist, '_output_wire.v')


# bus_in = next(top.get_cables("bus_in"))
# inst1 = next(top.get_instances("inst_1_0"))

# top.create_feedthrough(inst1, bus_in)
# sdn.compose(netlist, '_output_bus.v')
