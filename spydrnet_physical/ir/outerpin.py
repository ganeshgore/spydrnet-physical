from spydrnet.ir.outerpin import OuterPin as OuterPinBase


class OuterPin(OuterPinBase):
    ''' This class extends the default OuterPin class '''

    @property
    def port(self):
        '''Return the port that the inner pin is a part of.
        This object cannot be modified directly by the end user.'''

        return self._inner_pin._port