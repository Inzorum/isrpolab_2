import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(0),0.0)
        self.assertEqual(area(4),50.26548245743669)
        self.assertEqual(area(100), 31415.926535897932)
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 25.132741228718345)
        self.assertEqual(perimeter(100), 628.3185307179587)
        self.assertEqual(perimeter(0), 0.0)
    def test_area_negative(self):
        if(self.assertFalse(area(-10))==False):
            self.fail("Площадь не должна быть отрицательной")
    def test_perimeter_negative(self):
        if(self.assertFalse(perimeter(-10))==False):
            self.fail("Периметр не должен быть отрицательным")
    if  __name__ == '__main__':
        unittest.main()
