import unittest
from spydrnet_physical.util import ConnectPoint , ConnectPointList, ConnectionPattern

class test_connectpointlist(unittest.TestCase):
        
    def test_merge(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_x()
        pts2 = ConnectPointList(5,5)
        pts2.cursor = (2,3)
        pts2.move_y()
        pts1.merge(pts2)
        point = pts1.search_from_point((2,3))
        self.assertEqual(point.connection, (2, 3, 2, 4)) 

    def test_add_connection(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_x()
        pts1.add_connection(2, 3, 2, 5)
        point = pts1.search_from_point((2,3))
        self.assertEqual(point.connection, (2, 3, 2, 5))    

    def test_add_connect_point(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_x()
        pt = ConnectPoint(2,3,2,4)
        pts1.add_connect_point(pt)
        point = pts1.search_from_point((2,3))
        self.assertEqual(point.connection, (2, 3, 2, 4))
        self.assertEqual(pts1.cursor, (2, 4))

    def test_add_next_point(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.add_next_point(5, 2)
        point = pts1.search_from_point((2,2))
        self.assertEqual(point.connection, (2, 2, 5, 2))

    def test_move_cursor_x(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_cursor_x (3)
        self.assertEqual(pts1.cursor, (5,2))

    def test_move_cursor_y(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_cursor_y (3)
        self.assertEqual(pts1.cursor, (2,5))    

    def test_move_x(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_x(2)
        point = pts1.search_to_point((4,2))
        self.assertEqual(point.connection, (2, 2, 4, 2))

    def test_move_x(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_x(2)
        point = pts1.search_to_point((4,2))
        self.assertEqual(point.connection, (2, 2, 4, 2))

    def test_move_y(self):
        pts1 = ConnectPointList(5, 5)
        pts1.cursor = (2,2)
        pts1.move_y(2)
        point = pts1.search_to_point((2,4))
        self.assertEqual(point.connection, (2, 2, 2, 4))

    def test_short_through(self):
         pts = ConnectPointList(5,5)
         pts.cursor = (2,2)
         pts.move_y(steps = 3)
         pts.short_through((2,3))
         point = pts.search_from_point((2,2)) 
         self.assertEqual(point.connection, (2,2,2,4))

    



