import unittest
import math

import circle 
import square

class CircleTestCase(unittest.TestCase):
    ''' Тесты для circle.py проверка вычисления площадь и периметра круга'''

    def test_circle_area_small_int_radius(self):
        #Проверяет вычисление площади круга, когда радиус - небольшое целое положительное число
        res = circle.area(2)
        self.assertAlmostEqual(res,math.pi * 4,places = 5)

    def test_circle_area_zero_radius(self):
        #Проверяет вычисление площади круга, когда радиус = 0
        res = circle.area(0)
        self.assertEqual(res,0)

    def test_circle_area_float_radius(self):
        #Проверяет вычисление площади круга, когда радиус - небольшое дробное положительное число
        res = circle.area(1.32)
        self.assertAlmostEqual(res,math.pi * (1.32) ** 2, places = 5)
        
    def test_circle_area_large_int_radius(self):
        #Проверяет вычисление площади круга, когда радиус - большое целое положительное число 
        res = circle.area(100)
        self.assertAlmostEqual(res, math.pi * (100 ** 2), places = 5)

    def test_circle_area_large_float_radius(self):
        #Проверяет вычисление площади круга, когда радиус - большое дробное положительное число
        res = circle.area(123.45)
        self.assertAlmostEqual(res, math.pi * (123.45 ** 2), places = 5)
    
    def test_circle_perimeter_small_int_radius(self):
        #Проверяет вычисление периметра круга, когда радиус - небольшое целое положительное число
        res = circle.perimeter(2)
        self.assertAlmostEqual(res,2 * math.pi * 2,places = 5)

    def test_circle_perimetr_zero_radius(self):
        #Проверяет вычисление периметра круга, когда радиус = 0
        res = circle.perimeter(0)
        self.assertEqual(res,0)

    def test_circle_perimeter_float_radius(self):
        #Проверяет вычисление периметра круга, когда радиус - небольшое дробное положительное число
        res = circle.perimeter(1.32)
        self.assertAlmostEqual(res,2 * math.pi * 1.32, places = 5)
        
    def test_circle_perimeter_large_int_radius(self):
        #Проверяет вычисление периметра круга, когда радиус - большое целое положительное число
        res = circle.perimeter(120)
        self.assertAlmostEqual(res,2 * math.pi * 120, places = 5)
    
    def test_circle_perimeter_large_float_radius(self):
        #Проверяет вычисление периметра круга, когда радиус - большое дробное положительное число
        res = circle.perimeter(123.45)
        self.assertAlmostEqual(res, 2 * math.pi * 123.45, places = 5)

class SquareTestCase(unittest.TestCase):
    ''' Тесты для square.py проверка вычисления площадь и периметра квадрата'''

    def test_square_area_small_int_square_side(self):
        #Проверяет вычисление площади квадрата, когда сторона - небольшое целое положительное число
        res = square.area(2)
        self.assertEqual(res,4)

    def test_area_square_zero(self):
        #Проверяет вычисление площади квадрата, когда сторона = 0
        res = square.area(0)
        self.assertEqual(res,0)

    def test_square_area_float_square_side(self):
        #Проверяет вычисление площади квадрата, когда сторона - небольшое дробное положительное число
        res = square.area(1.32)
        self.assertEqual(res, 1.32 ** 2)

    def test_square_area_int_large_square_side(self):
        #Проверяет вычисление площади квадрата, когда сторона - большое целое положительное число
        res = square.area(100)
        self.assertEqual(res,100 ** 2)
    
    def test_square_area_float_large_square_side(self):
        #Проверяет вычисление площади квадрата, когда сторона - большое дробное положительное число
        res = square.area(123.45)
        self.assertAlmostEqual(res,123.45 ** 2, places = 5)

    def test_square_perimeter_small_int_square_side(self):
        #Проверяет вычисление периметра квадрата, когда сторона - небольшое целое положительное число
        res = square.perimeter(2)
        self.assertEqual(res,2 * 4)

    def test_perimetr_square_zero(self):
        #Проверяет вычисление периметра квадрата, когда сторона = 0
        res = square.perimeter(0)
        self.assertEqual(res,0)

    def test_square_perimeter_float_square_side(self):
        #Проверяет вычисление периметра квадрата, когда сторона - небольшое дробное положительное число
        res = square.perimeter(1.32)
        self.assertAlmostEqual(res, 1.32 * 4,places = 5)

    def test_square_perimeter_int_large_square_side(self):
        #Проверяет вычисление периметра квадрата, когда сторона - большое целое положительное число
        res = square.perimeter(100)
        self.assertEqual(res,100 * 4)
    
    def test_square_perimeter_float_large_square_side(self):
        #Проверяет вычисление периметра квадрата, когда сторона - большое дробное положительное число
        res = square.perimeter(123.45)
        self.assertAlmostEqual(res,123.45 * 4, places = 5)
if __name__ == '__main__':
    unittest.main()