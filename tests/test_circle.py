import math
import unittest
from circle import area, perimetr

class CircleTestCase(unittest.TestCase):
    def test_circle_area_normal(self):
        res = area(9)
        expected = 81 * math.pi
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_circle_area_uncorrect_data(self):
        res = area("пятьдесят два")
        expected = "Uncorrect input data: radius should be a possitive number, not a string"
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_circle_perimetr_normal(self):
        res = perimetr(12)
        expected = 24 * math.pi
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

