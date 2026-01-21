import unittest
import math 

from square import area as square_area, perimeter as square_perimeter

class SquareTestCase(unittest.TestCase):
    def test_basic_area(self):
        res = square_area(5)
        self.assertEqual(res, 25)
    def test_basic_perimeter(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)
    def test_huge_perimeter(self):
        res = square_perimeter(10**9)
        self.assertEqual(res, 4 * (10**9))
    def test_huge_area(self):
        res = square_area(10**9)
        self.assertEqual(res, 10**18)
    def test_float_area(self):
        res = square_area(2.5)
        self.assertEqual(res, 6.25)
    def test_float_perimeter(self):
        res = square_perimeter(2.5)
        self.assertEqual(res, 10)
    def test_zero_area(self):
        res = square_area(0)
        self.assertEqual(res, 0)