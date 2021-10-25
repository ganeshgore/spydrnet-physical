''' Tst cases fro get_names method '''
import unittest
from spydrnet import ir
import spydrnet_physical as sdnphy


class TestPin(unittest.TestCase):
    ''' Test case class '''

    def setUp(self):
        ''' Basic element setup '''
        self.definition = ir.Definition(name="Definition0")
        self.cable = self.definition.create_cable(name="Cable0")
        self.port = self.definition.create_port(name="Port0")
        self.instance = ir.Instance(name="Instance0")

    def test_get_names(self):
        ''' Test correctness of retruned string '''
        # Single object
        self.assertEqual(["Cable0", ], sdnphy.get_names(self.cable))
        # Iterarable objects
        self.assertEqual(["Cable0", "Port0", "Definition0", "Instance0"],
                         sdnphy.get_names([self.cable, self.port,
                                           self.definition, self.instance]))
        # Genrator object
        self.assertEqual(["Port0", ],
                         sdnphy.get_names(self.definition.get_ports()))
