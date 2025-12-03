import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        a = 5
        expected = 25
        self.assertEqual(area(a), expected)

    def test_area_zero(self):
        a = 0
        expected = 0
        self.assertEqual(area(a), expected)

    def test_perimeter_normal(self):
        a = 5
        expected = 20
        self.assertEqual(perimeter(a), expected)

    def test_perimeter_zero(self):
        a = 0
        expected = 0
        self.assertEqual(perimeter(a), expected)


if __name__ == "__main__":
    unittest.main()