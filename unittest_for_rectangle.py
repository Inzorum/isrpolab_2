import unittest;
from rectangle import *

# def area(a, b):
#     '''
#     Возвращает площадь прямоугольника.

#     Параметры:
#             a (int) - первая сторона прямоугольника,
#             b (int) - вторая сторона прямоугольника.
#     Возвращаемое значение - результат произведения a на b (int).

#     Пример вызова:
#     res = area(3, 5)
#     print(res)
#     >> 15
#     '''
#     return a * b

# def perimeter(a, b):
#     '''
#     Возвращает периметр прямоугольника.

#     Параметры:
#             a (int) - первая сторона прямоугольника,
#             b (int) - вторая сторона прямоугольника.
#     Возвращаемое значение - удвоенная сумма сторон, что соответствует определению периметра (int).

#     Пример вызова:
#     res = perimeter(3, 5)
#     print(res)
#     >> 16
#     '''
#     return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
    def test_fifteen_square(self):
        res = area(3, 5)
        self.assertEqual(res, 15)
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_thirty_perimeter(self):
        res = perimeter(3, 5)
        self.assertEqual(res, 16)
    def test_hundred_perimeter(self):
        res = perimeter(15, 35)
        self.assertEqual(res, 100)

if __name__ == '__main__':
    unittest.main()
