import unittest
from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_area_square(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_square_per(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
    def test_zero_per(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_negative_value(self):
        self.assertFalse(square.area(-5))
        self.assertFalse(square.perimeter(-5))