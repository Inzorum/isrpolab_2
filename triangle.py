import unittest

def area(a, h):
    '''
    возвращает площадь треугольника

    перемножает сторону (a) на высоту (h) и делит на 2

    Пример:
    int a = 4
    int h = 6

    возвращаемое значение: 12
    '''
    return a * h /2
def perimeter(a, b, c):
    '''
    возвращает периметр треугольника

    суммирует сторону (a) со стороной (b) со стороной (c)

    Пример:
    int a = 4
    int b = 3
    int c = 2

    возвращаемое значение: 9
    '''
    return a+b+c

class TriangleTest(unittest.TestCase):
    def  test_default_area(self):
        res = area(4, 6)
        self.assertEqual(res, 12)
    def test_default_per(self):
        res = perimeter(4, 3, 2)
        self.assertEqual(res, 9)