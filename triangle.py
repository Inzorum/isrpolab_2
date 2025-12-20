import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 10)
        self.assertEqual(res, 0.0)
       
    def test_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50.0)

    def test_one_mul(self):
        res = area(1, 10)
        self.assertEqual(res, 5.0)

    def test_zero_per(self):
        res = perimeter(0, 10, 10)
        self.assertEqual(res, 20)

    def test_per(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
    
    def test_one_per(self):
        res = perimeter(1, 10, 10)
        self.assertEqual(res, 21)

def area(a, h): 
    '''Принимает сторону a и высоту h, возвращает площадь треугольника со стороной a и высотой h'''
    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает сторонами a,b,c и возвращает периметр треугольника с данными сторонами'''
    return a + b + c
    