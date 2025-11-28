# Geometric_lib

## General description

Library includes _4 programs_ files with _2 functions_ for each geometric figure: `area` and `perimetr`

The functions <ins>take several parameters</ins> and in the next line return the calculated value in the form of **return <formula>**

Full descriptions of all functions are <ins>in the code files</ins>

### Links

- Circle.py https://github.com/ViLLXM/geometric_lib/blob/lab2/circle.py
```
import math


def area(r):
    '''
    Принимает число r, возвращает площадь круга радиуса r
    Например, для числа 3 будет возвращено число 28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает площадь круга радиуса r
    Например, для числа 3 будет возвращено число 18.84955592153876
    '''
    return 2 * math.pi * r
```

- Rectangle.py https://github.com/ViLLXM/geometric_lib/blob/lab2/rectangle.py
```
def area(a, b):
    '''
    Принимает числа a, b возвращает площадь прямоугольника со сторонами a, b
    Например, для чисел 4 и 5 будет возвращено число 20
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает числа a, b, возвращает периметр прямоугольника со сторонами a, b
    Например, для чисел 4 и 5 будет возвращено число 18
    '''
    return (a + b) * 2
```

- Sqare.py https://github.com/ViLLXM/geometric_lib/blob/lab2/square.py
```
def area(a):
    '''
    Принимает число a, возвращает площадь квадрата со стороной a
    Например, для числа 5 будет возвращено число 25
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число a, возвращает периметр квадрата со стороной a
    Например, для числа 5 будет возвращено число 20
    '''
    return 4 * a
```

- Triangle.py https://github.com/ViLLXM/geometric_lib/blob/lab2/triangle.py
```
def area(a, h):
    '''
    Принимает числа a, h возвращает площадь треугольника со стороной a и высотой h
    Например, для чисел 5, 6 будет возвращено число 15
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает числа a, b, c возвращает периметр треугольника со сторонами a, b, c
    Например, для чисел 5, 6, 7 будет возвращено число 18
    '''
    return a + b + c 
```

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = 1/2ah

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a + b)
- Square: P = 4a
- Triangle: P = a + b + c

## History of commits

* Commit 13b00e1bba2efeee0d02d09bd9861960f7bc7124
    Date:   Thu Sep 18 09:36:38 2025 +0300
    `Added comments to functions`

* Commit 6183a34dc69a32047bd80d573f07d8cd51286a87
    Date:   Thu Sep 18 09:08:59 2025 +0300
    `Rectangle.py and and triangle.py was added`

* Commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
    Date:   Thu Mar 4 14:55:29 2021 +0300
    `Docs added`

## Tests
Last tests found a mistake in situations with zero inputs

*rectangle.py*
input: 0 5
Expected: 0
Actual: 10

*triangle.py*
input: 0 2 0
Expected: 0
Actual: 2
