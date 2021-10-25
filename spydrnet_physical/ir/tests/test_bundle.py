import unittest

import spydrnet as sdn
from spydrnet.ir import Bundle
from spydrnet.ir import FirstClassElement


class TestBundle(unittest.TestCase):
    def setUp(self) -> None:
        self.bundle = Bundle()

    def test_size(self):
        objects = [object, object, object]
        self.bundle._items = lambda : objects
        self.assertEqual(self.bundle.size, 3)

    def test_get_index(self):
        ''' Tests size propoerty of the bundle '''
        objects = [object, object, object]
        self.bundle._items = lambda : objects

        # is_downto = True
        self.bundle.is_downto = True
        self.assertEqual(self.bundle.get_index(objects[0]), 0)
        self.assertEqual(self.bundle.get_verilog_index(objects[0]), 2)
        self.bundle.lower_index = 1
        self.assertEqual(self.bundle.get_index(objects[0]), 0)
        self.assertEqual(self.bundle.get_verilog_index(objects[0]), 3)
        # is_downto = False
        self.bundle.is_downto = False
        self.assertEqual(self.bundle.get_index(objects[0]), 0)
        self.assertEqual(self.bundle.get_verilog_index(objects[0]), 1)
        self.bundle.lower_index = 0
        self.assertEqual(self.bundle.get_index(objects[0]), 0)
        self.assertEqual(self.bundle.get_verilog_index(objects[0]), 0)