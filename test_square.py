import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    '''Набор юнит‑тестов для функций вычисления площади и периметра квадрата.'''

    def test_area(self):
        '''Проверяет, что функция area(a) правильно вычисляет площадь квадрата a * a.'''
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        '''Проверяет, что функция perimeter(a) правильно вычисляет периметр квадрата 4 * a.'''
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(5), 20)

if __name__ == "__main__":
    '''Запускает выполнение всех тестов только при прямом запуске этого файла'''
    unittest.main()
