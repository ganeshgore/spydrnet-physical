''' Example plugin to extend functionality '''
import typing
import logging
from spydrnet.ir.cable import Cable as CableBase
from spydrnet.ir import Port, InnerPin, OuterPin


if typing.TYPE_CHECKING:
    from spydrnet.ir.cable import Cable as CableSDN
    from spydrnet_physical.ir.bundle import Bundle as BundlePhy
    CableBase = type("BundleBase", (CableSDN, BundlePhy), {})

logger = logging.getLogger("spydrnet_logs")

class Cable(CableBase):
    ''' This class extends the default Cable class '''

    @property
    def size(self):
        '''
        Returns number of wires in the cable

        Returns:
            int: Returns size of cable
        '''
        return super().size

    @property
    def is_port_cable(self):
        '''
        Checks if the wire is connected to any definition port (InnerConnection)

        returns:
            bool: true if wire belongs to definition port
        '''
        return any(isinstance(pin, InnerPin) for wire in self._wires for pin in wire.pins)

    def connect_port(self, port, reverse=False):
        '''
        Connects cable to the port of definition.

        This is internal connection to the InnerPins of the definition

        args:
            port (Port): Port to connect
        '''
        assert self in port.definition.cables, \
            "Cable and Port does not belong to same definition"
        assert isinstance(
            port, Port), "Argument to connect_port should be port"
        assert port.size, "Port has no pins"

        for wire in self.wires:
            if self.is_downto:
                wire.connect_pin(port.pins[-(wire.index()+1)])
            else:
                wire.connect_pin(port.pins[wire.index()])

    def connect_instance_port(self, instance, port):
        '''
        Connects cable to the port of the given instance.

        args:
            instance (Instance): Instance to consider
            port (Port): Port to connect
        '''
        assert isinstance(port, Port), \
            "Argument to connect_port should be port"
        assert port.size, "Port has no pins"
        assert port.size == self.size, "Port and cable size do not match"
        assert port in instance.reference.ports, \
            "Port %s in not part of instance definition %s" % \
            (port.name, instance.reference.name)
        for wire in self.wires:
            wire.connect_pin(instance.pins[port.pins[wire.get_index]])

    def assign_cable(self, cable: 'Cable', upper=None, lower=None, reverse=False,
        assign_instance_name=None, bitwise_assignment=False):
        ''' Create assignment beetween self and provided cable

        assign self = cable[upper:lower]
        '''
        assert isinstance(
            cable, Cable), "Cable can be assigned to another cable"
        assert self.definition is cable.definition, \
            "Cables belongs to two differnt definitions"
        assert self.definition is cable.definition, \
            "Cables belongs to differnt definitions"

        upper = upper or (self.size if self.is_downto else 0)
        lower = lower or (0 if self.is_downto else self.size)

        assign_lib = self.definition._get_assignment_library()
        assign_def = self.definition._get_assignment_definition(
            assign_lib, 1 if bitwise_assignment else self.size)
        if bitwise_assignment:
            instances = []
            for indx, wire1 in enumerate(self.wires):
                if self.is_downto == cable.is_downto:
                    wire2 = cable.wires[indx+lower]
                else:
                    wire2 = cable.wires[-1*(indx+lower+1)]
                instance = self.definition.create_child(
                    (assign_instance_name or f"{self.name}_{cable.name}_assign") + f"_{indx}",
                    reference=assign_def)
                i_pin = next(instance.get_port_pins("i"))
                o_pin = next(instance.get_port_pins("o"))
                wire1.connect_pin(o_pin if reverse else i_pin )
                wire2.connect_pin(i_pin if reverse else o_pin )
            return instances
        else:
            assert self.is_downto == cable.is_downto, \
                "Can not assign little endian to big endian wire " + \
                f"{self.name} is {self.is_downto} and {cable.name} is {cable.is_downto}"
            instance = self.definition.create_child(
                assign_instance_name or f"{self.name}_{cable.name}_assign",
                reference=assign_def)
            in_port = next(assign_def.get_ports("o" if reverse else "i"))
            self.connect_instance_port(instance, in_port)

            out_port = next(assign_def.get_ports("i" if reverse else "o"))
            for indx, pin in enumerate(out_port.pins):
                cable.wires[range(lower, upper+1)[indx]
                            ].connect_pin(instance.pins[pin])
            return instance

    def split(self, get_name=None):
        get_name = get_name or (lambda x: f"{self.name}_{x}")
        for indx, wire in enumerate(self._wires[::-1]):
            new_cable = self.definition.create_cable(get_name(indx))
            self.remove_wire(wire)
            new_cable.add_wire(wire)
        self.definition.remove_cable(self)

    def check_concat(self):
        """ This fucntion check if the cable is concatenated while connecting to other ports
        """
        assert self.size, "Cable does not contain any wires"

        connectedPorts = len(self._wires[0].pins)
        for wire in self._wires:
            if not connectedPorts == len(wire.pins):
                return False
            for pin in wire.pins:
                if isinstance(pin, InnerPin):
                    if not pin.port.size == self.size:
                        return False
                    if not pin.index() == wire.index():
                        return False
                else:
                    if not pin.inner_pin.port.size == self.size:
                        return False
                    if not pin.inner_pin.index() == wire.index():
                        return False

        return True
