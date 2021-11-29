''' Tst cases fro get_names method '''
import unittest
import networkx as nx
from spydrnet_physical.util import prepare_graph_from_nx


class TestConnectivityGraph(unittest.TestCase):
    ''' Test case class '''

    def setUp(self):
        ''' Basic element setup '''
        self.graph = nx.Graph()
        self.graph.add_node(0)
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(0, 1, weight=10)
        self.graph.add_edge(0, 2, weight=5)

    def test_prepare_graph_from_nx(self):
        ''' Test returned array '''
        xadj, adjncy, eweights = \
            prepare_graph_from_nx(nx.to_numpy_array(self.graph))
        self.assertEqual(xadj, [0, 2, 3, 4])
        self.assertEqual(adjncy, [2, 3, 1, 1])
        self.assertEqual(eweights, [10.0, 5.0, 10.0, 5.0])
