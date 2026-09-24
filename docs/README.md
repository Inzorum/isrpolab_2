# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Available Python functions

The `main` branch contains two modules in the repository root:

- `circle.py`: `area(r)` returns the circle area; `perimeter(r)` returns
  the circumference. The argument `r` is the radius.
- `square.py`: `area(a)` returns the square area; `perimeter(a)` returns
  the square perimeter. The argument `a` is the side length.

The rectangle formulas above are reference formulas; this branch does not
contain a rectangle module.

## Usage example

Run Python 3 from the repository root so that both modules can be imported:

```python
import math
import circle
import square

assert math.isclose(circle.area(3), 9 * math.pi)
assert math.isclose(circle.perimeter(3), 6 * math.pi)
assert square.area(4) == 16
assert square.perimeter(4) == 16
```

Use non-negative lengths in the same unit. Areas are expressed in squared
units; perimeters use the original unit. The functions do not validate
negative inputs. Circle results use floating-point arithmetic, so compare
calculated values with a tolerance, for example `math.isclose`.
