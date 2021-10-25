from spydrnet.ir.port import Port as PortBase


class Port(PortBase):
    ''' This class extends the default Port class '''

    @property
    def size(self):
        '''
        Returns number of pins in the port

        Returns:
            int: Returns size of port
        '''
        return super().size
