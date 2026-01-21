import unittest;
from square import *

# def area(a):
#     '''
#     Возвращает площадь квадрата (int).
    
#     Принимает значение a (int) - сторона квадрата
    
#     Пример вызова:
#     res = area(24)
#     print(res)
#     >> 576
#     '''
#     return a * a


# def perimeter(a):
#     '''
#     Возвращает периметр квадрата (int).

#     Принимает значение a (int) - сторона квадрата
    
#     Пример вызова:
#     res = perimeter(24)
#     print(res)
#     >> 96
#     '''
#     return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
       res = area(24)
       self.assertEqual(res, 576)
    def test_fifty_side_square(self):
        res = area(50)
        self.assertEqual(res, 2500)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_first_perimeter(self):
        res = perimeter(24)
        self.assertEqual(res, 96)
    def test_thirteen_side_perimeter(self):
        res = perimeter(13)
        self.assertEqual(res, 52)

if __name__ == '__main__':
    unittest.main()