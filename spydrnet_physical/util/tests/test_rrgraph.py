''' Unit tests for ConnectionPoint Class '''
import unittest
from spydrnet_physical.util import rrgraph


class test_rrgraph(unittest.TestCase):
    """
    Unit tests for the rrgraph class.
    """

    def setUp(self) -> None:
        self.rrgraph = rrgraph(6, 6, "vpr_arch", "routing_chan")

    def test_create_node_no_truncated(self) -> None:
        """ Test create_node method without truncation """
        # Right going node without truncation
        node = self.rrgraph.create_node(1, 1, 8000, 0, "L4", "Right", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2,4,6")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 5, 1, 1))

        # Top going node without truncation
        node = self.rrgraph.create_node(1, 1, 8000, 0, "L4", "Top", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2,4,6")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 1, 1, 5))

        # Left going node without truncation
        node = self.rrgraph.create_node(6, 1, 8000, 0, "L4", "Left", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "7,5,3,1")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (2, 6, 1, 1))

        # Bottom going node without truncation
        node = self.rrgraph.create_node(6, 6, 8000, 0, "L4", "Bottom", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "7,5,3,1")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (6, 6, 2, 6))

    def test_create_node_truncated(self) -> None:
        """ Test create_node method with truncation """
        # Right going node with truncation
        node = self.rrgraph.create_node(4, 1, 8000, 0, "L4", "Right", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (4, 6, 1, 1))

        # Top going node with truncation
        node = self.rrgraph.create_node(1, 4, 8000, 0, "L4", "Top", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 1, 4, 6))

        # Left going node with truncation
        node = self.rrgraph.create_node(2, 1, 8000, 0, "L4", "Left", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "7")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 2, 1, 1))

        # Bottom going node with truncation
        node = self.rrgraph.create_node(1, 2, 8000, 0, "L4", "Bottom", 1)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "7")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 1, 1, 2))

    def test_create_node_truncated_at_source(self) -> None:
        """Test create_node method with truncation at source"""
        # Right going node with truncation at source
        node = self.rrgraph.create_node(1, 1, 8000, 0, "L4", "Right", 2)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2,4")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 4, 1, 1))

        # Top going node with truncation at source
        node = self.rrgraph.create_node(1, 1, 8000, 0, "L4", "Top", 2)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "0,2,4")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (1, 1, 1, 4))

        # Left going node with truncation at source
        node = self.rrgraph.create_node(6, 1, 8000, 0, "L4", "Left", 2)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "5,3,1")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (3, 6, 1, 1))

        # Bottom going node with truncation at source
        node = self.rrgraph.create_node(6, 6, 8000, 0, "L4", "Bottom", 3)
        self.assertEqual(node.id, 8000)
        self.assertEqual(node.loc.twist, 2)
        self.assertEqual(node.loc.ptc, "3,1")
        pts = (node.loc.xlow, node.loc.xhigh, node.loc.ylow, node.loc.yhigh)
        self.assertTupleEqual(pts, (6, 6, 4, 6))
