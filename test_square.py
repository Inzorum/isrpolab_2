import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    # Тесты для площади квадрата
    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2.5), 6.25)
        self.assertEqual(area(10**5), 10**10)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5)
        self.assertRaises(ValueError, area, -2.5)

    def test_invalid_types_area(self):
        self.assertRaises(TypeError, area, [5])
        self.assertRaises(TypeError, area, "5")
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, {5})
        self.assertRaises(TypeError, area, (5,))
        self.assertRaises(TypeError, perimeter, "Ладною дам последний шанс: назови площадь квадрата")
        self.assertRaises(TypeError, perimeter, 5+2j)
        self.assertRaises(TypeError, perimeter, {'key': 1})
        self.assertRaises(TypeError, perimeter, None)

    # Тесты для периметра квадрата
    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2.5), 10.0)
        self.assertEqual(perimeter(10**5), 4 * 10**5)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5)
        self.assertRaises(ValueError, perimeter, -10)
        self.assertRaises(ValueError, perimeter, -2.5)
        self.assertRaises(ValueError, perimeter, -0.1)

    def test_invalid_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, [5])
        self.assertRaises(TypeError, perimeter, "5")
        self.assertRaises(TypeError, perimeter, True)
        self.assertRaises(TypeError, perimeter, {5})
        self.assertRaises(TypeError, perimeter, (5,))
        self.assertRaises(TypeError, perimeter, "С меня хватит, пока ...")
        self.assertRaises(TypeError, perimeter, 5+2j)
        self.assertRaises(TypeError, perimeter, {'key': 1})
        self.assertRaises(TypeError, perimeter, None)

if __name__ == '__main__':
    unittest.main()