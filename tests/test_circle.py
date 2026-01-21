import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from circle import area, perimeter
import math


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        """Тест площади круга с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0,
                        f"Площадь круга с радиусом 0 должна быть 0, но получено {res}")

    def test_area_one(self):
        """Тест площади круга с радиусом равным единице"""
        res = area(1)
        expected = math.pi
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь круга с радиусом 1 должна быть примерно {expected}, но получено {res}")

    def test_area_positive(self):
        """Тест площади круга с положительным радиусом"""
        res = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь круга с радиусом 5 должна быть примерно {expected}, но получено {res}")

    def test_area_float(self):
        """Тест площади круга с дробным радиусом"""
        res = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь круга с радиусом 2.5 должна быть примерно {expected}, но получено {res}")

    def test_area_large(self):
        """Тест площади круга с большим радиусом"""
        res = area(100)
        expected = math.pi * 10000
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь круга с радиусом 100 должна быть примерно {expected}, но получено {res}")

    def test_area_negative(self):
        """Тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError) as context:
            area(-5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_area_string(self):
        """Тест площади круга со строковым значением"""
        with self.assertRaises(TypeError) as context:
            area("5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_perimeter_zero(self):
        """Тест периметра круга с нулевым радиусом"""
        res = perimeter(0)
        self.assertEqual(res, 0,
                        f"Периметр круга с радиусом 0 должен быть 0, но получено {res}")

    def test_perimeter_one(self):
        """Тест периметра круга с радиусом равным единице"""
        res = perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Периметр круга с радиусом 1 должен быть примерно {expected}, но получено {res}")

    def test_perimeter_positive(self):
        """Тест периметра круга с положительным радиусом"""
        res = perimeter(10)
        expected = 20 * math.pi
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Периметр круга с радиусом 10 должен быть примерно {expected}, но получено {res}")

    def test_perimeter_float(self):
        """Тест периметра круга с дробным радиусом"""
        res = perimeter(3.5)
        expected = 7 * math.pi
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Периметр круга с радиусом 3.5 должен быть примерно {expected}, но получено {res}")

    def test_perimeter_large(self):
        """Тест периметра круга с большим радиусом"""
        res = perimeter(100)
        expected = 200 * math.pi
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Периметр круга с радиусом 100 должен быть примерно {expected}, но получено {res}")

    def test_perimeter_negative(self):
        """Тест периметра круга с отрицательным радиусом"""
        with self.assertRaises(ValueError) as context:
            perimeter(-5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_perimeter_string(self):
        """Тест периметра круга со строковым значением"""
        with self.assertRaises(TypeError) as context:
            perimeter("5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")


if __name__ == '__main__':
    unittest.main()
