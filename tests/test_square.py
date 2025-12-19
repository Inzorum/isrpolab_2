import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_positive(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_large(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25, places=5)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_positive(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_large(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)

    def test_area_large(self):
        res = area(100)
        self.assertEqual(res, 10000)

    def test_perimeter_large(self):
        res = perimeter(100)
        self.assertEqual(res, 400)


if __name__ == '__main__':
    unittest.main()
