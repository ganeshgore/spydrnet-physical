import unittest

import spydrnet as sdn
from spydrnet_physical.util.get_names import get_names


class TestWire(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist()
        self.library = self.netlist.create_library()
        self.definition = self.library.create_definition()
        self.module1 = self.library.create_definition()
        self.cable = self.definition.create_cable()
        self.wire = self.cable.create_wire()
        self.instance = self.definition.create_child(reference=self.module1)

    def test_isload(self):
        ''' Checks connection sequence to port '''
        pin = self.module1.create_port(direction=sdn.OUT).create_pin()
        self.wire.connect_pin(pin)
        self.assertTrue(self.wire.isload(pin),
                        "Output Innerpin not detected as load")

        self.wire.connect_pin(self.instance.pins[pin])
        self.assertFalse(self.wire.isload(self.instance.pins[pin]),
                        "Output OuterPin detected as load")

        pin = self.module1.create_port(direction=sdn.IN).create_pin()
        self.wire.connect_pin(pin)
        self.assertFalse(self.wire.isload(pin),
                        "Input Innerpin detected as load")

        self.wire.connect_pin(self.instance.pins[pin])
        self.assertTrue(self.wire.isload(self.instance.pins[pin]),
                        "Input OuterPin not detected as load")


