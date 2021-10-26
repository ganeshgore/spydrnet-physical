import unittest

import spydrnet as sdn


class TestOuterPin(unittest.TestCase):
    def setUp(self) -> None:
        self.definition = sdn.Definition("top")
        self.module = sdn.Definition("module1")
        self.pin = sdn.OuterPin()

    def test_get_index(self):
        ''' tests get_index property of outerpin '''
        port = self.module.create_port(pins=4)
        instance = self.definition.create_child(reference=self.module)
        self.assertIsInstance(instance.pins[port.pins[1]],sdn.OuterPin)
        self.assertEqual(instance.pins[port.pins[1]].get_index, 1)
