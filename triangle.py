def area(a, h):
    if (type(a) not in [int,float]) or (type(h) not in [int,float]):
        raise TypeError("Стороны могут быть только  действительными числами")
    if a < 0 or (h < 0):
        raise ValueError("Основание и высота не могут быть орицательными")
    ''' 
    Возвращает площадь треугольника.

    Параметры:
        a (float): длина основания
        b (float): высота треугольника

    Возвращаемое значение:
        float: площадь треугольника
    '''
    return a * h / 2


def perimeter(a, b, c):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]) or (type(c) not in [int, float]):
        raise TypeError("Стороны могут быть только действительными числами")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    ''' 
    Возвращает периметр треугольника.

    Параметры:
        a (float): длина первой стороны
        b (float): длина второй стороны
        c (float): длина третий стороны

    Возвращаемое значение:
        float: периметр треугольника
    '''
    return a + b + c




