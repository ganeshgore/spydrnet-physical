""" Unit tests for ConnectionPoint Class """

import unittest
from spydrnet_physical.util import rrgraph
import capnp  # noqa: F401
from spydrnet_physical.util import rr_graph_uxsdcxx_capnp
import tempfile
import random
import string
import xml.etree.ElementTree as ET


class test_rrgraph(unittest.TestCase):
    """
    Unit tests for the rrgraph class.
    """

    def setUp(self) -> None:
        self.rrgraph = rrgraph(6, 6, "vpr_arch", "routing_chan")

    @staticmethod
    def _gen_random_string(length):
        c = random.choices(string.ascii_letters + string.digits, k=length)
        return "".join(c)

    def test_create_node_no_truncated(self) -> None:
        """Test create_node method without truncation"""
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
        """Test create_node method with truncation"""
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

    def test_switches_bin2xml(self) -> None:
        """Test the creation of a switch and its attributes in the rrgraph."""

        sw_name = self._gen_random_string(15)
        sw_type = "mux"
        switch = self.rrgraph.create_switch(sw_name, sw_type)
        self.assertEqual(switch.id, 0)
        self.assertEqual(switch.name, sw_name)
        self.assertEqual(switch.type, sw_type)

    def test_write_rrgraph_xml(self) -> None:
        """
        Test the `write_rrgraph_xml` method of the `rrgraph` class.
        This test generates a random rrgraph object and writes it to a temporary
        XML file. It then verifies that the XML file contains the correct tool
        metadata attributes.
        Steps:
        1. Create an rrgraph object with specified parameters.
        2. Generate random strings for tool_comment, tool_name, and tool_version.
        3. Write the rrgraph object to a temporary XML file using the generated
           metadata.
        4. Parse the XML file and verify that the root element's attributes match
           the generated metadata.
        Asserts:
        - The root element's "tool_comment" attribute matches the generated tool_comment.
        - The root element's "tool_name" attribute matches the generated tool_name.
        - The root element's "tool_version" attribute matches the generated tool_version.
        """

        rrgraph_bin = rrgraph(6, 6, "vpr_arch", "routing_chan")

        tool_comment = self._gen_random_string(50)
        tool_name = self._gen_random_string(10)
        tool_version = self._gen_random_string(5)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
            rrgraph_bin.write_rrgraph_xml(
                temp_file.name, tool_comment, tool_name, tool_version
            )
            tree = ET.parse(temp_file.name)
            root = tree.getroot()

        self.assertEqual(root.attrib["tool_comment"], tool_comment)
        self.assertEqual(root.attrib["tool_name"], tool_name)
        self.assertEqual(root.attrib["tool_version"], tool_version)

    # bin2xml conversion utilities
