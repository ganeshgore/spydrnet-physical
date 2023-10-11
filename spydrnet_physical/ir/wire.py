''' Example plugin to extend functionality '''
import typing
import spydrnet as sdn
from spydrnet.ir.wire import Wire as WireBase


if typing.TYPE_CHECKING:
    from spydrnet.ir.wire import Wire as WireSDN
    from spydrnet_physical.ir.element import Element as ElementPhy
    WireBase = type("WireBase", (WireSDN, ElementPhy), {})


class Wire(WireBase):
    ''' This class extends the default Wire class '''

    def _bundle(self):
        '''
        Overrides the _bundle method from element class
        '''
        return self._cable

    def index(self):
        """
        if this wire is in a cable, returns the index number of the wire in the parent cable, respects down_to and lower_index parameters
        """

        assert self.cable is not None, "Wire does not belong to any cable"
        assert self in self.cable.wires, "Decrepancy in cable and wire mapping"

        indx = self.cable.wires.index(self)
        size = self.cable.size-1
        if self.cable.is_downto:
            return (size-indx) + self.cable.lower_index
        else:
            return indx + self.cable.lower_index

    def get_driver(self):
        '''
        returns the driver(s) of the wire
        '''
        drivers = []
        for pin in self._pins:
            if pin.__class__ is sdn.InnerPin:
                if pin.port.direction is sdn.IN:
                    drivers.append(pin)
            else:
                if pin.inner_pin.port.direction is sdn.OUT:
                    drivers.append(pin)
        return drivers

    def assign_wire(self, wire, reverse=False, assign_instance_name=None):
        '''
        Perform single bit assignement of self to given wire
        '''
        assert self.cable is not None, "Wire do not have cable assigned"
        assign_lib = self.cable.definition._get_assignment_library()
        assign_def = self.cable.definition._get_assignment_definition(assign_lib, 1)
        if assign_instance_name is None:
            assign_instance_name = f"{self.cable.name}_{self.index()}_{wire.cable.name}_{wire.index()}_assign"
        instance = self.cable.definition.create_child(assign_instance_name, reference=assign_def)
        i_pin = next(instance.get_port_pins("i"))
        o_pin = next(instance.get_port_pins("o"))
        self.connect_pin(o_pin if reverse else i_pin )
        wire.connect_pin(i_pin if reverse else o_pin )
