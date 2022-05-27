''' Tst cases fro get_names method '''
import unittest
import spydrnet as sdn
from spydrnet_physical.util import initial_placement


class Test_initial_placement(unittest.TestCase):
    ''' Test case class '''

    def setUp(self):
        ''' Basic element setup '''
        self.netlist = sdn.Netlist("test_netlist")
        self.library = self.netlist.create_library("test_lib")
        self.definition = self.library.create_definition()
        self.netlist.top_instance = self.definition
        self.placement = initial_placement((4, 4), self.netlist, None)

    def test__init__(self):
        """
        Check general initialization parameters
        """
        self.assertEqual(self.placement.sizeX, 4)
        self.assertEqual(self.placement.sizeY, 4)

    def test_add_clb(self):
        '''
        '''
        self.placement.CLB_W, self.placement.CLB_H = 40, 30
        self.placement.CLB_GRID_X, self.placement.CLB_GRID_Y = 75, 85
        data = self.placement.add_clb(0, 0, "my_clb", 'clb')
        self.assertEqual(data["name"], "my_clb_1__1_")
        self.assertEqual(data["short_name"], "clb_1_1")
