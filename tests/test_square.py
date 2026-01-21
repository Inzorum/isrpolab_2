import unittest
from square import area, perimetr

class SquareTestCase(unittest.TestCase):
    def test_square_area_normal(self):
        res = area(25)
        expected = 625
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_square_area_negative(self):
        res = area(-100500)
        expected = "Uncorrect input data: number should be more than 0"
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_square_perimetr_normal(self):
        res = perimetr(500)
        expected = 2000
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")
