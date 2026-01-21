import unittest
import math

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

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
class SquareTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = square_area(5)
        self.assertEqual(res, 25)
    def test_basic_perimeter(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)
    def test_huge_perimeter(self):
        res = square_perimeter(10**9)
        self.assertEqual(res, 4 * (10**9))
    def test_huge_area(self):
        res = square_area(10**9)
        self.assertEqual(res, 10**18)
    def test_float_area(self):
        res = square_area(2.5)
        self.assertEqual(res, 6.25)
    def test_float_perimeter(self):
        res = square_perimeter(2.5)
        self.assertEqual(res, 10)
    def test_zero_area(self):
        res = square_area(0)
        self.assertEqual(res, 0)
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