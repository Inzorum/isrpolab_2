import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_positive(self):
        r = 3
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected)

    def test_area_zero(self):
        r = 0
        expected = 0
        self.assertEqual(area(r), expected)

    def test_perimeter_positive(self):
        r = 3
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected)

    def test_perimeter_zero(self):
        r = 0
        expected = 0
        self.assertEqual(perimeter(r), expected)


if __name__ == "__main__":
    unittest.main()