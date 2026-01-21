import unittest
from geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0,0)
        self.assertEqual(res, 0)
    def test_area_triangle(self):
        res = triangle.area(5,6)
        self.assertEqual(res, 15)

    def test_triangle_per(self):
        res = triangle.perimeter(5,4,3)
        self.assertEqual(res, 12)
    def test_zero_per(self):
        res = triangle.perimeter(0,0,0)
        self.assertEqual(res, 0)
    
    def test_neravenstvo_triangle(self):
        self.assertFalse(triangle.perimeter(10, 4, 5))
        self.assertFalse(triangle.perimeter(1, 100, 1))
    def test_negative_triangle(self):
        self.assertFalse(triangle.perimeter(-5, 4, 5))
        self.assertFalse(triangle.area(-11, 1))
        