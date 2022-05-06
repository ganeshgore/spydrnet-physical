import unittest

import spydrnet as sdn


class TestInnerPin(unittest.TestCase):
    def setUp(self) -> None:
        self.definition = sdn.Definition("top")
        self.module = sdn.Definition("module1")
        self.pin = sdn.InnerPin()
