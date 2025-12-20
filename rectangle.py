import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_one_mul(self):
        res = area(1, 10)
        self.assertEqual(res, 10)

    def test_zero_per(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_square_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_one_per(self):
        res = perimeter(1, 10)
        self.assertEqual(res, 22)


def area(a, b): 
    '''Принимает стороны a и b, возвращает площадь прямоугольника со сторонами a и b'''
    return a * b 

def perimeter(a, b):
    '''Принимает стороны a и b, возвращает периметр прямоугольника со сторонами a и b''' 
    return 2 * (a + b)
    