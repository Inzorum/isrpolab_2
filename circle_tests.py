import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = circle_area(5)
        self.assertEqual(res, 25 * math.pi)
    def test_basic_perimeter(self):
        res = circle_perimeter(5)
        self.assertEqual(res, 10 * math.pi)
    def test_huge_perimeter(self):
        res = circle_perimeter(10**9)
        self.assertEqual(res, 2 * (10**9) * math.pi)
    def test_huge_area(self):
        res = circle_area(10**9)
        self.assertEqual(res, 10**18 * math.pi)
    def test_float_area(self):
        res = circle_area(2.5)
        self.assertEqual(res, 6.25 * math.pi)
    def test_float_perimeter(self):
        res = circle_perimeter(2.5)
        self.assertEqual(res, 5 * math.pi)
    def test_zero_area(self):
        res = circle_area(0)
        self.assertEqual(res, 0)