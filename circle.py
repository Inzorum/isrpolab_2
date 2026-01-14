import math


def area(r):
    # type - встроенная функция,возвращающая тип объекта
    if type(r) not in [int,float]:
        # raise - ключевое слова для создания исключений
        raise TypeError("Радиус может быть только неотрицательным действительным числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательный")
    ''' Принимается число r, возвращает pi*r^2(площадь круга)'''
    return math.pi * r * r


def perimeter(r):
    if type(r) not in [int,float]:
        raise TypeError("Радиус может быть только неотрицательным действительным числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательный")
    ''' Принимается число r, возвращает 2*pi*r(периметр круга)'''
    return 2 * math.pi * r

