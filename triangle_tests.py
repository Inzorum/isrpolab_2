import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter

class TriangleTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = triangle_area(2, 5)
        self.assertEqual(res, 5)
    def test_basic_perimeter(self):
        res = triangle_perimeter(3, 5, 7)
        self.assertEqual(res, 15)
    def test_huge_perimeter(self):
        res = triangle_perimeter(10**9, 10**9, 10**9)
        self.assertEqual(res, 3 * (10**9))
    def test_huge_area(self):
        res = triangle_area(10**9, 10**9)
        self.assertEqual(res, (10**18) * 0.5)
    def test_float_area(self):
        res = triangle_area(2.5, 2.5)
        self.assertEqual(res, 3.125)
    def test_float_perimeter(self):
        res = triangle_perimeter(2.5, 2.5, 2.5)
        self.assertEqual(res, 7.5)
    def test_one_zero_area(self):
        res = triangle_area(15, 0)
        self.assertEqual(res, 0)
    def test_all_zero_area(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 0)