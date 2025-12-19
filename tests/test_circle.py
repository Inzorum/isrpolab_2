import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from circle import area, perimeter
import math


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi, places=5)

    def test_area_positive(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25, places=5)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=5)

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 20 * math.pi, places=5)

    def test_perimeter_float(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 7 * math.pi, places=5)

    def test_area_large(self):
        res = area(100)
        self.assertAlmostEqual(res, math.pi * 10000, places=5)

    def test_perimeter_large(self):
        res = perimeter(100)
        self.assertAlmostEqual(res, 200 * math.pi, places=5)


if __name__ == '__main__':
    unittest.main()
