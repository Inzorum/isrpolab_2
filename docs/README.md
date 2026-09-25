# Math formulas

Библиотека `geometric_lib` содержит функции для вычисления площади и периметра
простых геометрических фигур.

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ½·a·h

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions
| Файл        | Функция        | Описание                               |
|-------------|----------------|----------------------------------------|
| `circle.py` | `area(r)`      | площадь круга радиуса `r`              |
| `circle.py` | `perimeter(r)` | длина окружности радиуса `r`           |
| `square.py` | `area(a)`      | площадь квадрата со стороной `a`       |
| `square.py` | `perimeter(a)` | периметр квадрата со стороной `a`      |

## Usage
```python
import circle, square

print(circle.area(2))       # 12.566...
print(square.perimeter(3))  # 12
```
