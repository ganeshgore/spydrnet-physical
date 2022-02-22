''' Tst cases fro get_names method '''
from spydrnet_physical.util import RoutingRender
import unittest
from spydrnet_physical.util import get_names


class TestRoutingRender(unittest.TestCase):
    ''' Test Routing Rendering '''

    def setUp(self) -> None:
        self.name = ""
