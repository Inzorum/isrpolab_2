import math


def area(r):
    """Функция возвращает площадь круга по формуле pi*r**2"""
    if (r<0):
        return False
    return math.pi * r * r
def perimeter(r):
    """Функция возвращает периметр круга по формуле 2*pi*r"""
    if (r<0):
        return False
    return 2 * math.pi * r

print(area(4))
print(area(100))
print(perimeter(4))

print(perimeter(100))