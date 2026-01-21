import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        """Тест площади прямоугольника, когда вторая сторона равна нулю"""
        res = area(10, 0)
        self.assertEqual(res, 0, 
                        f"Площадь прямоугольника со сторонами (10, 0) должна быть 0, но получено {res}")

    def test_area_zero_first(self):
        """Тест площади прямоугольника, когда первая сторона равна нулю"""
        res = area(0, 5)
        self.assertEqual(res, 0,
                        f"Площадь прямоугольника со сторонами (0, 5) должна быть 0, но получено {res}")

    def test_area_both_zero(self):
        """Тест площади прямоугольника, когда обе стороны равны нулю"""
        res = area(0, 0)
        self.assertEqual(res, 0,
                        f"Площадь прямоугольника со сторонами (0, 0) должна быть 0, но получено {res}")

    def test_area_square_mul(self):
        """Тест площади квадрата (прямоугольник с равными сторонами)"""
        res = area(10, 10)
        expected = 100
        self.assertEqual(res, expected,
                        f"Площадь квадрата со стороной 10 должна быть {expected}, но получено {res}")

    def test_area_one(self):
        """Тест площади прямоугольника со стороной равной единице"""
        res = area(1, 5)
        expected = 5
        self.assertEqual(res, expected,
                        f"Площадь прямоугольника со сторонами (1, 5) должна быть {expected}, но получено {res}")

    def test_area_both_one(self):
        """Тест площади прямоугольника с обеими сторонами равными единице"""
        res = area(1, 1)
        expected = 1
        self.assertEqual(res, expected,
                        f"Площадь прямоугольника со сторонами (1, 1) должна быть {expected}, но получено {res}")

    def test_area_positive(self):
        """Тест площади прямоугольника с положительными сторонами"""
        res = area(4, 5)
        expected = 20
        self.assertEqual(res, expected,
                        f"Площадь прямоугольника со сторонами (4, 5) должна быть {expected}, но получено {res}")

    def test_area_float(self):
        """Тест площади прямоугольника с дробными сторонами"""
        res = area(2.5, 3.5)
        expected = 8.75
        self.assertAlmostEqual(res, expected, places=5,
                              msg=f"Площадь прямоугольника со сторонами (2.5, 3.5) должна быть примерно {expected}, но получено {res}")

    def test_area_large(self):
        """Тест площади прямоугольника с большими сторонами"""
        res = area(100, 200)
        expected = 20000
        self.assertEqual(res, expected,
                        f"Площадь прямоугольника со сторонами (100, 200) должна быть {expected}, но получено {res}")

    def test_area_negative_first(self):
        """Тест площади прямоугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError) as context:
            area(-5, 10)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_area_negative_second(self):
        """Тест площади прямоугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError) as context:
            area(10, -5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_area_both_negative(self):
        """Тест площади прямоугольника с обеими отрицательными сторонами"""
        with self.assertRaises(ValueError) as context:
            area(-5, -10)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_area_string_first(self):
        """Тест площади прямоугольника со строковой первой стороной"""
        with self.assertRaises(TypeError) as context:
            area("5", 10)
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_area_string_second(self):
        """Тест площади прямоугольника со строковой второй стороной"""
        with self.assertRaises(TypeError) as context:
            area(10, "5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_area_both_string(self):
        """Тест площади прямоугольника с обеими строковыми сторонами"""
        with self.assertRaises(TypeError) as context:
            area("5", "10")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_perimeter_zero(self):
        """Тест периметра прямоугольника, когда первая сторона равна нулю"""
        res = perimeter(0, 5)
        expected = 10
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (0, 5) должен быть {expected}, но получено {res}")

    def test_perimeter_both_zero(self):
        """Тест периметра прямоугольника, когда обе стороны равны нулю"""
        res = perimeter(0, 0)
        expected = 0
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (0, 0) должен быть {expected}, но получено {res}")

    def test_perimeter_square(self):
        """Тест периметра квадрата (прямоугольник с равными сторонами)"""
        res = perimeter(10, 10)
        expected = 40
        self.assertEqual(res, expected,
                        f"Периметр квадрата со стороной 10 должен быть {expected}, но получено {res}")

    def test_perimeter_one(self):
        """Тест периметра прямоугольника со стороной равной единице"""
        res = perimeter(1, 5)
        expected = 12
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (1, 5) должен быть {expected}, но получено {res}")

    def test_perimeter_both_one(self):
        """Тест периметра прямоугольника с обеими сторонами равными единице"""
        res = perimeter(1, 1)
        expected = 4
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (1, 1) должен быть {expected}, но получено {res}")

    def test_perimeter_positive(self):
        """Тест периметра прямоугольника с положительными сторонами"""
        res = perimeter(4, 5)
        expected = 18
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (4, 5) должен быть {expected}, но получено {res}")

    def test_perimeter_float(self):
        """Тест периметра прямоугольника с дробными сторонами"""
        res = perimeter(2.5, 3.5)
        expected = 12.0
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (2.5, 3.5) должен быть {expected}, но получено {res}")

    def test_perimeter_large(self):
        """Тест периметра прямоугольника с большими сторонами"""
        res = perimeter(100, 200)
        expected = 600
        self.assertEqual(res, expected,
                        f"Периметр прямоугольника со сторонами (100, 200) должен быть {expected}, но получено {res}")

    def test_perimeter_negative_first(self):
        """Тест периметра прямоугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError) as context:
            perimeter(-5, 10)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_perimeter_negative_second(self):
        """Тест периметра прямоугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError) as context:
            perimeter(10, -5)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_perimeter_both_negative(self):
        """Тест периметра прямоугольника с обеими отрицательными сторонами"""
        with self.assertRaises(ValueError) as context:
            perimeter(-5, -10)
        self.assertIn("отрицательн", str(context.exception).lower(),
                     f"Функция должна выбрасывать ValueError с сообщением об отрицательном значении, но получено: {context.exception}")

    def test_perimeter_string_first(self):
        """Тест периметра прямоугольника со строковой первой стороной"""
        with self.assertRaises(TypeError) as context:
            perimeter("5", 10)
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_perimeter_string_second(self):
        """Тест периметра прямоугольника со строковой второй стороной"""
        with self.assertRaises(TypeError) as context:
            perimeter(10, "5")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")

    def test_perimeter_both_string(self):
        """Тест периметра прямоугольника с обеими строковыми сторонами"""
        with self.assertRaises(TypeError) as context:
            perimeter("5", "10")
        self.assertIn("числ", str(context.exception).lower(),
                     f"Функция должна выбрасывать TypeError с сообщением о типе данных, но получено: {context.exception}")


if __name__ == '__main__':
    unittest.main()
