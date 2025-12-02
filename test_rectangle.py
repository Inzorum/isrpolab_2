import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        a, b = 3, 4
        expected = 12
        self.assertEqual(area(a, b), expected)

    def test_area_zero_side(self):
        a, b = 0, 5
        expected = 0
        self.assertEqual(area(a, b), expected)

    def test_perimeter_normal(self):
        a, b = 3, 4
        expected = 14
        self.assertEqual(perimeter(a, b), expected)

    def test_perimeter_square_case(self):
        a, b = 5, 5
        expected = 20
        self.assertEqual(perimeter(a, b), expected)


    def test_area_zero(self):
        a, b = 0, 0
        expected = 0
        self.assertEqual(area(a, b), expected)


if __name__ == "__main__":
    unittest.main()