import unittest
from rectangle import area, perimetr

class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle_uncorrect_data(self):
        expected = "Uncorrect input data: numbers should be more than 0"
        res = area(-4, 15)
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_area_rectangle_normal(self):
        expected = 150
        res = area(15, 10)
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_perimetr_uncorrect_data(self):
        expected = "Uncorrect input data: numbers should be more than 0"
        res = perimetr(2, -18)
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_perimetr_rectangle_normal(self):
        expected = 90
        res = perimetr(15, 30)
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    