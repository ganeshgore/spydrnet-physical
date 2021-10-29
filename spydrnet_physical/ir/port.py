import typing
from spydrnet.ir.port import Port as PortBase


if typing.TYPE_CHECKING:
    from spydrnet.ir.port import Port as PortSDN
    from spydrnet_physical.ir.bundle import Bundle as BundlePhy
    PortBase = type("PortBase", (PortSDN, BundlePhy), {})


class Port(PortBase):
    ''' This class extends the default Port class '''

    def __init__(self, name=None, properties=None, is_downto=None,
                 is_scalar=None, lower_index=None, direction=None):
        super().__init__(name=name, properties=properties, is_downto=is_downto,
                         is_scalar=is_scalar, lower_index=lower_index, direction=direction)
        properties = properties or dict()
        self.properties["SIDE"] = properties.get("SIDE", "")
        self.properties["OFFSET"] = properties.get("OFFSET", 0)

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
