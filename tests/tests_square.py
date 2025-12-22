import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    # Класс с модульными тестами для функций area() и perimeter(),
    # которые считают площадь и периметр квадрата по длине стороны.

    def test_area_zero(self):
        # Тест 1: проверяем, что площадь квадрата со стороной 0 равна 0.
        # Ожидаемое значение: area(0) == 0.
        self.assertEqual(area(0), 0)

    def test_area_positive_int(self):
        # Тест 2: проверяем площадь квадрата с целочисленной стороной.
        # Ожидаемое значение: area(5) == 25.
        self.assertEqual(area(5), 25)

    def test_area_positive_float(self):
        # Тест 3: проверяем площадь квадрата с вещественной (дробной) стороной.
        # Ожидаемое значение: area(2.5) == 6.25.
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter_zero(self):
        # Тест 4: проверяем, что периметр квадрата со стороной 0 равен 0.
        # Ожидаемое значение: perimeter(0) == 0.
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_int(self):
        # Тест 5: проверяем периметр квадрата с целочисленной стороной.
        # Ожидаемое значение: perimeter(5) == 20.
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_positive_float(self):
        # Тест 6: проверяем периметр квадрата с вещественной стороной.
        # Ожидаемое значение: perimeter(2.5) == 10.0.
        self.assertAlmostEqual(perimeter(2.5), 10.0)


if __name__ == "__main__":
    unittest.main()
