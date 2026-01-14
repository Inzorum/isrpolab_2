
def area(a):
    if type(a) not in [int, float]:
        raise TypeError("Сторона может быть только действительным числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    ''' Принимается число a, возвращает произведение a на a (площадь квадрата)'''
    return a * a


def perimeter(a):
    if type(a) not in [int, float]:
        raise TypeError("Сторона может быть только действительным числом")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной")
    ''' Принимается число a, возвращает произведение 4 на a (периметр квадрата)'''
    return 4 * a

