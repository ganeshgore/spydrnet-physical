import unittest

import spydrnet as sdn


class TestWire(unittest.TestCase):
    def setUp(self) -> None:
        self.netlist = sdn.Netlist()
