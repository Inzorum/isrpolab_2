import unittest

def area(a, b):
    '''
    возвращает площадь прямоугольника

    умножает сторону (a) на сторону (b)

    Пример:
    int a = 2
    int b = 3

    возвращаемое значение: 6
    '''
    return a * b


def perimeter(a, b):
    '''
    возвращает периметр прямоугольника

    суммирует сторону (a) и сторону (b) и умножает на 2

    Пример:
    int a = 2
    int b = 3

    возвращаемое значение: 10
    '''
    return (a + b)*2

class RectangleTest(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_default_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
