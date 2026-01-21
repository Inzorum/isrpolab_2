# Math formulas library
A library for calculating areas and perimeters for simple figures: circle, rectangle, triangle and square.

---

# Figures
## [Circle](../circle.py)
### Functions
  - `area(r)` - Returns area of the circle with given radius.
  Example:
  ```python
     print(area(54)) # Output: 9160.884177867836
  ```

  - `perimeter(r)` - Returns perimeter of the circle with given radius.
  Example:
  ```python
     print(perimeter(54)) # Output: 339.29200658769764
  ```

---

## [Rectangle](../rectangle.py)
### Functions
  - `area(a, b)` - Returns area of the rectangle with given sides.
  Example:
  ```python
     print(area(3, 8)) # Output: 24
  ```

  - `perimeter(a, b)` - Returns perimeter of the rectangle with given sides.
  Example:
  ```python
     print(perimeter(3, 8)) # Output: 22
  ```

---

## [Triangle](../triangle.py)
### Functions
  - `area(a, h)` - Returns area of the triangle with given base and height of triangle.
  Example:
  ```python
     print(area(4, 8)) # Output: 16.0
  ```

  - `perimeter(a, b, c)` - Returns perimeter of the triangle with given sides of triangle.
  Example:
  ```python
     print(perimeter(4, 8, 12)) # Output: 24
  ```

---

## [Square](../square.py)
### Functions
  - `area(a)` - Returns area of the square with given side.
  Example:
  ```python
     print(area(4)) # Output: 16
  ```

  - `perimeter(a)` - Returns perimeter of the square with given side.
  Example:
  ```python
     print(perimeter(4)) # Output: 16
  ```

---

# Commits history:

- commit 2196826374e846a2b998d80ec9418723fa778b30 (HEAD -> new_features_505052, origin/new_features_505052)\
Author: Tarklez <tarklez.dev@gmail.com>\
Date:   Wed Oct 15 22:12:02 2025 +0300\

    Rectangle perimeter calculation fixed

- commit 0739c1adc1d29c94d22b033cc1a466477ee1d5ba\
Author: Tarklez <tarklez.dev@gmail.com>\
Date:   Wed Oct 15 22:10:53 2025 +0300\

    Triangle added

- commit a94935022c7d8a728ddd897c349f271a5d5d38f3\
Author: Tarklez <tarklez.dev@gmail.com>\
Date:   Wed Oct 15 22:09:58 2025 +0300\

    Rectangle added

- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)\
Author: smartiqa <info@smartiqa.ru>\
Date:   Thu Mar 4 14:55:29 2021 +0300\

    L-03: Docs added

- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460\
Author: smartiqa <info@smartiqa.ru>\
Date:   Thu Mar 4 14:54:08 2021 +0300\

    L-03: Circle and square added
