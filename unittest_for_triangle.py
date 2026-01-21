import unittest;
from triangle import *

# def area(a, h):
#     '''
#     Возвращает площадь треугольника.

#     Параметры:
#             a (int) - основание треугольника,
#             b (int) - высота треугольника, проведённая к основанию.
#     Возвращаемое значение - результат произведения a на h, делённый на 2 (int).

#     Пример вызова:
#     res = area(4, 3)
#     print(res)
#     >> 6
#     '''
#     if (a + b < c or a + c < b or b + c < a):
#         print("Error: invalid triangle")
#         return -1
#     return a * h / 2

# def perimeter(a, b, c):
#     '''
#     Возвращает периметр треугольника.

#     Параметры:
#             a (int) - первая сторона треугольника,
#             b (int) - вторая сторона треугольника,
#             c (int) - третья сторона треугольника.
#     Возвращаемое значение - сумма всех трёх значений сторон (int).

#     Пример вызова:
#     res = perimeter(3, 3, 4)
#     print(res)
#     >> 10
#     '''
#     if (a + b < c or a + c < b or b + c < a):
#         print("Error: invalid triangle")
#         return -1
#     return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_square_mul(self):
       res = area(4, 3)
       self.assertEqual(res, 6)
    def test_fifty_square(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_first_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    def test_ninty_nine_perimeter(self):
        res = perimeter(33, 33, 33)
        self.assertEqual(res, 99)
    def test_proper_sides(self):
        res = perimeter(1, 1, 99)
        self.assertNotEqual(res, 101)
        self.assertEqual(res, -1)

if __name__ == '__main__':
    unittest.main()