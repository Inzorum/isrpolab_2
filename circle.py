import math
import unittest


def area(r):
    '''
    возвращает площадь круга

    возводит радиус (r) в квадрат и умножает на число π

    Пример:
    int r = 3

    возвращаемое значение: 9π
    '''
    return math.pi * r * r

#
def perimeter(r):
    '''
    возвращает периметр круга

    умножает радиус (r) на число π и на 2

     Пример:
    int r = 3

    возвращаемое значение: 6π
    '''
    return 2 * math.pi * r



class Test_circle(unittest.TestCase):
    def test_default_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_default_per(self):
        res = perimeter(7)
        self.assertEqual(res, 43.982297150257104)
