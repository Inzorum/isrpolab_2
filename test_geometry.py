import unittest
import math

from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestSquare(unittest.TestCase):
    
    def test_area_positive_integer(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(10), 100)
        
    def test_area_positive_float(self):
        self.assertAlmostEqual(square_area(2.5), 6.25)
        self.assertAlmostEqual(square_area(3.14), 9.8596, places=4)
        
    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)
        
    def test_perimeter_positive_integer(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)
        
    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(square_perimeter(2.5), 10.0)
        self.assertAlmostEqual(square_perimeter(3.14), 12.56, places=2)
        
    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
        

class TestRectangle(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(10, 4), 40)
        
    def test_area_positive_floats(self):
        self.assertAlmostEqual(rectangle_area(2.5, 4), 10.0)
        self.assertAlmostEqual(rectangle_area(3.14, 2.1), 6.594, places=3)
        
    def test_area_zero(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)
        
    def test_perimeter_positive_integers(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(10, 4), 28)
        
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(rectangle_perimeter(2.5, 4), 13.0)
        self.assertAlmostEqual(rectangle_perimeter(3.14, 2.1), 10.48, places=2)
        
    def test_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(5, 0), 10)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        

class TestTriangle(unittest.TestCase):
    
    def test_area_positive_integers(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(6, 4), 12)
        
    def test_area_positive_floats(self):
        self.assertAlmostEqual(triangle_area(5.5, 3.2), 8.8)
        self.assertAlmostEqual(triangle_area(7.25, 4.1), 14.8625)
        
    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)
            
    def test_perimeter_positive_integers(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
        self.assertEqual(triangle_perimeter(7, 8, 9), 24)
        
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5)
        self.assertAlmostEqual(triangle_perimeter(1.1, 2.2, 3.3), 6.6)
        
    def test_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
        self.assertEqual(triangle_perimeter(3, 0, 5), 8)
        self.assertEqual(triangle_perimeter(3, 4, 0), 7)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        

class TestCircle(unittest.TestCase):
    
    def test_area_positive_integer(self):
        expected = math.pi * 5 * 5
        self.assertAlmostEqual(circle_area(5), expected)
        self.assertAlmostEqual(circle_area(1), math.pi)
        
    def test_area_positive_float(self):
        expected = math.pi * 2.5 * 2.5
        self.assertAlmostEqual(circle_area(2.5), expected)
        self.assertAlmostEqual(circle_area(0.5), math.pi * 0.25)
        
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)
        
    def test_perimeter_positive_integer(self):
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(circle_perimeter(5), expected)
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        
    def test_perimeter_positive_float(self):
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(circle_perimeter(2.5), expected)
        self.assertAlmostEqual(circle_perimeter(0.5), math.pi)
        
    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)


unittest.main(verbosity=2)