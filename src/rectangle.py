def area(a, b):
    """
    Вычисляет площадь прямоугольника по заданным сторонам.
        Параметры:
            a (float): Длина первой стороны прямоугольника.
            b (float): Длина второй стороны прямоугольника.
        Возвращает:
            float: Площадь прямоугольника.
        Примеры:
            area(3, 4) // 12
    """

    if(not isinstance(a, (float, int)) or not isinstance(b, (float, int))):
        raise TypeError("Ожидается int или float")

    if(a < 0 or b < 0):
        raise ValueError("Число не может быть отрицательным")
    
    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника по заданным сторонам.
        Параметры:
            a (float): Длина первой стороны прямоугольника.
            b (float): Длина второй стороны прямоугольника.
        Возвращает:
            float: Периметр прямоугольника.
        Примеры:
            perimeter(3, 4) // 14
    """
    
    if(not isinstance(a, (float, int)) or not isinstance(b, (float, int))):
        raise TypeError("Ожидается int или float")

    if(a < 0 or b < 0):
        raise ValueError("Число не может быть отрицательным")
    
    return 2 * (a + b)