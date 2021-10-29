
import typing
from collections.abc import Iterable
from spydrnet.ir.instance import Instance as InstanceBase


if typing.TYPE_CHECKING:
    from spydrnet.ir.instance import Instance as InstanceSDN
    from spydrnet_physical.ir.first_class_element import FirstClassElement as FirstClassElementPhy
    InstanceBase = type(
        "InstanceBase", (InstanceSDN, FirstClassElementPhy), {})


class Instance(InstanceBase):
    ''' Extending base instance class '''

    def __init__(self, name=None, properties=None):
        super().__init__(name=name, properties=properties)
        properties = properties or dict()
        self.properties["LOC_X"] = properties.get("LOC_X", 0)
        self.properties["LOC_Y"] = properties.get("LOC_X", 0)

    def check_all_scalar_connections(self, port):
        '''
        Check if each wire connected to this port are single wire

        args:
            port (Port): Port of the instance
        '''
        assert self.reference == port.definition, \
            "Port does not belong to same definition"
        for pin in port.pins:
            if self.pins[pin].wire is None:
                return False
            if self._pins[pin].wire.cable.size > 1:
                return False
        return True

    def get_port_pins(self, ports):
        '''
        Returns all the outerpins of this port on this instance

        args:
            port (Port): Port of the instance
        '''
        if isinstance(ports, str):
            ports = self.reference.get_ports(ports)
        if not isinstance(ports, Iterable):
            ports = tuple(ports)
        return (self.pins[p] for port in ports for p in port.pins)

    def get_port_cables(self, ports):
        '''
        Return all outer cables connected to this port

        args:
            port (Port): Port of the instance
        '''
        cable_list = []
        for each in self.get_port_pins(ports):
            if each.wire:
                if not each.wire.cable in cable_list:
                    cable_list.append(each.wire.cable)
        return cable_list
