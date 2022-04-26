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
        self.properties["SIDE"] = properties.get("SIDE", 'center')
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

    def split(self, get_name=None):
        get_name = get_name or (lambda x: f"{self.name}_{x}")
        self._pins[0].wire.cable.split(get_name)
        for indx, pin in enumerate(self._pins[::-1]):
            new_port = self.definition.create_port(get_name(indx),
                                                   direction=self.direction)
            self._pins.remove(pin)
            pin._port = None
            new_port.add_pin(pin)

        self.definition.remove_port(self)

    def change_name(self, name):
        '''
        Change name of the port and corrosponding cable

        args:
            name (str): Name of the ports
        '''
        self.name = name
        for pin in self.pins:
            pin.wire.cable.name = name
