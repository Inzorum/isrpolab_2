import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),  "..", "src"))

from src.rectangle import area, perimeter

class TestRectangeFunctions(unittest.TestCase):
    
    def test_area_positive(self):
        self.assertEqual(area(2, 2), 4)

    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)    

    def test_area_negative(self):
      with self.assertRaises(ValueError):
        area(-10, -10)
        area(10, -10)

    def test_area_type(self):
      with self.assertRaises(TypeError):
        area("10", "10")
        area(True, True)
        area(None, None)
    
    def test_area_return_type(self):
      self.assertIsInstance(area(1, 10), int)
      self.assertIsInstance(area(2, 10), int)
      self.assertIsInstance(area(10, 10), int)

    def test_area_large_number(self):
       self.assertEqual(area(10000000000000, 10000000000000), 10000000000000 ** 2)

    def test_area_small_number(self):
       self.assertEqual(area(1e-6, 1e-6), 1e-6 * 1e-6)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2, 2), 8)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_negative(self):
      with self.assertRaises(ValueError):
        perimeter(-10, 10)
        perimeter(10, -10)
        perimeter(-10, -10)

    def test_perimeter_type(self):
      with self.assertRaises(TypeError):
        perimeter("10", "10")
        perimeter(True, False)
        perimeter(None, None)

    def test_perimeter_return_type(self):
      self.assertIsInstance(perimeter(4, 1), int)
      self.assertIsInstance(perimeter(2, 1), int)
      self.assertIsInstance(perimeter(10, 1), int)
      self.assertIsInstance(perimeter(1121, 1), int)

    def test_perimeter_large_number(self):
       self.assertEqual(perimeter(10000000000000, 10000000000000), 2*10000000000000 * 2)

    def test_perimeter_small_number(self):
       self.assertEqual(perimeter(1e-6, 1e-6), 2* 1e-6 * 2)
    


if __name__ == '__main__':
    unittest.main()