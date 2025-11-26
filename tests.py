import circle
import triangle
import rectangle
import square
import unittest
import math

class TestCase(unittest.TestCase):
    def test_circle_perimetr_and_area(self):
        res1 = circle.perimeter(5)
        res2 = circle.area(12)
        self.assertEqual(res1, 2 * math.pi * 5)
        self.assertEqual(res2, math.pi * 12 * 12)

    def test_zero_circle(self):
        res1 = circle.area(0)
        res2 = circle.perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)

    def test_square_perimetr_and_area(self):
        res1 = square.perimeter(5)
        res2 = square.area(12)
        self.assertEqual(res1, 20)
        self.assertEqual(res2, 144)

    def test_zero_square(self):
        res1 = square.area(0)
        res2 = square.perimeter(0)
        self.assertEqual(0, res1)
        self.assertEqual(0, res2)

    def test_rectangle_perimetr_and_area(self):
        res1 = rectangle.perimeter(5, 6)
        res2 = rectangle.area(12, 3)
        self.assertEqual(res1, 22)
        self.assertEqual(res2, 36)

    def test_zero_rectangle(self):
        res1 = rectangle.area(2, 0)
        res2 = rectangle.perimeter(0, 5)
        self.assertEqual(0, res1)
        self.assertEqual(0, res2)

    def test_triangle_perimetr_and_area(self):
        res1 = triangle.perimeter(5, 4, 8)
        res2 = triangle.area(12, 2)
        self.assertEqual(res1, 17)
        self.assertEqual(res2, 12)

    def test_zero_triangle(self):
        res1 = triangle.area(0, 1)
        res2 = triangle.perimeter(0, 2, 0)
        self.assertEqual(0, res1)
        self.assertEqual(0, res2)
