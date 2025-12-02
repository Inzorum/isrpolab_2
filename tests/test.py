import unittest
import math

import rectangle
import square
import circle
import triangle

# ТЕСТЫ ДЛЯ ПРЯМОУГОЛЬНИКА

class RectangleTestCase(unittest.TestCase):

    def test_area_zero_height(self):
        """ проверяем площадь: если одна сторона = 0 -> результат 0 """
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_normal(self):
        """ проверяем площадь: обычный случай -> 3 * 4 = 12 """
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_area_small_floats(self):
        """ проверяем площадь: маленькие числа -> 0.001 * 0.002 = 0.000002 """
        self.assertAlmostEqual(rectangle.area(0.001, 0.002), 0.000002)

    def test_area_large_numbers(self):
        """ проверяем площадь: большие числа -> 1_000_000 * 2_000_000 = 2e12 """
        self.assertEqual(rectangle.area(1_000_000, 2_000_000), 2_000_000_000_000)

    def test_perimeter_zero_sides(self):
        """ проверяем периметр: стороны 0 и 0 -> результат 0 """
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_normal(self):
        """ проверяем периметр: обычный случай -> 3 + 4 + 3 + 4 = 14 """
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_perimeter_small_floats(self):
        """ проверяем периметр: маленькие числа -> 0.001 + 0.002 + 0.001 + 0.002 = 0.006 """
        self.assertAlmostEqual(rectangle.perimeter(0.001, 0.002), 0.006)

    def test_perimeter_large_numbers(self):
        """ проверяем периметр: большие числа -> 2 * (1e6 + 2e6) = 6e6 """
        self.assertEqual(rectangle.perimeter(1_000_000, 2_000_000), 6_000_000)


# ТЕСТЫ ДЛЯ КВАДРАТА

class SquareTestCase(unittest.TestCase):

    def test_area_zero(self):
        """ проверяем площадь: сторона 0 -> площадь 0 """
        self.assertEqual(square.area(0), 0)

    def test_area_normal(self):
        """ проверяем площадь: обычный случай -> 5 * 5 = 25 """
        self.assertEqual(square.area(5), 25)

    def test_area_small_float(self):
        """ проверяем площадь: маленькое число -> 0.01 * 0.01 = 0.0001 """
        self.assertAlmostEqual(square.area(0.01), 0.0001)

    def test_area_large_numbers(self):
        """ проверяем площадь: большая сторона -> (1e6)^2 = 1e12 """
        self.assertEqual(square.area(1_000_000), 1_000_000_000_000)

    def test_perimeter_zero(self):
        """ проверяем периметр: сторона 0 -> результат 0 """
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_normal(self):
        """ проверяем периметр: обычный случай -> 5 * 4 = 20 """
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_small_float(self):
        """ проверяем периметр: маленькое число -> 0.01 * 4 = 0.04 """
        self.assertAlmostEqual(square.perimeter(0.01), 0.04)

    def test_perimeter_large_numbers(self):
        """ проверяем периметр: большая сторона -> 4 * 1e6 = 4e6 """
        self.assertEqual(square.perimeter(1_000_000), 4_000_000)


# ТЕСТЫ ДЛЯ КРУГА

class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        """ проверяем площадь: радиус 0 -> площадь 0 """
        self.assertEqual(circle.area(0), 0)

    def test_area_normal(self):
        """ проверяем площадь: радиус 1 -> π """
        self.assertEqual(circle.area(1), math.pi)

    def test_area_small_float(self):
        """ проверяем площадь: маленький радиус -> π * (0.001^2) """
        self.assertAlmostEqual(circle.area(0.001), math.pi * 1e-6)

    def test_area_large_numbers(self):
        """ проверяем площадь: большой радиус -> π * (1e6)^2 = π * 1e12 """
        self.assertEqual(circle.area(1_000_000), math.pi * 1_000_000_000_000)

    def test_perimeter_zero(self):
        """ проверяем периметр: радиус 0 -> результат 0 """
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_normal(self):
        """ проверяем периметр: радиус 1 -> 2π """
        self.assertEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_small_float(self):
        """ проверяем периметр: маленький радиус -> 2π * 0.001 """
        self.assertAlmostEqual(circle.perimeter(0.001), 2 * math.pi * 0.001)

    def test_perimeter_large_numbers(self):
        """ проверяем периметр: большой радиус -> 2π * 1e6 """
        self.assertEqual(circle.perimeter(1_000_000), 2 * math.pi * 1_000_000)


# ТЕСТЫ ДЛЯ ТРЕУГОЛЬНИКА

class TriangleTestCase(unittest.TestCase):

    def test_area_simple(self):
        """ проверяем площадь: основание 1 и высота 1 -> 1 * 1 / 2 = 0.5 """
        self.assertEqual(triangle.area(1, 1), 0.5)

    def test_area_normal(self):
        """ проверяем площадь: обычный случай -> 10 * 5 / 2 = 25 """
        self.assertEqual(triangle.area(10, 5), 25)

    def test_area_small_floats(self):
        """ проверяем площадь: маленькие числа -> 0.001 * 0.002 / 2 = 0.000001 """
        self.assertAlmostEqual(triangle.area(0.001, 0.002), 0.000001)

    def test_area_large_numbers(self):
        """ проверяем площадь: большие числа -> 1e6 * 2e6 / 2 = 1e12 """
        self.assertEqual(triangle.area(1_000_000, 2_000_000), 1_000_000_000_000)

    def test_perimeter_simple(self):
        """ проверяем периметр: 1 + 1 + 1 -> 3 """
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)

    def test_perimeter_normal(self):
        """ проверяем периметр: обычный случай -> 3 + 4 + 5 = 12 """
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_small_floats(self):
        """ проверяем периметр: маленькие числа -> 0.001 + 0.002 + 0.003 = 0.006 """
        self.assertAlmostEqual(triangle.perimeter(0.001, 0.002, 0.003), 0.006)

    def test_perimeter_large_numbers(self):
        """ проверяем периметр: большие стороны -> 1e6 + 2e6 + 3e6 = 6e6 """
        self.assertEqual(triangle.perimeter(1_000_000, 2_000_000, 3_000_000), 6_000_000)


if __name__ == "__main__":
    unittest.main()