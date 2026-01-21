import unittest
from square import area, perimeter


class TestGeometric(unittest.TestCase):

    # ТЕСТЫ ДЛЯ area()
    def test_area_zero(self):
        """Площадь при стороне 0 должна быть 0"""
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        """Площадь при положительном числе"""
        self.assertEqual(area(5), 25)

    def test_area_one(self):
        """Площадь квадрата со стороной 1"""
        self.assertEqual(area(1), 1)



    #ТЕСТЫ ДЛЯ perimeter() 
    def test_perimeter_zero(self):
        """Периметр при стороне 0 должен быть 0"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        """Периметр при положительной стороне"""
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_one(self):
        """Периметр при стороне 1"""
        self.assertEqual(perimeter(1), 4)


if __name__ == '__main__':
    unittest.main()
#запускаються через 
# python3 -m unittest UnitTests.py