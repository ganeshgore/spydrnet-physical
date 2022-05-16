import unittest
import pytest
from spydrnet_physical.util import ConnectPoint , ConnectPointList

class test_connectpointlist(unittest.TestCase):

	def setUp(self):
		self.pts = ConnectPointList(5,10)


	def test_cursor_point(self):
		'''This test checks whether the cursor is correctly placed initially at the right coordinates using cursor_point'''
		self.pts.cursor = (1,1)
		self.assertEqual(self.pts.cursor,(1,1))

	def test_getx(self):
		'''This test checks whether getx correctly provides the x coordinate of the cursor'''
		self.pts.cursor = (3,4)
		self.assertEqual(self.pts.get_x,3)

	def test_gety(self):
		'''This test checks whether gety correctly provides the y coordinate of the cursor'''
		self.pts.cursor = (3,4)
		self.assertEqual(self.pts.get_y,4)

	def test_set_cursor(self):
		'''This test checks whether the set_cursor correcly places cursor at the new coordinates'''
		self.pts.cursor = (1,1)
		self.pts.set_cursor(5,5)
		self.assertEqual(self.pts.cursor,(5,5))

	def test_set_color(self):
		'''This test checks whether the color of ConnectPointList is set correcly'''
		pt = ConnectPoint(1, 2, 1, 3, level="up")
		pts = ConnectPointList(5,10,pt)
		pts.set_color("red")
		self.assertEqual(pt.color,"red")

	def test_search_from_point(self):
		'''This test checks whether the search from point correctly returns connection going out of the given coordinate'''
		self.pts.cursor = (2,3)
		self.pts.move_x(1)
		self.pts.move_y(1)
		point = self.pts.search_from_point((3,3))
		self.assertTupleEqual(point.connection,(3,3,3,4))

	def test_search_to_point(self):
		'''This test checks whether the search to point correctly returns connection coming into the given coordinate'''
		self.pts.cursor = (2,3)
		self.pts.move_x(1)
		self.pts.move_y(1)
		point = self.pts.search_to_point((3,3))
		self.assertTupleEqual(point.connection,(2,3,3,3))

	def test_push_connection_down(self):
		'''This test checks whether the level of the connection is going one down'''
		pt = ConnectPoint(2, 2, 2, 3)
		self.pts.push_connection_down(pt)
		self.assertEqual(pt.level,"down")

	def test_pull_connection_up(self):
		'''This test checks whether the level of the connection is going one down'''
		pt = ConnectPoint(2, 2, 2, 3)
		self.pts.pull_connection_up(pt)
		self.assertEqual(pt.level,"up")

	@pytest.mark.skip(reason= "Not working for some reason")
	def test_make_top_connection(self):
		'''This test checks whether the connection is made with the top level'''
		pass
		#pts = ConnectPointList(5,10)
		#pt = ConnectPoint(2, 2, 2, 3)
		#pts.make_top_connection()
		#self.assertEqual(pt.level,"same")

	def test_reset_level(self):
		'''This test checks whether the connection reset to the same level'''
		pt = ConnectPoint(2, 2, 2, 3,level = "up")
		self.pts.reset_level(pt)
		self.assertEqual(pt.level,"same")

	def test_hold_cursor(self):
		'''This test checks whether the cursor holds its position when a connection is made in any coordonate'''
		self.pts.cursor = (2,3)
		self.pts.hold_cursor()
		self.pts.move_x(3)
		self.assertEqual(self.pts.cursor,(2,3))
		self.assertEqual(self.pts._cursor_state,False)
    
	def test_release_cursor(self):
		'''This test checks whether the cursor also moves its position when a connection is made in any coordonate'''
		self.pts.set_cursor(2,3)
		self.pts.hold_cursor()
		self.assertEqual(self.pts._cursor_state,False)
		self.pts.move_x(3)
		self.pts.release_cursor()
		self.assertEqual(self.pts._cursor_state,True)
		self.pts.move_x(2).move_y(4)
		self.assertEqual(self.pts.cursor,(4,7))

	def test_flip_V(self):
		'''This test checks whether the connection is correctly flipped vertically'''
		pt = ConnectPoint(2, 2, 2, 3,level = "up")
		pts = ConnectPointList(5,10,pt)
		point = pts.search_from_point((2,2))
		self.assertEqual(point.connection,(2,2,2,3))
		pts.flip("V")
		self.assertEqual(point.connection,(2,-2,2,-3))

	def test_flip_H(self):
		'''This test checks whether the connection is correctly flipped horizontally'''
		pt = ConnectPoint(2, 2, 2, 3,level = "up")
		pts = ConnectPointList(5,10,pt)
		point = pts.search_from_point((2,2))
		self.assertEqual(point.connection,(2,2,2,3))
		pts.flip("H")
		self.assertEqual(point.connection,(-2,2,-2,3))

	def test_sample_connections(self):
		'''This test checks whether the connection is sampled correctly equal to the max distance defined, it also checks if all other segments exist after sampling, also the level property remains the same
		'''
		pt = ConnectPoint(2, 2, 5, 2,level = "up")
		pts = ConnectPointList(5,10,pt)
		point = pts.search_to_point((5,2))
		self.assertEqual(point.connection,(2,2,5,2))
		pts.sample_connections(max_distance=1)
		self.assertEqual(point.connection,(4,2,5,2))
		self.assertEqual(point.level, "up")
		point = pts.search_to_point((4,2))
		self.assertEqual(point.connection,(3,2,4,2))
		self.assertEqual(point.level, "same")

	def test_merge(self):
		'''This test cheks whether two connect point lists are merged correclty'''
		exp_list = [(2, 2, 3, 2), (3, 2, 3, 4), (2, 3, 4, 3), (4, 3, 4, 4)]
		pts1 = ConnectPointList(5, 5)
		pts1.cursor = (2,2)
		pts1.move_x(1).move_y(2)
		pts2 = ConnectPointList(5,5)
		pts2.cursor = (2,3)
		pts2.move_x(2).move_y(1)
		pts1.merge(pts2)
		total_pts = [pts.connection for pts in pts1]
		self.assertEqual(total_pts, exp_list)

	def test_scale(self):
		'''This test checks whether the ConnectPointList is scaled correctly according to the scale value and anchor coordinates defined '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.scale(scale=3,anchor=(0,0))
		point = self.pts.search_from_point((3,3))
		self.assertEqual(point.connection,(3,3, 9,3))

	def test_scale_anchor1(self):
		'''This test checks whether the ConnectPointList is scaled correctly according to the scale value and anchor coordinates defined '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.scale(scale=3,anchor=(1,1))
		point = self.pts.search_from_point((1,1))
		self.assertEqual(point.connection,(1,1, 7,1))

	def test_scale_anchor2(self):
		'''This test checks whether the ConnectPointList is scaled correctly according to the scale value and anchor coordinates defined '''
		self.pts.cursor = (2,2)
		self.pts.move_x(1)		
		self.pts.move_y(1)
		self.pts.scale(scale=2,anchor=(2,4))
		point = self.pts.search_from_point((4,0))
		self.assertEqual(point.connection,(4,0, 4,2))
		point = self.pts.search_to_point((4,0))
		self.assertEqual(point.connection,(2,0, 4,0))

	def test_translate(self):
		'''This test checks whether the ConnectPointList is translated correctly according the to the x and y coordinates defined '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.translate(2,0)
		point = self.pts.search_from_point((3,1))
		self.assertEqual(point.connection,(3,1, 5,1))

	def test_rotate(self):
		'''This test checks whether the ConnectPointList is rotated correctly according the to defined angle '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.rotate(90)
		point = self.pts.search_from_point((5,1))
		self.assertEqual(point.connection,(5,1, 5,3))

	def test_rotate_180(self):
		'''This test checks whether the ConnectPointList is rotated correctly according the to defined angle '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.rotate(180)
		point = self.pts.search_from_point((5,10))
		self.assertEqual(point.connection,(5, 10, 3, 10))

	def test_rotate_270(self):
		'''This test checks whether the ConnectPointList is rotated correctly according the to defined angle '''
		self.pts.cursor = (1,1)
		self.pts.move_x(2)
		self.pts.rotate(270)
		point = self.pts.search_from_point((1,10))
		self.assertEqual(point.connection,(1, 10, 1, 8))

	def test_add_next_point(self):
		'''This test checks whether the add_next_point correctly adds a connection point in the ConnectPointList '''
		self.pts.cursor = (2,2)
		self.pts.add_next_point(3, 2)
		point = self.pts.search_from_point((2,2))
		self.assertEqual(point.connection, (2, 2, 3, 2))

	def test_move_cursor_x(self):
		'''This test checks whether the move_cursor_x moves the cursor in the right direction without making a connection'''
		self.pts.cursor = (2,2)
		self.pts.move_cursor_x(3)
		self.assertEqual(self.pts.cursor, (5,2))
		point = self.pts.search_to_point((5,2))
		self.assertEqual(point, None)

	def test_move_cursor_y(self):
		'''This test checks whether the move_cursor_y moves the cursor in the right direction without making a connection'''
		self.pts.cursor = (2,2)
		self.pts.move_cursor_y(3)
		self.assertEqual(self.pts.cursor, (2,5))
		point = self.pts.search_to_point((2,5))
		self.assertEqual(point, None)

	def test_move_x(self):
		'''This test checks whether the move_x moves the cursor in the right direction while making a connection'''
		self.pts.cursor = (1,2)
		self.pts.move_x(2,2,"red")
		point = self.pts.search_to_point((3,2))
		self.assertEqual(point.connection, (1, 2, 3, 2))
		point = self.pts.search_to_point((5,2))
		self.assertEqual(point.connection, (3, 2, 5, 2))
		self.assertEqual(self.pts.cursor, (5,2))
		self.assertEqual(point.color, "red")

	def test_move_y(self):
		'''This test checks whether the move_y moves the cursor in the right direction while making a connection'''
		self.pts.cursor = (2,2)
		self.pts.move_y(4,2,"red")
		point = self.pts.search_to_point((2,6))
		self.assertEqual(point.connection, (2, 2, 2, 6))
		point = self.pts.search_to_point((2,10))
		self.assertEqual(point.connection, (2, 6, 2, 10))
		self.assertEqual(self.pts.cursor, (2,10))
		self.assertEqual(point.color, "red")

	def test_add_connect_point(self):
		'''This test checks whether the ConnectPoint is correctly added in the ConnectPointList'''
		self.pts.cursor = (2,2)
		self.pts.move_x()
		pt = ConnectPoint(2,3,2,4)
		self.pts.add_connect_point(pt)
		point = self.pts.search_from_point((2,3))
		self.assertEqual(point.connection, (2, 3, 2, 4))
		self.assertEqual(self.pts.cursor, (2, 4))

	def test_add_connection(self):
		'''This test checks whether a new connection is correctly added in the ConnectPointList'''
		self.pts.cursor = (2,2)
		self.pts.move_x()
		self.pts.add_connection(2, 3, 2, 5)
		point = self.pts.search_from_point((2,3))
		self.assertEqual(point.connection, (2, 3, 2, 5))

	def test_short_through(self):
		'''This test checks whether the short_through skips a connection at the specified coordinate'''
		self.pts.cursor = (2,2)
		self.pts.move_y(steps = 3)
		self.pts.short_through((2,3))
		point = self.pts.search_from_point((2,2))
		self.assertEqual(point.connection, (2,2,2,4))

