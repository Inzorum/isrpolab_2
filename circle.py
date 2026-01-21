import math;

def area(r):
    '''
    Возвращает площадь окружности (float)
    
    Принимает значение r, где r (int) - радиус окружности
    
    Пример вызова:
    res = area(5)
    print(res)
    >> 78.5
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности (float)
    
    Принимает значение r, где r (int) - радиус окружности
    
    Пример вызова:
    c = perimeter(3)
    print(c)
    >> 18.84
    '''
    return 2 * math.pi * r


#for tests