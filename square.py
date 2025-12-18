
def area(a):
    """ Принимает сторону квадрата a и возвращает его площадь """
    if (a<0):
        return False
    return a * a


def perimeter(a):
    """ Принимает сторону квадрата и возвращает его периметр"""
    if (a<0):
        return False
    return 4 * a

print(area(4))
print(perimeter(3))