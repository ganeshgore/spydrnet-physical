''' Example plugin to extend functionality '''
import typing
from spydrnet.ir.pin import Pin as PinBase

if typing.TYPE_CHECKING:
    from spydrnet.ir.pin import Pin as PinSDN
    from spydrnet_physical.ir.element import ElementPhy
    PinBase = type("PinBase", (PinSDN, ElementPhy), {})


class Pin(PinBase):
    ''' This class extends the default Pin class '''

    def _bundle(self):
        '''
        Overrides the _bundle method from element class (returns port)
        '''
        return self.port

    @property
    def is_connected(self):
        ''' Checks if this pin is connected to any wire

        Checks for the connected wire if not found false
        '''
        return bool(self.wire)
