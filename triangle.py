def area(a, h):
    '''Принимает сторону треугольника a и высоту опушенную на a - h, возвращает площадь треугольника'''
    if (a < 0 or h < 0):
        return False
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает стороны треугольника a,b,c и выводит периметр треугольника'''
    if (a < 0 or b < 0 or c < 0):
        return False
    return a + b + c

print(area(4, 3))
print(perimeter(4, 3, 5))