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
        cable = self.definition.create_cable("cable1", wires=4)

        port1, port2 = self.definition.create_feedthroughs_ports(cable, "feed")
        self.assertIsInstance(port1, sdn.Port)
        self.assertIsInstance(port2, sdn.Port)
        self.assertSetEqual(set(get_names(self.definition.get_ports())),
                            {"cable1_feed_in", "cable1_feed_out"})

