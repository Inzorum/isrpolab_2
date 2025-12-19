import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base(self):
        """Тест площади треугольника с нулевым основанием"""
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        """Тест площади треугольника с нулевой высотой"""
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_both_zero(self):
        """Тест площади треугольника с нулевым основанием и высотой"""
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        """Тест площади треугольника с положительными значениями"""
        res = area(4, 5)
        self.assertEqual(res, 10.0)

    def test_area_large(self):
        """Тест площади треугольника с большими значениями"""
        res = area(100, 50)
        self.assertEqual(res, 2500.0)

    def test_area_float(self):
        """Тест площади треугольника с дробными значениями"""
        res = area(2.5, 3.5)
        self.assertAlmostEqual(res, 4.375, places=5)

    def test_area_negative_base(self):
        """Тест площади треугольника с отрицательным основанием"""
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_area_negative_height(self):
        """Тест площади треугольника с отрицательной высотой"""
        with self.assertRaises(ValueError):
            area(10, -5)

    def test_area_both_negative(self):
        """Тест площади треугольника с отрицательными основанием и высотой"""
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_area_string_base(self):
        """Тест площади треугольника со строковым основанием"""
        with self.assertRaises(TypeError):
            area("5", 10)

    def test_area_string_height(self):
        """Тест площади треугольника со строковой высотой"""
        with self.assertRaises(TypeError):
            area(10, "5")

    def test_area_both_string(self):
        """Тест площади треугольника со строковыми основанием и высотой"""
        with self.assertRaises(TypeError):
            area("5", "10")

    def test_perimeter_zero(self):
        """Тест периметра треугольника с нулевыми сторонами"""
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_one_zero(self):
        """Тест периметра треугольника с одной нулевой стороной"""
        res = perimeter(0, 5, 5)
        self.assertEqual(res, 10)

    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_right_triangle(self):
        """Тест периметра прямоугольного треугольника"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_positive(self):
        """Тест периметра треугольника с положительными сторонами"""
        res = perimeter(6, 7, 8)
        self.assertEqual(res, 21)

    def test_perimeter_float(self):
        """Тест периметра треугольника с дробными сторонами"""
        res = perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)

    def test_perimeter_large(self):
        """Тест периметра треугольника с большими сторонами"""
        res = perimeter(100, 200, 300)
        self.assertEqual(res, 600)

    def test_perimeter_negative_first(self):
        """Тест периметра треугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError):
            perimeter(-5, 10, 15)

    def test_perimeter_negative_second(self):
        """Тест периметра треугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError):
            perimeter(10, -5, 15)

    def test_perimeter_negative_third(self):
        """Тест периметра треугольника с отрицательной третьей стороной"""
        with self.assertRaises(ValueError):
            perimeter(10, 15, -5)

    def test_perimeter_all_negative(self):
        """Тест периметра треугольника со всеми отрицательными сторонами"""
        with self.assertRaises(ValueError):
            perimeter(-5, -10, -15)

    def test_perimeter_string_first(self):
        """Тест периметра треугольника со строковой первой стороной"""
        with self.assertRaises(TypeError):
            perimeter("5", 10, 15)

    def test_perimeter_string_second(self):
        """Тест периметра треугольника со строковой второй стороной"""
        with self.assertRaises(TypeError):
            perimeter(10, "5", 15)

    def test_perimeter_string_third(self):
        """Тест периметра треугольника со строковой третьей стороной"""
        with self.assertRaises(TypeError):
            perimeter(10, 15, "5")

    def test_perimeter_all_string(self):
        """Тест периметра треугольника со всеми строковыми сторонами"""
        with self.assertRaises(TypeError):
            perimeter("5", "10", "15")


if __name__ == '__main__':
    unittest.main()
