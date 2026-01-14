import unittest
from triangle import area, perimeter 


class TestTriangle(unittest.TestCase): 
    # Функции для произведения
    def test_area_tr(self):
        self.assertEqual(area(7,5), 7*5/2)
        self.assertEqual(area(10**10,2), 2*(10**10)/2)
        self.assertEqual(area(0,5), 0)
        self.assertEqual(area(1,1), 1/2)
        self.assertEqual(area(1.5,2.3), 2.3*1.5/2)

    def test_value_tr(self):
        self.assertRaises(ValueError, area, -1, 4)
        self.assertRaises(ValueError, area, 10, -10.8)
        self.assertRaises(ValueError, area, -10, -10.8)

    def test_type_tr(self):
        self.assertRaises(TypeError, area, [1], [2])
        self.assertRaises(TypeError, area, False, False) 
        self.assertRaises(TypeError, area, "Я буду жаловаться!!!", "Поняли???")
        self.assertRaises(TypeError, area, "5", 2)
        self.assertRaises(TypeError, area, {1}, 2) 
        self.assertRaises(TypeError, area, (1,2), 2) 
        self.assertRaises(TypeError, area, 1+4j, 2 )
        self.assertRaises(TypeError, area, {'key': 1}, 2) 
        self.assertRaises(TypeError, area, None, 3) 

    # Функции для периметра
    def test_perimeter_tr(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10, 10, 10), 30)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(1, 2, 3), 6)
        self.assertEqual(perimeter(2.5, 3.5, 4.0), 10.0)
        self.assertEqual(perimeter(10**5, 10**5, 10**5), 3 * 10**5)

    def test_value_tr_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, 2, 3)
        self.assertRaises(ValueError, perimeter, 1, -2, 3)
        self.assertRaises(ValueError, perimeter, 1, 2, -3)
        self.assertRaises(ValueError, perimeter, -1, -2, -3)
        self.assertRaises(ValueError, perimeter, -5, 10, -15)

    def test_type_tr_perimeter(self):
        self.assertRaises(TypeError, perimeter, [1], 2, 3)
        self.assertRaises(TypeError, perimeter, 1, [2], 3)
        self.assertRaises(TypeError, perimeter, 1, 2, [3])
        self.assertRaises(TypeError, perimeter, "1", 2, 3)
        self.assertRaises(TypeError, perimeter, 2, "Где поддержка??", "ААААААААА")
        self.assertRaises(TypeError, perimeter, False, 2, 3)
        self.assertRaises(TypeError, perimeter, {1}, 2, 3)
        self.assertRaises(TypeError, perimeter, 1, 2, (3,))
        self.assertRaises(TypeError, perimeter, 1+4j, 2, 3)
        self.assertRaises(TypeError, perimeter, 2, {'key': 1}, 2)
        self.assertRaises(TypeError, perimeter, None, 2, 3)
        
if __name__ == '__main__':
    unittest.main()