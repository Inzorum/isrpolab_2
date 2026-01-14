import unittest
from circle import area, perimeter 
from math import pi


# Создаем класс для функции нахождения площади
class TestCircleArea(unittest.TestCase): 
    # Функции для площади
    # Функция проверки валидных элементов
    def test_area(self):
        # assertEqual - функция отслеживающая равенство двух значений
        self.assertEqual(area(7), pi*7**2)
        self.assertEqual(area(10**10), pi*(10**10)**2)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), pi)
        self.assertEqual(area(1.5), pi*1.5**2)

    # Функция проверки работы с отрицательными числами
    def test_value(self):
        # assertRaises - функция вызывает определенную ошибку
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -10.8)
    
    # Функция проверки невалидного типа
    def test_type(self):
        self.assertRaises(TypeError, area, [1])
        self.assertRaises(TypeError, area, False) # bool
        self.assertRaises(TypeError, area, "Дай мне площадь круга с радиусам 2")
        self.assertRaises(TypeError, area, "5")
        self.assertRaises(TypeError, area, {1}) # множество
        self.assertRaises(TypeError, area, (1,2)) # кортеж
        self.assertRaises(TypeError, area, 1+4j)
        self.assertRaises(TypeError, area, {'key': 1}) # словарь
        self.assertRaises(TypeError, area, None) # специальный объект, который означает ничего

    # Функции для периметра
    def test_perimeter(self):
        self.assertEqual(perimeter(7), pi*7*2)
        self.assertEqual(perimeter(10**10), pi*(10**10)*2)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 2*pi)
        self.assertEqual(perimeter(1.5), pi*1.5*2)

    def test_value_self(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -10.8)
    
    def test_type_self(self):
        self.assertRaises(TypeError, perimeter, [1])
        self.assertRaises(TypeError, perimeter, False) 
        self.assertRaises(TypeError, perimeter, "... машина, ... уже  на площадь, дай хотя бы периметр круга с радиусам 2")
        self.assertRaises(TypeError, perimeter, "5")
        self.assertRaises(TypeError, perimeter, {1}) 
        self.assertRaises(TypeError, perimeter, (1,2))
        self.assertRaises(TypeError, perimeter, 1+4j)
        self.assertRaises(TypeError, perimeter, {'key': 1}) 
        self.assertRaises(TypeError, perimeter, None) 
#Запуск тестов только при прямом выполнение файла        
if __name__ == '__main__':
    unittest.main()
