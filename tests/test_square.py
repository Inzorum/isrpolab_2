import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0,
                        f"Площадь квадрата со стороной 0 должна быть 0, но получено {res}")

    def test_area_one(self):
        """Тест площади квадрата со стороной равной единице"""
        res = area(1)
        expected = 1
        self.assertEqual(res, expected,
                        f"Площадь квадрата со стороной 1 должна быть {expected}, но получено {res}")

    def test_area_positive(self):
        """Тест площади квадрата с положительной стороной"""
        res = area(4)
        expected = 16
        self.assertEqual(res, expected,
                        f"Площадь квадрата со стороной 4 должна быть {expected}, но получено {res}")

    def test_area_large(self):
        """Тест площади квадрата с большой стороной"""
        res = area(100)
        expected = 10000
        self.assertEqual(res, expected,
                        f"Площадь квадрата со стороной 100 должна быть {expected}, но получено {res}")

    def test_area_float(self):
        """Тест площади квадрата с дробной стороной"""
        res = area(2.5)
        expected = 6.25
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь квадрата со стороной 2.5 должна быть примерно {expected}, но получено {res}")

    def test_area_negative(self):
        """Тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError) as context:
            area(-5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_area_string(self):
        """Тест площади квадрата со строковым значением"""
        with self.assertRaises(TypeError) as context:
            area("5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0,
                        f"Периметр квадрата со стороной 0 должен быть 0, но получено {res}")

    def test_perimeter_one(self):
        """Тест периметра квадрата со стороной равной единице"""
        res = perimeter(1)
        expected = 4
        self.assertEqual(res, expected,
                        f"Периметр квадрата со стороной 1 должен быть {expected}, но получено {res}")

    def test_perimeter_positive(self):
        """Тест периметра квадрата с положительной стороной"""
        res = perimeter(4)
        expected = 16
        self.assertEqual(res, expected,
                        f"Периметр квадрата со стороной 4 должен быть {expected}, но получено {res}")

    def test_perimeter_large(self):
        """Тест периметра квадрата с большой стороной"""
        res = perimeter(100)
        expected = 400
        self.assertEqual(res, expected,
                        f"Периметр квадрата со стороной 100 должен быть {expected}, но получено {res}")

    def test_perimeter_float(self):
        """Тест периметра квадрата с дробной стороной"""
        res = perimeter(2.5)
        expected = 10.0
        self.assertEqual(res, expected,
                        f"Периметр квадрата со стороной 2.5 должен быть {expected}, но получено {res}")

    def test_perimeter_negative(self):
        """Тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError) as context:
            perimeter(-5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_perimeter_string(self):
        """Тест периметра квадрата со строковым значением"""
        with self.assertRaises(TypeError) as context:
            perimeter("5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")


if __name__ == '__main__':
    unittest.main()
