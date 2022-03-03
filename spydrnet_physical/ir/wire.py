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
