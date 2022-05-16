import re
import unittest
#import spydrnet as sdn
from spydrnet_physical.util import ConnectPoint

class test_ConnectPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.pt = ConnectPoint (2, 2, 2, 3, level= "up", color="black")

    def test_level(self):
        '''Test Correctness of clock connection level'''
        self.assertEqual(self.pt.level, "up")

    def test_connection(self):
        '''Test Correctness of the coordinates of a connection point'''
        self.assertEqual (self.pt.connection, (2,2,2,3))
    
    def test_full_connection(self):
        '''Test Correctness of the coordinates of a connection point along with 
        relative directions'''
        self.assertEqual (self.pt.full_connection, (2, 2, 2, 3, 'top', 'bottom'))  

    def test_from_connection(self):
        '''Test Correctness of starting connection point'''
        self.assertEqual (self.pt.from_connection, (2, 2))     

    def test_to_connection(self):
        '''Test Correctness of ending connection point'''
        self.assertEqual (self.pt.to_connection, (2, 3))   

    def test_distance(self):
        '''Test Correctness of distance between points'''
        self.assertEqual (self.pt.distance, 1)

    def test_color(self):
        '''Test the color of a connection point'''
        self.assertEqual (self.pt.color, "black")    

    def test_vertical_flip_connection(self):
        '''Test Correctness of the vertical fliping of a connection point'''
        self.pt.flip_connection('v')
        self.assertEqual (self.pt.connection, (2, -2, 2, -3)) 

    def test_horizontal_flip_connection(self):
        '''Test Correctness of the horizontal fliping of a connection point'''
        self.pt.flip_connection('h')
        self.assertEqual(self.pt.connection, (-2, 2, -2, 3)) 
    
    # what is size x and size y in rotate connection.
    def test_rotate_connection(self):
        '''Test Correctness of the rotation of a connection point (re-check)'''
        self.pt.rotate_connection(90, 1, 1)
        self.assertEqual(self.pt.connection, (0, 2, -1, 2))

    def test_translate_connection(self):
        '''Test Correctness of the translation of a connection point'''
        self.pt.translate_connection(1,1)
        self.assertEqual(self.pt.connection, (3, 3, 3, 4))

    def test_scale_connection(self):
        '''Test the scalibility of a connection point'''
        self.pt.scale_connection(3)
        self.assertEqual(self.pt.connection, (6, 6, 6, 9))

    
    def test_reverse_direction(self):
        ''' Test correctness of the reversing the direction of a connection point'''
        self.assertEqual(self.pt.direction(reverse=True), 'top' )

    def test_mul(self):
        ''' This test is returning None because the updated points 
        are saved in a variable that is a deep copy of the self  '''
        self.assertEqual(print(self.pt.__mul__(2)), None )

    #def test_rotate_point(self):
        



