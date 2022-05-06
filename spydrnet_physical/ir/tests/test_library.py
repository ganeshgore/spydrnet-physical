import unittest

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.ir.library import Library
from spydrnet_physical.util import get_names


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist()
        self.library: Library = self.netlist.create_library("work")
        self.definition = self.library.create_definition("top")

    def test_create_top_wrapper(self):
        ''' Creates a simple top level verilog wrapper with default arguments

        - Validated the default name
        - Validates the name, inst_name, port_map
        '''
        self.netlist.top_instance = self.definition
        self.netlist.top_instance.name = "top"
        new_top = self.library.create_top_wrapper()
        self.assertIsInstance(new_top, sdn.Definition)
        self.assertEqual(new_top.name, "top_wrapper")
        self.assertEqual(self.netlist.top_instance.reference, new_top)
        self.assertEqual(set(get_names(new_top.get_instances())), {"top_1"})

    def test_create_top_wrapper__names(self):
        ''' Creates wrapper for top module  with new name and insta name

        - Validates the name, inst_name
        '''
        self.netlist.top_instance = self.definition
        self.netlist.top_instance.name = "top"
        new_top = self.library.create_top_wrapper("fpga_top",
                                                  inst_name="fpga_core")
        self.assertIsInstance(new_top, sdn.Definition)
        self.assertEqual(new_top.name, "fpga_top")
        self.assertEqual(self.netlist.top_instance.reference, new_top)
        self.assertEqual(set(get_names(new_top.get_instances())),
                         {"fpga_core"})

    def test_create_top_wrapper__pin_map(self):
        ''' Creates wrapper for top module  with new name and insta name

        - Validates the name, inst_name
        '''
        self.definition.create_cable("a", wires=2, is_downto=False).connect_port(
            self.definition.create_port(
                "a", direction=sdn.IN, pins=2, is_downto=False)
        )
        self.definition.create_cable("b", wires=3).connect_port(
            self.definition.create_port("b", direction=sdn.IN, pins=3)
        )
        self.definition.create_cable("cout", wires=1).connect_port(
            self.definition.create_port("cout", direction=sdn.OUT, pins=1)
        )
        self.netlist.top_instance = self.definition
        self.netlist.top_instance.name = "top"

        def portmap(x):
            return f"port_{x}"

        new_top = self.library.create_top_wrapper(port_map=portmap)
        self.assertIsInstance(new_top,  sdn.Definition,
                              msg="Return type is not definition")
        self.assertEqual(new_top.name, "top_wrapper",
                         msg="new definition name does not match with argument")
        self.assertEqual(self.netlist.top_instance.reference, new_top,
                         msg="New instance reference does not match")
        self.assertEqual(set(get_names(new_top.get_instances())), {"top_1"},
                         msg="new instance name does not match with argument")
        self.assertTupleEqual(tuple(get_names(new_top.get_ports())),
                              ("port_a", "port_b", "port_cout"),
                              msg="Pinname of new definition dont match")
        self.assertFalse(next(new_top.get_ports("port_a")).is_downto,
                         msg="Pinname of new definition dont match")
