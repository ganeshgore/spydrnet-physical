import unittest

import spydrnet as sdn
from spydrnet_physical.utils.get_names import get_names


class TestDefinition(unittest.TestCase):
    def setUp(self):
        self.netlist = sdn.Netlist("test_netlist")
        self.library = self.netlist.create_library("test_lib")
        self.definition = self.library.create_definition()

    def test_create_feedthroughs_ports(self):
        ''' Test feedthrough port creation '''
        cable = sdn.Cable("cable1")
        cable.create_wires(4)

        port1, port2 = self.definition.create_feedthroughs_ports(cable, "feed")
        self.assertIsInstance(port1, sdn.Port)
        self.assertIsInstance(port2, sdn.Port)
        self.assertSetEqual(set(get_names(self.definition.get_ports())),
                            {"cable1_feed_in", "cable1_feed_out"})
        self.assertSetEqual(set(get_names(self.definition.get_cables())),
                            {'cable1_feed_in', 'cable1_feed_out'})

    def test_create_feedthroughs_ports_2(self):
        ''' Test feedthrough port creation with lambda naming '''
        cable = sdn.Cable("cable1")
        cable.create_wires(4)
        def get_port_name(x): return "inport" if x is sdn.IN else "outport"
        port1, port2 = self.definition.create_feedthroughs_ports(
            cable,
            get_port_names=get_port_name)
        self.assertIsInstance(port1, sdn.Port)
        self.assertIsInstance(port2, sdn.Port)
        self.assertSetEqual(set(get_names(self.definition.get_ports())),
                            {"inport", "outport"})
