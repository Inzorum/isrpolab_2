import unittest
import math
from circle import area, perimeter
class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_normal_mul(self):
        res = area(3)
        self.assertAlmostEqual(res, math.pi * 9)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)
    def test_positive_perimeter(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 2 * math.pi * 3)
