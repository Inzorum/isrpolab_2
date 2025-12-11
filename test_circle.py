import unittest
from circle import area, perimeter
import math


class CircleTestCase(unittest.TestCase):
    """Набор юнит‑тестов для функций вычисления площади и периметра круга."""

    def test_area(self):
        """Проверяет, что функция area(r) правильно вычисляет площадь круга π * r * r."""
        self.assertAlmostEqual(area(0), 0.0)
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter(self):
        """Проверяет, что функция perimeter(r) правильно вычисляет длину окружности 2π * r."""
        self.assertAlmostEqual(perimeter(0), 0.0)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)


if __name__ == "__main__":
    # Запускает выполнение всех тестов только при прямом запуске этого файла,
    # а при импорте модуля тесты автоматически не запускаются.
    unittest.main()
