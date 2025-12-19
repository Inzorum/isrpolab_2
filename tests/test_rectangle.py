import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        """Тест площади прямоугольника, когда вторая сторона равна нулю"""
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_first(self):
        """Тест площади прямоугольника, когда первая сторона равна нулю"""
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_both_zero(self):
        """Тест площади прямоугольника, когда обе стороны равны нулю"""
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        """Тест площади квадрата (прямоугольник с равными сторонами)"""
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_one(self):
        """Тест площади прямоугольника со стороной равной единице"""
        res = area(1, 5)
        self.assertEqual(res, 5)

    def test_area_both_one(self):
        """Тест площади прямоугольника с обеими сторонами равными единице"""
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_area_positive(self):
        """Тест площади прямоугольника с положительными сторонами"""
        res = area(4, 5)
        self.assertEqual(res, 20)

    def test_area_float(self):
        """Тест площади прямоугольника с дробными сторонами"""
        res = area(2.5, 3.5)
        self.assertAlmostEqual(res, 8.75, places=5)

    def test_area_large(self):
        """Тест площади прямоугольника с большими сторонами"""
        res = area(100, 200)
        self.assertEqual(res, 20000)

    def test_area_negative_first(self):
        """Тест площади прямоугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_area_negative_second(self):
        """Тест площади прямоугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError):
            area(10, -5)

    def test_area_both_negative(self):
        """Тест площади прямоугольника с обеими отрицательными сторонами"""
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_area_string_first(self):
        """Тест площади прямоугольника со строковой первой стороной"""
        with self.assertRaises(TypeError):
            area("5", 10)

    def test_area_string_second(self):
        """Тест площади прямоугольника со строковой второй стороной"""
        with self.assertRaises(TypeError):
            area(10, "5")

    def test_area_both_string(self):
        """Тест площади прямоугольника с обеими строковыми сторонами"""
        with self.assertRaises(TypeError):
            area("5", "10")

    def test_perimeter_zero(self):
        """Тест периметра прямоугольника, когда первая сторона равна нулю"""
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_perimeter_both_zero(self):
        """Тест периметра прямоугольника, когда обе стороны равны нулю"""
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_square(self):
        """Тест периметра квадрата (прямоугольник с равными сторонами)"""
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_one(self):
        """Тест периметра прямоугольника со стороной равной единице"""
        res = perimeter(1, 5)
        self.assertEqual(res, 12)

    def test_perimeter_both_one(self):
        """Тест периметра прямоугольника с обеими сторонами равными единице"""
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_positive(self):
        """Тест периметра прямоугольника с положительными сторонами"""
        res = perimeter(4, 5)
        self.assertEqual(res, 18)

    def test_perimeter_float(self):
        """Тест периметра прямоугольника с дробными сторонами"""
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

    def test_perimeter_large(self):
        """Тест периметра прямоугольника с большими сторонами"""
        res = perimeter(100, 200)
        self.assertEqual(res, 600)

    def test_perimeter_negative_first(self):
        """Тест периметра прямоугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)

    def test_perimeter_negative_second(self):
        """Тест периметра прямоугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError):
            perimeter(10, -5)

    def test_perimeter_both_negative(self):
        """Тест периметра прямоугольника с обеими отрицательными сторонами"""
        with self.assertRaises(ValueError):
            perimeter(-5, -10)

    def test_perimeter_string_first(self):
        """Тест периметра прямоугольника со строковой первой стороной"""
        with self.assertRaises(TypeError):
            perimeter("5", 10)

    def test_perimeter_string_second(self):
        """Тест периметра прямоугольника со строковой второй стороной"""
        with self.assertRaises(TypeError):
            perimeter(10, "5")

    def test_perimeter_both_string(self):
        """Тест периметра прямоугольника с обеими строковыми сторонами"""
        with self.assertRaises(TypeError):
            perimeter("5", "10")


if __name__ == '__main__':
    unittest.main()
