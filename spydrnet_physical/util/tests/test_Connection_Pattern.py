"""
Unit tests for the ConnectionPattern class from the spydrnet_physical.util module.

This test suite includes the following tests:
- test_get_htree: Verifies the creation of an H-Tree pattern.
- test_get_htree_2n: Verifies the creation of an H-Tree pattern with different dimensions.
- test_get_htree_root: Verifies the creation of an H-Tree pattern with a specified root.
- test_get_htree_side: Verifies the creation of an H-Tree pattern with a specified side.
- test_get_htree_repeat: Verifies the creation of a repeated H-Tree pattern.
- test_get_fishbone: Placeholder for testing the creation of a Fishbone pattern (not implemented).
- test_get_fishbone_margin_x: Placeholder for testing the creation of a Fishbone pattern with x-axis margins (not implemented).
- test_get_fishbone_margin_y: Placeholder for testing the creation of a Fishbone pattern with y-axis margins (not implemented).

Each test initializes a ConnectionPattern object with specified dimensions and verifies the generated connection points against expected values.
"""

import unittest
from spydrnet_physical.util import ConnectionPattern


class test_Connection_Pattern(unittest.TestCase):
    """Unit tests for the ConnectionPattern class from the spydrnet_physical.util module."""

    def setUp(self) -> None:
        self.width = 11
        self.height = 11
        self.conn_manager = ConnectionPattern(self.width, self.height)
        self.conn_patt = self.conn_manager.connections

    def test_get_htree(self):
        """
        Test the creation of following H-Tree pattern.
        |                  |
        |    ↑           ↑ |
        |    ↑           ↑ |
        |    <- <- ↑ -> -> |
        |    ↓     ↑     ↓ |
        |    ↓     ↑     ↓ |
        |          ↑       |
        | 1  2  3  4  5  6 |
        """
        p_list = [
            (4, 0, 4, 1),
            (4, 1, 4, 2),
            (4, 2, 4, 3),
            (4, 3, 4, 4),
            (4, 4, 5, 4),
            (5, 4, 6, 4),
            (6, 4, 6, 5),
            (6, 5, 6, 6),
            (6, 4, 6, 3),
            (6, 3, 6, 2),
            (4, 4, 3, 4),
            (3, 4, 2, 4),
            (2, 4, 2, 5),
            (2, 5, 2, 6),
            (2, 4, 2, 3),
            (2, 3, 2, 2),
        ]
        self.conn_patt.cursor = (4, 0)
        self.conn_patt.move_y(steps=4)
        htree = self.conn_patt.merge(self.conn_manager.get_htree(7))
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_htree_2n(self):
        """
        Test the creation of H-Tree pattern for even multiple grid.
        |                               |
        |       ↑           ↑           |
        |       ↑           ↑           |
        |       <- <- ↑ -> ->           |
        |       ↓     ↑     ↓           |
        |       ↓     ↑     ↓           |
        |             ↑                 |
        |             ↑                 |
        |             ↑ (5, 0, 5, 1)    |
        | 1  2  3  4  5  6  7  8  9  10 |
        """
        p_list = [
            (5, 0, 5, 1),
            (5, 1, 5, 2),
            (5, 2, 5, 3),
            (5, 3, 5, 4),
            (5, 4, 5, 5),
            (5, 5, 6, 5),
            (6, 5, 7, 5),
            (7, 5, 7, 6),
            (7, 6, 7, 7),
            (7, 5, 7, 4),
            (7, 4, 7, 3),
            (5, 5, 4, 5),
            (4, 5, 3, 5),
            (3, 5, 3, 6),
            (3, 6, 3, 7),
            (3, 5, 3, 4),
            (3, 4, 3, 3),
        ]
        width = 10
        height = 10
        conn_manager = ConnectionPattern(width, height)
        conn_patt = conn_manager.connections
        conn_patt.cursor = (5, 0)
        conn_patt.move_y(steps=5)
        htree = conn_patt.merge(conn_manager.get_htree(width))
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_htree_root(self):
        """
        Test if the root of the HTree can be move to left of right shifted
        |                               |
        |    ↑                       ↑  |
        |    ↑                       ↑  |
        |    ↑                       ↑  |
        |    <- <- <- <-   -> -> -> ->  |
        |    ↓                       ↓  |
        |    ↓                       ↓  |
        |    ↓                       ↓  |
        |                               |
        |                               |
        | 1  2  3  4  5  6  7  8  9  10 |
        """
        p_list = [
            (6, 6, 7, 6),
            (7, 6, 8, 6),
            (8, 6, 9, 6),
            (9, 6, 10, 6),
            (10, 6, 10, 7),
            (10, 7, 10, 8),
            (10, 8, 10, 9),
            (10, 6, 10, 5),
            (10, 5, 10, 4),
            (10, 4, 10, 3),
            (6, 6, 5, 6),
            (5, 6, 4, 6),
            (4, 6, 3, 6),
            (3, 6, 2, 6),
            (2, 6, 2, 7),
            (2, 7, 2, 8),
            (2, 8, 2, 9),
            (2, 6, 2, 5),
            (2, 5, 2, 4),
            (2, 4, 2, 3),
        ]

        htree = self.conn_patt.merge(self.conn_manager.get_htree(self.width, root=1))
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_htree_side(self):
        """
        Test side parameter of get_htree
        |    ↑                       ↑  |
        |    ↑                       ↑  |
        |    ↑                       ↑  |
        |    ↑                       ↑  |
        |    <- <- <- <-   -> -> -> ->  |
        |    ↓                       ↓  |
        |    ↓                       ↓  |
        |    ↓                       ↓  |
        |    ↓                       ↓  |
        |                               |
        | 1  2  3  4  5  6  7  8  9  10 |
        """
        p_list = [
            (4, 4, 5, 4),
            (5, 4, 6, 4),
            (6, 4, 7, 4),
            (7, 4, 7, 5),
            (7, 5, 7, 6),
            (7, 6, 7, 7),
            (7, 4, 7, 3),
            (7, 3, 7, 2),
            (7, 2, 7, 1),
            (4, 4, 3, 4),
            (3, 4, 2, 4),
            (2, 4, 1, 4),
            (1, 4, 1, 5),
            (1, 5, 1, 6),
            (1, 6, 1, 7),
            (1, 4, 1, 3),
            (1, 3, 1, 2),
            (1, 2, 1, 1),
        ]

        htree = self.conn_patt.merge(self.conn_manager.get_htree(7, root=1, side=1))
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_htree_repeat(self):
        """
        Test side parameter of get_htree

        |               |
        | ↑  ↑     ↑  ↑ |
        | <- <-   -> -> |
        | ↓  ↓     ↓  ↓ |
        |               |
        | 1  2  3  4  5 |
        """
        p_list = [
            (3, 3, 4, 3),
            (4, 3, 4, 4),
            (4, 3, 4, 2),
            (4, 3, 5, 3),
            (5, 3, 5, 4),
            (5, 3, 5, 2),
            (3, 3, 2, 3),
            (2, 3, 2, 4),
            (2, 3, 2, 2),
            (2, 3, 1, 3),
            (1, 3, 1, 4),
            (1, 3, 1, 2),
        ]
        htree = self.conn_patt.merge(
            self.conn_manager.get_htree(5, root=0, side=0, repeat=2)
        )
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_fishbone(self):
        """
        Test side parameter of get_htree
        | <- <- ↑ -> -> |
        | <- <- ↑ -> -> |
        | <- <- ↑ -> -> |
        | <- <- ↑ -> -> |
        | <- <- ↑ -> -> |
        |       ↑       |
        | 1  2  3  4  5 |
        """
        p_list = [
            (3, 0, 3, 1),
            (3, 1, 4, 1),
            (4, 1, 5, 1),
            (3, 1, 2, 1),
            (2, 1, 1, 1),
            (3, 1, 3, 2),
            (3, 2, 4, 2),
            (4, 2, 5, 2),
            (3, 2, 2, 2),
            (2, 2, 1, 2),
            (3, 2, 3, 3),
            (3, 3, 4, 3),
            (4, 3, 5, 3),
            (3, 3, 2, 3),
            (2, 3, 1, 3),
            (3, 3, 3, 4),
            (3, 4, 4, 4),
            (4, 4, 5, 4),
            (3, 4, 2, 4),
            (2, 4, 1, 4),
            (3, 4, 3, 5),
            (3, 5, 4, 5),
            (4, 5, 5, 5),
            (3, 5, 2, 5),
            (2, 5, 1, 5),
        ]
        htree = self.conn_patt.merge(self.conn_manager.get_fishbone(5, 5))
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_fishbone_margin_x(self):
        """
        Test side parameter of get_htree
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |       ↑       |
        | 1  2  3  4  5 |
        """
        p_list = [
            (3, 0, 3, 1),
            (3, 1, 4, 1),
            (3, 1, 2, 1),
            (3, 1, 3, 2),
            (3, 2, 4, 2),
            (3, 2, 2, 2),
            (3, 2, 3, 3),
            (3, 3, 4, 3),
            (3, 3, 2, 3),
            (3, 3, 3, 4),
            (3, 4, 4, 4),
            (3, 4, 2, 4),
            (3, 4, 3, 5),
            (3, 5, 4, 5),
            (3, 5, 2, 5),
        ]
        htree = self.conn_patt.merge(
            self.conn_manager.get_fishbone(5, 5, x_margin=(1, 1))
        )
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)

    def test_get_fishbone_margin_y(self):
        """
        Test side parameter of get_htree
        |               |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |    <- ↑ ->    |
        |       ↑       |
        | 1  2  3  4  5 |
        """
        p_list = [
            (3, 0, 3, 2),
            (3, 2, 4, 2),
            (4, 2, 5, 2),
            (3, 2, 2, 2),
            (2, 2, 1, 2),
            (3, 2, 3, 3),
            (3, 3, 4, 3),
            (4, 3, 5, 3),
            (3, 3, 2, 3),
            (2, 3, 1, 3),
            (3, 3, 3, 4),
            (3, 4, 4, 4),
            (4, 4, 5, 4),
            (3, 4, 2, 4),
            (2, 4, 1, 4),
            (3, 4, 3, 5),
            (3, 5, 4, 5),
            (4, 5, 5, 5),
            (3, 5, 2, 5),
            (2, 5, 1, 5),
        ]
        htree = self.conn_patt.merge(
            self.conn_manager.get_fishbone(5, 5, y_margin=(1, 1))
        )
        htree_points = [points.connection for points in htree]
        self.assertListEqual(p_list, htree_points)
