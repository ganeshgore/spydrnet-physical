import unittest

import spydrnet as sdn
from spydrnet_physical.util.get_names import get_names


class TestCable(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist()
        self.library = self.netlist.create_library()
        self.definition = self.library.create_definition()
        self.module1 = self.library.create_definition()
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

    def test_assign_cable(self):
        self.cable.create_wires(2)
        cable = self.definition.create_cable(wires=4)

        # Check straight connection
        assig_inst = self.cable.assign_cable(cable)
        self.assertIsInstance(assig_inst, sdn.Instance)
        self.assertSetEqual(set(get_names(assig_inst.get_ports())), {"i", "o"})
        get_pin = lambda pin: assig_inst.pins[pin].wire.get_index
        i_indx = [get_pin(pin) for pin in next(assig_inst.get_ports("i")).pins]
        o_indx = [get_pin(pin) for pin in next(assig_inst.get_ports("o")).pins]
        self.assertEqual(i_indx, [0, 1])
        self.assertEqual(o_indx, [0, 1])

        # Check assignment concat
        cable.name = "_0_"
        assig_inst = self.cable.assign_cable(cable, upper=2, lower=1)
        get_pin = lambda pin: assig_inst.pins[pin].wire.get_index
        i_indx = [get_pin(pin) for pin in next(assig_inst.get_ports("i")).pins]
        o_indx = [get_pin(pin) for pin in next(assig_inst.get_ports("o")).pins]
        self.assertEqual(i_indx, [0, 1])
        self.assertEqual(o_indx, [1, 2])

    def test_split(self):

        cable1 = self.definition.create_cable(name="in0",is_downto=True, is_scalar = False, lower_index = 0, wires=4)

        cable_list1 = [print(i.name) for i in self.definition.cables]  

        self.assertEqual(len(cable_list1), 2)

        cable1.split()

        cable_list2 = [print(i.name) for i in self.definition.cables]  

        self.assertEqual(len(cable_list2), 5)

    def test_check_concat(self):

        port1 = self.definition.create_port(name="in0", is_downto=True, is_scalar = False, lower_index = 0, direction=sdn.IN, pins=4)

        cable1 = self.definition.create_cable(name="in0",is_downto=True, is_scalar = False, lower_index = 0, wires=4)

        cable1.connect_port(port1)

        self.assertEqual(cable1.check_concat(), False)

        port2 = self.definition.create_port("io1", pins = 1)

        cable2 = self.definition.create_cable("io1",wires = 1)

        cable2.connect_port(port2)

        self.assertEqual(cable2.check_concat(), True)
    
    