import unittest

from src.backend.app import App


class TestApp(unittest.TestCase):

    def test_calculate(self):
        app = App()
        assert 4 == app.calculate(2, 2)
