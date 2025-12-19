import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_first(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive(self):
        res = area(4, 5)
        self.assertEqual(res, 20)

    def test_area_float(self):
        res = area(2.5, 3.5)
        self.assertAlmostEqual(res, 8.75, places=5)

    def test_perimeter_zero(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_positive(self):
        res = perimeter(4, 5)
        self.assertEqual(res, 18)

    def test_perimeter_float(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

    def test_area_both_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_both_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area_large(self):
        res = area(100, 200)
        self.assertEqual(res, 20000)

    def test_perimeter_large(self):
        res = perimeter(100, 200)
        self.assertEqual(res, 600)


if __name__ == '__main__':
    unittest.main()
