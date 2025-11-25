import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_normal_mul(self):
        res = area(10, 4)
        self.assertEqual(res, 20)
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 5)
        self.assertEqual(res, 5)
    def test_normal_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
