# Geometric Lib
## Общее описание библиотеки

- Четыре файла с функциями для подсчета площади или периметра геометрических фигур.

    1. `circle.py`
        - Содержит функции для вычисления площади и периметра ***окружности***
    2. `rectangle.py`
        - Содержит функции для вычисления площади и периметра ***прямоугольника***
    3. `square.py`
        - Содержит функции для вычисления площади и периметра ***квадрата***
    4. `triangle.py`
        - Содержит функции для вычисления площади и периметра ***треугольника***
## Функции библиотеки

- Примеры использования функций библиотеки

    1. `cicle.py`
        
        1.1 `def area(r)`
        
        ```python
        def area(r):
            return math.pi * r * r
        
        area(3) #return: 28.274333882308138
        ```

        2.1 `def perimetr(r)`

        ```python
        def perimeter(r):
        return 2 * math.pi * r

        perimetr(3) #return: 18.84955592153876
        ```

    2. `rectangle.py`

        2.1 `def area(a, b)`

        ```python
        def area(a, b): 
            return a * b
        
        area(3, 2) #return: 6
        ```

        2.2 `def perimetr(a, b)`

        ```python
        def perimeter(a, b):
            return (a + b) * 2

        perimeter(2, 3) #return: 10
        ```

    3. `square.py`

        3.1 `def area(a)`

        ```python
        def area(a):
            return a*a

        area(2) #return: 4
        ```

        3.2 `def perimetr(a)`

        ```python
        def perimeter(a):
            return 4 * a
        
        perimeter(3) #return: 12
        ```

    4. `triangle.py`

        4.1 `def area(a, h)`

        ```python
        def area(a, h):
            return a * h / 2

        area(2, 3) #return: 3
        ```

        4.2 `def perimetr(a, b, c)`

        ```python
        def perimeter(a, b, c):
            return a + b + c
        
        perimeter(1, 2, 3) #return: 6
        ```
## История изменения репозитория

- `commit 22448c264be27183035de12ed165e30817ee8a71`
    - исправлена ошибка с подсчетом периметра прямоугольника

- `commit 75d36a660f6ab1005fddcb3aedc1ece1efd6847b`
    - добавлен файл rectangle.py для подсчеты площади и периметра треугольника

- `commit d078c8d9ee6155f3cb0e577d28d337b791de28e2` 
    - добвлена директория docs 
    
- `commit 8ba9aeb3cea847b63a91ac378a2a6db758682460`
    - добавлены файлы circle.py и square.py

    