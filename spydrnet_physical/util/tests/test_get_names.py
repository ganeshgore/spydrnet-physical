''' Tst cases fro get_names method '''
import unittest
from spydrnet import ir
from  spydrnet_physical.util import get_names
from  spydrnet_physical.util import get_attr



class TestGetNames(unittest.TestCase):
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
        self.assertEqual(["Cable0", ], get_names(self.cable))
        # Iterarable objects
        self.assertEqual(["Cable0", "Port0", "Definition0", "Instance0"],
                         get_names([self.cable, self.port,
                                    self.definition, self.instance]))
        # Genrator object
        self.assertEqual(["Port0", ],
                         get_names(self.definition.get_ports()))

    def test_get_attr(self):
        ''' Test correctness of retruned string '''
        # Single object
        self.assertEqual(["Cable0", ], get_names(self.cable))
        # Iterarable objects
        self.assertEqual(["Cable0", "Port0", "Definition0", "Instance0"],
                         get_attr([self.cable, self.port, self.definition,
                                   self.instance], 'name'))
