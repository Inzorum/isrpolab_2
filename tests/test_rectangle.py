import unittest
from rectangle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(0,0),0.0)
        self.assertEqual(area(3,4),12)
        self.assertEqual(area(100,100), 10000)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3,4), 14)
        self.assertEqual(perimeter(100,100), 400)
        self.assertEqual(perimeter(0,0), 0.0)
    def test_area_negative(self):
        if(self.assertFalse(area(0,-10))==False):
            self.fail("Площадь не должна быть отрицательной")
    def test_perimeter_negative(self):
        if(self.assertFalse(perimeter(0,-10))==False):
            self.fail("Периметр не должен быть отрицательным")
    if __name__ == '__main__':
        unittest.main()
