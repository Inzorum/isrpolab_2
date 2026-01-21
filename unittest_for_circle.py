import unittest;
import math;
from circle import *

# def area(r):
#     '''
#     Возвращает площадь окружности (float)
    
#     Принимает значение r, где r (int) - радиус окружности
    
#     Пример вызова:
#     res = area(5)
#     print(res)
#     >> 78.5
#     '''
#     return math.pi * r * r


# def perimeter(r):
#     '''
#     Возвращает длину окружности (float)
    
#     Принимает значение r, где r (int) - радиус окружности
    
#     Пример вызова:
#     c = perimeter(3)
#     print(c)
#     >> 18.84
#     '''
#     return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
       res = area(5)
       self.assertEqual(res, 78.53981633974483)
    def test_two_square(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_first_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)
    def test_hundred_perimeter(self):
        res = perimeter(100)
        self.assertAlmostEqual(res, 2*314.15, places=1)
        

if __name__ == '__main__':
    unittest.main()
