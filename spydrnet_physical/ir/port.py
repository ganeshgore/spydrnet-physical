from spydrnet.ir.port import Port as PortBase


class Port(PortBase):
    ''' This class extends the default Port class '''

    @property
    def is_input(self):
        return self.direction == self.Direction.IN

    @property
    def is_output(self):
        return self.direction == self.Direction.OUT

    @property
    def is_inout(self):
        return self.direction == self.Direction.INOUT

    @property
    def size(self):
        '''
        Returns number of pins in the port

        Returns:
            int: Returns size of port
        '''
        return super().size

    def change_name(self, name):
        '''
        Change name of the port and corrosponding cable

        args:
            name (str): Name of the ports
        '''
        self.name = name
        for pin in self.pins:
            pin.wire.cable.name = name
