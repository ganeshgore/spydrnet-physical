from spydrnet.ir import Bundle as BundleBase


class Bundle(BundleBase):
    ''' This class extends the default Bundle class '''

    @property
    def size(self) -> int:
        ''' Returns size of the bundle '''
        return len(self._items())
