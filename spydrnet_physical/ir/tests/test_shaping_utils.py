
"""
"""
import unittest
from spydrnet_physical.ir.shaping_utils import shaping_utils


class Test_shaping_utils(unittest.TestCase):
    ''' Test case class '''

    def test_convert_to_shape(self):
        '''
        Check if two 
        '''
        points = [(90, 210), (130, 170), (50, 170), (170, 170), (50, 250),
                  (90, 170), (90, 250), (130, 210), (50, 210), (170, 210)]
        shape, outline = shaping_utils._get_shapes_outline(points)
        self.assertEqual(shape, "custom")
        self.assertListEqual(outline, [(50, 170), (170, 170), (170, 210),
                                       (90, 210), (90, 250), (50, 250),
                                       (50, 170)])

    def test_points_to_path(self):
        points = [(50, 170), (170, 170), (170, 210),
                  (90, 210), (90, 250), (50, 250),
                  (50, 170)]
        path = shaping_utils._points_to_path(points)
        self.assertEqual(path, "H 0 0 120 40 -80 40 -40 -80")
