import unittest
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),  "..", "src"))

from src.circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):
    
    def test_area_positive(self):
        self.assertEqual(area(2), math.pi * 4)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
      self.assertEqual(area(1), math.pi)

    def test_area_negative(self):
      with self.assertRaises(ValueError):
        area(-10)
        area(-999)
        area(-1)

    def test_area_type(self):
      with self.assertRaises(TypeError):
        area("10")
        area(True)
        area(None)
    
    def test_area_return_type(self):
      self.assertIsInstance(area(1), float)
      self.assertIsInstance(area(2), float)
      self.assertIsInstance(area(10), float)
      self.assertIsInstance(area(1121), float)

    def test_area_large_number(self):
       self.assertEqual(area(10000000000000), math.pi * 10000000000000 ** 2)

    def test_area_small_number(self):
       self.assertEqual(area(1e-6), math.pi * 1e-6 * 1e-6)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2), math.pi * 4)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
      self.assertEqual(perimeter(1), 2*math.pi)

    def test_perimeter_negative(self):
      with self.assertRaises(ValueError):
        perimeter(-10)
        perimeter(-999)
        perimeter(-1)

    def test_perimeter_type(self):
      with self.assertRaises(TypeError):
        perimeter("10")
        perimeter(True)
        perimeter(None)

    def test_perimeter_return_type(self):
      self.assertIsInstance(perimeter(1), float)
      self.assertIsInstance(perimeter(2), float)
      self.assertIsInstance(perimeter(10), float)
      self.assertIsInstance(perimeter(1121), float)

    def test_perimeter_large_number(self):
       self.assertEqual(perimeter(10000000000000), math.pi * 10000000000000 * 2)

    def test_perimeter_small_number(self):
       self.assertEqual(perimeter(1e-6), math.pi * 1e-6 * 2)