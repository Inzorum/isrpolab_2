def area(a, b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Стороны могут быть только действительными числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    ''' Принимает числа a и b, возвращает произведение a на b'''
    return a * b


def perimeter(a,b):
    if (type(a) not in [int, float]) or (type(b) not in [int, float]):
        raise TypeError("Стороны могут быть только действительными числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    ''' Принимает числа a и b, возвращает удвоенную сумму a на b'''
    return 2 * (a + b)


    