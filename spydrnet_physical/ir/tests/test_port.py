import unittest

import spydrnet as sdn
from spydrnet.ir import Bundle


class TestPort(unittest.TestCase):
    def setUp(self) -> None:
        self.port = sdn.Port()
