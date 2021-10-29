''' Example plugin to extend functionality '''
import typing
from spydrnet.ir.cable import Cable as CableBase
from spydrnet.ir import Port, InnerPin, OuterPin


if typing.TYPE_CHECKING:
    from spydrnet.ir.cable import Cable as CableSDN
    from spydrnet_physical.ir.bundle import Bundle as BundlePhy
    CableBase = type("BundleBase", (CableSDN, BundlePhy), {})


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
            if reverse:
                wire.connect_pin(port.pins[wire.index()])
            else:
                wire.connect_pin(port.pins[-(wire.index()+1)])

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

    def assign_cable(self, cable: 'Cable', upper=None, lower=None):
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
            assign_lib, self.size)
        instance = self.definition.create_child(f"{self.name}_{cable.name}_assign",
                                                reference=assign_def)

        self.connect_instance_port(instance, next(assign_def.get_ports("i")))

        print(f"upper {upper}")
        print(f"lower {lower}")
        for indx, pin in enumerate(next(assign_def.get_ports("o")).pins):
            cable.wires[range(lower, upper+1)[indx]
                        ].connect_pin(instance.pins[pin])
        return instance
