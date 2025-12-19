
def area(a):
    """
    Вычисляет площадь квадрата по длине его стороны.

    Параметры:
    a (float): длина стороны квадрата.

    Возвращает:
    float: площадь квадрата.

    Пример вызова:
    >>> area(4)
    16
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата по длине его стороны.

    Параметры:
    a (float): длина стороны квадрата.

    Возвращает:
    float: периметр квадрата.

    Пример вызова:
    >>> perimeter(4)
    16
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    return 4 * a






