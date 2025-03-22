import unittest

from src.interface.display import Display

class TestDisplay(unittest.TestCase):

    def test_display(self):
        assert isinstance(Display().login(), str)

