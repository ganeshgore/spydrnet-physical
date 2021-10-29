import typing
from spydrnet.ir.outerpin import OuterPin as OuterPinBase


if typing.TYPE_CHECKING:
    from spydrnet.ir.outerpin import OuterPin as OuterPinSDN
    from spydrnet_physical.ir.pin import Pin as PinPhy
    OuterPinBase = type("OuterPinBase", (OuterPinSDN, PinPhy), {})


class OuterPin(OuterPinBase):
    ''' This class extends the default OuterPin class '''

    @property
    def port(self):
        '''Return the port that the inner pin is a part of.
        This object cannot be modified directly by the end user.'''

        return self._inner_pin._port

    @property
    def get_index(self):
        ''' Returns python index of element

        As outer pins do not have port associated with it
        the index is copied from corrosponding innerpins
        '''
        innerpin = self.inner_pin
        return innerpin._bundle().get_index(innerpin)
