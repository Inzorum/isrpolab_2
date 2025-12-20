import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_one_mul(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    
    def test_one_per(self):
        res = perimeter(1)
        self.assertEqual(res, 4)


def area(a):
    '''Принимает сторону a, возвращает площадь квадрата со стороной a'''
    return a * a

def perimeter(a):
    '''Принимает сторону a, возвращает периметр квадрата со стороной a'''
    return 4 * a

