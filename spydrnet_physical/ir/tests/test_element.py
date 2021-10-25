import unittest

from spydrnet.ir import Element, Bundle


class TestElement(unittest.TestCase):

    def setUp(self) -> None:
        ''' Test setup '''
        self.element = Element()

    def test_index(self):
        ''' test get_index and get_verilog_index methods '''
        bundle = Bundle()
        bundle._items = lambda : [self.element, Element(), Element()]
        self.assertIsInstance(bundle._items()[0], Element)
        self.element._bundle = lambda : bundle
        self.assertIsInstance(self.element._bundle(), Bundle)
        self.assertEqual(self.element._bundle(), bundle)
        self.assertEqual(bundle._items()[0].get_index, 0)
        self.assertEqual(bundle._items()[0].get_verilog_index, 2)
