import unittest

import spydrnet as sdn
from spydrnet.ir import Bundle


class TestPort(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist("test_netlist")
        self.library = self.netlist.create_library("test_lib")
        self.definition = self.library.create_definition()

    def test_size(self):
        port = self.definition.create_port(name="in0", is_downto=True, is_scalar = False, lower_index = 0, direction=sdn.IN, pins=4)
        self.assertEqual(port.size, 4)

    def test_change_name(self):
        port = self.definition.create_port(name="in0", pins = 1)
        cable = self.definition.create_cable(name="in0", wires=1)
        cable.connect_port(port)
        self.assertEqual(port.name, "in0")
        self.assertEqual(cable.name, "in0")
        port.change_name("in2")
        self.assertEqual(port.name, "in2")
        self.assertEqual(cable.name, "in2")
