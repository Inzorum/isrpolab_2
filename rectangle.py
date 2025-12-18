def area(a, b):
    '''Принимает стороны прямоугольника a, b и выводит площадь прямоугольника'''
    if (a<0 or b <0):
        return False
    return a * b

def perimeter(a, b):
    ''' Принимает стороны прямоугольника a,b и выводит периметр прямоугольника'''
    if (a<0 or b<0):
        return False
    return 2*(a + b)

print(area(100, 100))
print(perimeter(100, 100))