"""
=========================
Merging one or more ports
=========================

This example demonstrate how to merge two instance in the design to create a new
merged definition

"""

import spydrnet as sdn
from spydrnet_physical.util import get_names
from itertools import chain

with open("_temp_merge_ports.v", "w", encoding="UTF-8") as tmp:
    tmp.write(
        """
    module top();
        wire [4:0] mode;

        module1 inst1 (.wire1(mode[4]), .wire2(mode[3]), .wire3(mode[2:0]));
    endmodule

    module module1(wire1, wire2, wire3);
        input wire1;
        input wire2;
        input [2:0]wire3;

    endmodule
    """
    )


def merge_ports(self, new_port_name, port_sequence, reverse=False):
    new_port = self.create_port(new_port_name)
    new_cable = self.create_cable(new_port_name)

    for port in list(port_sequence):
        print(f"Adding wires from {port.name}")
        for pin in list(port.pins):
            wire = pin.wire
            port._pins.remove(pin)
            pin._port = None
            new_port.add_pin(pin)

            wire._cable = None
            new_cable.add_wire(wire)
        self.remove_cable(next(self.get_cables(port.name)))
        self.remove_port(port)
        print(f"Total pins {len(new_port.pins)}")
        print(f"Total wires  {len(new_port.pins)}")
        new_port.direction = port.direction

    return new_port


netlist = sdn.parse("_temp_merge_ports.v")
top = netlist.top_instance
module = next(netlist.get_definitions("top"))
module1 = next(netlist.get_definitions("module1"))
print(get_names(module1.get_ports()))
merge_ports(module1,
    "merged_port",
    chain(
        module1.get_ports("wire3*"),
        module1.get_ports("wire2*"),
        module1.get_ports("wire1*"),
    ),
)
print(get_names(module1.get_ports()))

sdn.compose(
    netlist, "_temp_merge_ports_rewrite.v", skip_constraints=True, write_blackbox=False
)
