from spydrnet.ir.innerpin import InnerPin as InnerPinBase


class InnerPin(InnerPinBase):
    ''' This class extends the default InnerPin class '''

    def index(self):
        """if this wire is in a cable, returns the index number of the wire in the parent cable"""

        assert self._port is not None, "the wire does not belong to a cable"

        return self._port.pins.index(self)