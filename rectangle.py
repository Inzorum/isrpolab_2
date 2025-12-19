def area(a, b):
    """
    Вычисляет площадь прямоугольника по длинам его сторон.

    Параметры:
    a (float): длина первой стороны прямоугольника.
    b (float): длина второй стороны прямоугольника.

    Возвращает:
    float: площадь прямоугольника.

    Пример вызова:
    >>> area(4, 5)
    20
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника по длинам его сторон.

    Параметры:
    a (float): длина первой стороны прямоугольника.
    b (float): длина второй стороны прямоугольника.

    Возвращает:
    float: периметр прямоугольника.

    Пример вызова:
    >>> perimeter(4, 5)
    18
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)

