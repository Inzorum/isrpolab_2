import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),  "..", "src"))

from src.triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(area(6, 4), 12)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_one(self):
        self.assertEqual(area(1, 1), 0.5)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)
            area(5, -10)
            area(-10, -5)

    def test_area_type(self):
        with self.assertRaises(TypeError):
            area("10", 5)
            area(10, "5")
            area(10, None)
    
    def test_area_return_type(self):
        self.assertIsInstance(area(1, 1), (int, float))
        self.assertIsInstance(area(2, 3), (int, float))
        self.assertIsInstance(area(10, 5), (int, float))
        self.assertIsInstance(area(1121, 500), (int, float))

    def test_area_large_number(self):
        self.assertEqual(area(10000000000000, 10000000000000), 10000000000000 * 10000000000000 / 2)

    def test_area_small_number(self):
        self.assertEqual(area(1e-6, 1e-6), 1e-6 * 1e-6 / 2)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(5, 0, 5), 10)
        self.assertEqual(perimeter(5, 5, 0), 10)

    def test_perimeter_one(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 5, 5)
            perimeter(5, -10, 5)
            perimeter(5, 5, -10)
            perimeter(-10, -5, -3)

    def test_perimeter_type(self):
        with self.assertRaises(TypeError):
            perimeter("10", 5, 5)
            perimeter(10, "5", 5)
            perimeter(10, 5, "5")
            perimeter(10, None, 5)

    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(1, 1, 1), (int, float))
        self.assertIsInstance(perimeter(2, 3, 4), (int, float))
        self.assertIsInstance(perimeter(10, 5, 8), (int, float))
        self.assertIsInstance(perimeter(1121, 500, 800), (int, float))

    def test_perimeter_large_number(self):
        self.assertEqual(perimeter(10000000000000, 10000000000000, 10000000000000), 10000000000000 * 3)

    def test_perimeter_small_number(self):
        self.assertEqual(perimeter(1e-6, 1e-6, 1e-6), 1e-6 * 3)
    

if __name__ == '__main__':
    unittest.main()