''' Example plugin to extend functionality '''
from spydrnet.ir.wire import Wire as WireBase


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