def area(a, h):
    '''
    Возвращает площадь треугольника.

    Параметры:
        a (float): длина основания
        b (float): высота треугольник

    Возвращаемое значение:
        float: площадь треугольника
    '''
    return a * h

def perimetr(a, b, c):
    '''

    Возвращает периметр треугольника.

    Параметры:
        a (float): длина первой стороны
        b (float): длина второй стороны
        c (float): длина третьей стороны


    Возвращаемое значние:
        float: периметр треугольника
    '''
    sides = [a, b, c]
    for i in range(0, len(sides)):
        if sides[i] >= sides[i - 1] + sides[i - 2]:
            return "Any side can't be more than summary of another two"
    return a + b + c
