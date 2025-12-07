import unittest

def area(a):
    '''
    возвращает площадь квадрата

    возводит сторону (a) в квадрат

    Пример:
    int a = 7

    возвращаемое значение: 49
    '''
    return a * a


def perimeter(a):
    '''
    возвращает периметр квадрата

    умножает сторону (a) на 4

    Пример:
    int a = 7

    возвращаемое значение: 28
    '''
    return 4 * a

class SquareTest(unittest.TestCase):
    def test_default_area(self):
        res = area(6)
        self.assertEqual(res, 36)
    def test_default_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
