import unittest
from triangle import area, perimetr

class TriangleTestCase(unittest.TestCase):
    def test_area_triangle_normal(self):
        res = area(27, 10)
        expected = 270
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_perimetr_triangle_uncorrect(self):
        res = perimetr(12, 10, 5000)
        expected = "Any side can't be more than summary of another two"
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")

    def test_perimetr_triangle_normal(self):
        res = perimetr(10, 6, 14)
        expected = 30
        self.assertEqual(res, expected, f"\nExpected: {expected} \nActual: {res}")


