''' Example plugin to extend functionality '''
from spydrnet.ir.cable import Cable as CableBase
from spydrnet.ir import Port, InnerPin, OuterPin


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
            if port.is_downto:
                wire.connect_pin(instance.pins[port.pins[wire.index()]])
            else:
                wire.connect_pin(instance.pins[port.pins[-(wire.index()+1)]])
