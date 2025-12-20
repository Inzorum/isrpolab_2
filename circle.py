import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_one_mul(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_per(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    
    def test_one_per(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)


def area(r):
    '''Принимает радиус r, возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус r, возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r
