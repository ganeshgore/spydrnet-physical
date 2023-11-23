#Copyright 2021
#Author Dallin Skouson
#see the license for details
#
#Tests the verilog composers functions and output

from collections import OrderedDict
import unittest
from unittest.case import expectedFailure
import spydrnet as sdn
from spydrnet.composers.verilog.composer import Composer
from collections import OrderedDict

class TestVerilogComposerUnit(unittest.TestCase):

    class TestFile:
        '''represents a file (has a write function for the composer)
        can be used as a drop in replacement for the composer file.write function
        saves all written stuff to a string'''
        def __init__(self):
            self.written = ""

        def write(self, text):
            self.written += text

        def clear(self):
            self.written = ""

        def compare(self, text, should_match = True):
            self.written = self.written.lstrip()
            if (text == self.written) == should_match:
                return True
            else:
                print("The composer wrote:")
                print('"' + self.written + '"')
                print("This was compared to:")
                print('"' + text + '"')
                if not should_match:
                    print("and these are not supposed to match")
                else:
                    print("and these should have matched")
                print("\n")
                return False


    def initialize_tests(self):
        composer = Composer()
        composer.file = self.TestFile()
        return composer

    def initialize_netlist(self):
        netlist = sdn.Netlist()
        netlist.name = "test_netlist"
        return netlist

    def initialize_library(self):
        netlist = self.initialize_netlist()
        library = netlist.create_library()
        library.name = "test_library"
        return library

    def initialize_definition(self):
        library = self.initialize_library()
        definition = library.create_definition()
        definition.name = "test_definition"
        return definition

    def initialize_instance_parameters(self, instance):
        instance["VERILOG.Parameters"] = OrderedDict()
        instance["VERILOG.Parameters"]["key"] = "value"
        instance["VERILOG.Parameters"]["key2"] = "value2"

        expected1 = ".key(value)"
        expected2 = ".key2(value2)"

        return expected1, expected2

    # def test_assignment_single_bit(self):
    #     composer = self.initialize_tests()
    #     definition = self.initialize_definition()

    #     cable1 = definition.create_cable(name = "left_cable", is_downto = False, wires=1)
    #     cable2 = definition.create_cable(name = "right_cable", is_downto = False, wires=1)

    #     instance = cable1.assign_cable(cable2, bitwise_assignment=True)
    #     composer._write_assignments(instance)
    #     assert composer.file.compare("assign %s = %s;\n" % (cable1.name, cable2.name))
