import unittest

import spydrnet as sdn
from spydrnet.ir import pin


class TestCable(unittest.TestCase):
    def setUp(self) -> None:
        self.definition = sdn.Definition()
        self.module1 = sdn.Definition()
        self.cable = self.definition.create_cable()

    def test_connect_port(self):
        ''' Checks connection sequence to port '''
        port = self.definition.create_port(name="p0", direction=sdn.IN, pins=4)
        wire = self.cable.create_wires(4)
        self.assertIsNone(self.cable.connect_port(port))
        self.assertTrue(port.pins[0].wire is wire[0])
        self.assertTrue(port.pins[1].wire is wire[1])
        self.assertTrue(port.pins[2].wire is wire[2])
        self.assertTrue(port.pins[3].wire is wire[3])

    def test_connect_instance_port(self):
        ''' Checks connection sequence to the instance port '''
        top = sdn.Definition(name="top")
        module = sdn.Definition(name="module1")
        port = module.create_port(name="p0",
                                  direction=sdn.Port.Direction.IN,
                                  is_downto=False)
        port.create_pins(4)
        inst1 = top.create_child(name="inst1", reference=module)

        w = self.cable.create_wires(4)
        self.assertIsNone(self.cable.connect_instance_port(inst1, port))
        self.assertEqual(inst1.pins[port.pins[0]].wire, w[0])
        self.assertEqual(inst1.pins[port.pins[1]].wire, w[1])
        self.assertEqual(inst1.pins[port.pins[2]].wire, w[2])
        self.assertEqual(inst1.pins[port.pins[3]].wire, w[3])

    def test_is_port_cable(self):
        ''' Checks if the cable is connected to the Port-InnerConnection'''
        self.cable.create_wires(wire_count=4)
        self.assertFalse(self.cable.is_port_cable, "No connections")

        port = self.module1.create_port(pins=4)
        instance = self.definition.create_child(reference=self.module1)
        self.cable.connect_instance_port(instance, port)
        self.assertFalse(self.cable.is_port_cable, "Only instance connection")

        port = self.definition.create_port(pins=4)
        self.cable.connect_port(port)
        self.assertTrue(self.cable.is_port_cable, "Port connection")