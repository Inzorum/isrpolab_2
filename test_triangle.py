import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        a, h = 6, 4
        expected = 12
        self.assertEqual(area(a, h), expected)

    def test_area_zero_height(self):
        a, h = 10, 0
        expected = 0
        self.assertEqual(area(a, h), expected)

    def test_perimeter_normal(self):
        a, b, c = 3, 4, 5
        expected = 12
        self.assertEqual(perimeter(a, b, c), expected)

    def test_perimeter_equal_sides(self):
        a = b = c = 7
        expected = 21
        self.assertEqual(perimeter(a, b, c), expected)


if __name__ == "__main__":
    unittest.main()