import unittest

import spydrnet as sdn
from spydrnet_physical.util import get_names


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist()
        self.library = self.netlist.create_library("work")
        self.definition = self.library.create_definition("top")

    def test_create_top_wrapper(self):
        ''' Creates wrapper for top module '''
        self.netlist.top_instance = self.definition
        self.netlist.top_instance.name = "top"
        new_top = self.library.create_top_wrapper()
        self.assertIsInstance(new_top, sdn.Definition)
        self.assertEqual(new_top.name, "top_wrapper")
        self.assertEqual(self.netlist.top_instance.reference, new_top)
        self.assertEqual(set(get_names(new_top.get_instances())), {"top_1"})
