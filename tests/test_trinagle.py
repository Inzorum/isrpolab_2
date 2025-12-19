import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(4, 5)
        self.assertEqual(res, 10.0)

    def test_area_large(self):
        res = area(10, 8)
        self.assertEqual(res, 40.0)

    def test_area_float(self):
        res = area(2.5, 3.5)
        self.assertAlmostEqual(res, 4.375, places=5)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_equilateral(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_right_triangle(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_positive(self):
        res = perimeter(6, 7, 8)
        self.assertEqual(res, 21)

    def test_perimeter_float(self):
        res = perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)


if __name__ == '__main__':
    unittest.main()

