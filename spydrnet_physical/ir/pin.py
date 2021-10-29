''' Example plugin to extend functionality '''
from spydrnet.ir.pin import Pin as PinBase


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
