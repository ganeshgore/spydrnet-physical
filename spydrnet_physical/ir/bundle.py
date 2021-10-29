import typing

from spydrnet.ir import Bundle as BundleBase

if typing.TYPE_CHECKING:
    from spydrnet.ir import Bundle as BundleSDN
    from spydrnet_physical.ir.first_class_element import \
        FirstClassElement as FirstClassElementPhy
    BundleBase = type(
        "BundleBase", (BundleSDN, FirstClassElementPhy), {})


class Bundle(BundleBase):
    ''' This class extends the default Bundle class '''

    @property
    def size(self) -> int:
        ''' Returns size of the bundle '''
        return len(self._items())

    def get_index(self, element):
        ''' Returns the python index of element '''
        return self._items().index(element)

    def get_verilog_index(self, element):
        ''' Returns the verilog index of element '''
        indx = self._items().index(element)
        if self.is_downto:
            return (self.size-indx-1) + self.lower_index
        else:
            return indx + self.lower_index
