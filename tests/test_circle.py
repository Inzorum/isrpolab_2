import unittest
from geometric_lib.circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_area_circle(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_circle_per(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    def test_zero_per(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_negative_value(self):
        self.assertFalse(circle.area(-5))
        self.assertFalse(circle.perimeter(-5))