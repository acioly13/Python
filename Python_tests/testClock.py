import unittest
from clock import *


class ClockTest(unittest.TestCase):

    def setUp(self):
        self.radius2degrees = clock.radius2degrees(self, angle=45.0)

    def test_radius2degrees(self):
        valor = self.radius2degrees
        self.assertIsNotNone(valor)


if __name__ == '__main__':
    unittest.main()

