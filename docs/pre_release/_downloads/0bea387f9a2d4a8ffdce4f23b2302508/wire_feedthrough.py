"""
===========================================
Generating feedthrough from single instance
===========================================

This example demostrates how to generate a feedthrough wire connection for
a given scalar or vector wires.

**Initial Design**

.. image:: ../auto_sample_verilog/basic_hierarchy.svg
    :align: center


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

import spydrnet as sdn
import spydrnet_physical as sdnphy

netlist = sdnphy.load_netlist_by_name("basic_hierarchy")

top = netlist.top_instance.reference
cable0 = next(top.get_cables("in3"))
inst2 = next(top.get_instances("inst_1_0"))


top.create_feedthrough(inst2, cable0)
top.create_unconn_wires()
sdn.compose(netlist, "_output_wire.v", skip_constraints=True)


# Reset design
netlist = sdnphy.load_netlist_by_name("basic_hierarchy")

top = netlist.top_instance.reference
bus_in = next(top.get_cables("bus_in"))
inst1 = next(top.get_instances("inst_2_0"))

cables = top.create_feedthrough(inst1, bus_in)
top.create_unconn_wires()
sdn.compose(netlist, "_output_bus.v", skip_constraints=True)
