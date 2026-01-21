import unittest
import math

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class RectangleTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = rectangle_area(4, 5)
        self.assertEqual(res, 20)
    def test_basic_perimeter(self):
        res = rectangle_perimeter(4, 5)
        self.assertEqual(res, 18)
    def test_huge_perimeter(self):
        res = rectangle_perimeter(10**9, 10**9)
        self.assertEqual(res, 4 * (10**9))
    def test_huge_area(self):
        res = rectangle_area(10**9, 10**9)
        self.assertEqual(res, 10**18)
    def test_float_area(self):
        res = rectangle_area(2.5, 2.5)
        self.assertEqual(res, 6.25)
    def test_float_perimeter(self):
        res = rectangle_perimeter(2.5, 2.5)
        self.assertEqual(res, 10)
    def test_one_zero_area(self):
        res = rectangle_area(15, 0)
        self.assertEqual(res, 0)
    def test_all_zero_area(self):
        res = rectangle_area(0, 0)
        self.assertEqual(res, 0)