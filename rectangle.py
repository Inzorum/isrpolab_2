def area(a, b):
    ''' Принимает числа a и b и возвращает и возвращает площадь - произведение a и b'''

    if a < 0 or b < 0:
       return "Uncorrect input data: numbers should be more than 0"

    return a * b

def perimetr(a, b):
    '''Принимает числа a и b, возвращает удвоенную сумму a и b '''

    if a < 0 or b < 0:
        return "Uncorrect input data: numbers should be more than 0"

    return 2 * (a + b)
