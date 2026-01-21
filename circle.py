import math


def area(r):
    ''' Принимается число r, возвращает pi*r^2(площадь круга) '''

    if type(r) == str:
        return "Uncorrect input data: radius should be a possitive number, not a string" 

    return math.pi * r ** 2 


def perimetr(r):
    ''' Принимается число r,  возвращает 2*pi*r(периметр круга)'''
    return 2 * math.pi * r 

