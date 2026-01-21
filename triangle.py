def area(a, h):
    """
    Вычисляет площадь треугольника по длине основания и высоте.

    Параметры:
    a (float): длина основания треугольника.
    h (float): высота треугольника.

    Возвращает:
    float: площадь треугольника.

    Пример вызова:
    >>> area(4, 5)
    10.0
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Основание и высота должны быть числами")
    if a < 0 or h < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * a * h

def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника по длинам его сторон.

    Параметры:
    a (float): длина первой стороны треугольника.
    b (float): длина второй стороны треугольника.
    c (float): длина третьей стороны треугольника.

    Возвращает:
    float: периметр треугольника.

    Пример вызова:
    >>> perimeter(3, 4, 5)
    12
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a + b + c