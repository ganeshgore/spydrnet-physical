import unittest

from spydrnet.ir import FirstClassElement
from spydrnet.ir import Pin


class TestPin(unittest.TestCase):
    def setUp(self):
        self.pin = Pin()