import unittest
from rectangle import area, perimeter


class TestRectangle(unittest.TestCase):
    # Тесты для площади прямоугольника
    def test_area(self):
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(2.5, 4.0), 10.0)
        self.assertEqual(area(10**5, 10**5), 10**10)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5, 3)
        self.assertRaises(ValueError, area, 5, -3)
        self.assertRaises(ValueError, area, -5, -3)
        self.assertRaises(ValueError, area, -2.5, 4.0)

    def test_invalid_types_area(self):
        self.assertRaises(TypeError, area, [5], 3)
        self.assertRaises(TypeError, area, 5, [3])
        self.assertRaises(TypeError, area, "5", 3)
        self.assertRaises(TypeError, area, False, 3)
        self.assertRaises(TypeError, area, "Я устал...", 3)
        self.assertRaises(TypeError, area, {5}, 3)
        self.assertRaises(TypeError, area, (5,), 3)
        self.assertRaises(TypeError, area, 5+2j, 3)
        self.assertRaises(TypeError, perimeter, 2, {'key': 1}, 2)
        self.assertRaises(TypeError, area, None, 3)

    # Тесты для периметра прямоугольника
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(2.5, 4.0), 13.0)
        self.assertEqual(perimeter(10**5, 10**5), 4 * 10**5)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5, 3)
        self.assertRaises(ValueError, perimeter, 5, -3)
        self.assertRaises(ValueError, perimeter, -5, -3)
        self.assertRaises(ValueError, perimeter, -2.5, 4.0)

    def test_invalid_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, [5], 3)
        self.assertRaises(TypeError, perimeter, 5, [3])
        self.assertRaises(TypeError, perimeter, "5", 3)
        self.assertRaises(TypeError, perimeter, 5, "Уже 3:20 ...")
        self.assertRaises(TypeError, perimeter, False, 3)
        self.assertRaises(TypeError, perimeter, {5}, 3)
        self.assertRaises(TypeError, perimeter, (5,), 3)
        self.assertRaises(TypeError, perimeter, 5+2j, 3)
        self.assertRaises(TypeError, perimeter, 2, {'key': 1}, 2)
        self.assertRaises(TypeError, perimeter, None, 3)

if __name__ == '__main__':
    unittest.main()
    