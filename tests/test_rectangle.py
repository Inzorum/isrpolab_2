import unittest
from geometric_lib.rectangle import area, perimeter 

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10,0)
        self.assertEqual(res,0)
    def test_square_mul(self):
        res = rectangle.area(10,10)
        self.assertEqual(res,100)

    def test_zero_per(self):
        res = rectangle.perimeter(0,0)
        self.assertEqual(res,0)
    def test_square_per(self):
        res = rectangle.perimeter(10,10)
        self.assertEqual(res,40)

    def test_negative_width_length_area(self):
        self.assertFalse(rectangle.area(-5, 10))
        self.assertFalse(rectangle.perimeter(-5, 10))
