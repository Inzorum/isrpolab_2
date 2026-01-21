import math


def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Параметры:
    r (float): радиус круга.

    Возвращает:
    float: площадь круга.

    Пример вызова:
    >>> area(3)
    28
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга) по радиусу.

    Параметры:
    r (float): радиус круга.

    Возвращает:
    float: длина окружности.

    Пример вызова:
    >>> perimeter(3)
    18
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r