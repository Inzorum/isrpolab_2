import math


def area(r):
    '''
    Находит площадь круга
    
        Параметры:
        r (float): радиус
        
        Возвращаемое значение:
        area (float): площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Находит периметр круга
    
        Параметры:
        r (float): радиус
        
        Возвращаемое значение:
        perimeter (float): периметр круга
    '''
    return 2 * math.pi * r

