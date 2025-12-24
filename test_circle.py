import unittest
import math

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_float(self):
        r = 2.5
        self.assertAlmostEqual(area(r), math.pi * r * r)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_float(self):
        r = 2.5
        self.assertAlmostEqual(perimeter(r), 2 * math.pi * r)


if __name__ == "__main__":
    unittest.main()
