import unittest

import spydrnet as sdn


class TestInnerPin(unittest.TestCase):
    def setUp(self) -> None:
        self.definition = sdn.Definition("top")
        self.module = sdn.Definition("module1")
        self.pin = sdn.InnerPin()

    #def test_get_index(self):
    #    port = self.definition.create_port(pins = 4)
    #    self.assertEqual(port.pins[1], sdn.InnerPin)
