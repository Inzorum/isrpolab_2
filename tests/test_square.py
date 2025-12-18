import unittest
from square import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(0),0)
        self.assertEqual(area(3),9)
        self.assertEqual(area(100), 10000)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(100), 400)
        self.assertEqual(perimeter(0), 0.0)
    def test_area_negative(self):
        if(self.assertFalse(area(-10))==False):
            self.fail("Площадь не должна быть отрицательной")
    def test_perimeter_negative(self):
        if(self.assertFalse(perimeter(-12))==False):
            self.fail("Периметр не должен быть отрицательным")
    if __name__ == '__main__':
        unittest.main()
