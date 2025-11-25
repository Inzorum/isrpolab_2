# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Документация проекта Geometry Calculator

## Общее описание решения

Проект Geometry Calculator представляет собой набор функций для вычисления геометрических параметров различных фигур. Решение реализовано на Python и включает модули для работы с квадратами, прямоугольниками, треугольниками и кругами. Каждая функция сопровождается подробной документацией с описанием параметров, возвращаемых значений и примерами использования.

## Описание функций

### Модуль: square.py

#### Функция area(a)

Вычисляет площадь квадрата.

**Параметры:**
- `a` (float) - длина стороны квадрата

**Возвращаемое значение:**
- float - площадь квадрата

**Пример вызова:**
```python
>>> area(5)
25.0
>>> area(2.5)
6.25
```


#### Функция perimeter(a)

Вычисляет периметр квадрата.

**Параметры:**

- `a` (float) - длина стороны квадрата
    

**Возвращаемое значение:**

- float - периметр квадрата
    

**Пример вызова:**

python
```python
>>> perimeter(5)
20.0
>>> perimeter(2.5)
10.0
```

### Модуль: rectangle.py

#### Функция area(a, b)

Вычисляет площадь прямоугольника.

**Параметры:**

- `a` (float) - длина первой стороны
    
- `b` (float) - длина второй стороны
    

**Возвращаемое значение:**

- float - площадь прямоугольника
    

**Пример вызова:**

```python
>>> area(5, 3)
15.0
>>> area(2.5, 4)
10.0
```

#### Функция perimeter(a, b)

Вычисляет периметр прямоугольника.

**Параметры:**

- `a` (float) - длина первой стороны
    
- `b` (float) - длина второй стороны
    

**Возвращаемое значение:**

- float - периметр прямоугольника
    

**Пример вызова:**

```python
>>> perimeter(5, 3)
16.0
>>> perimeter(2.5, 4)
13.0
```


### Модуль: triangle.py

#### Функция area(a, h)

Вычисляет площадь треугольника через основание и высоту.

**Параметры:**

- `a` (float) - длина основания треугольника
    
- `h` (float) - высота треугольника, проведенная к основанию
    

**Возвращаемое значение:**

- float - площадь треугольника
    

**Пример вызова:**

```python
>>> area(10, 5)
25.0
>>> area(6, 4)
12.0
```

#### Функция perimeter(a, b, c)

Вычисляет периметр треугольника.

**Параметры:**

- `a` (float) - длина первой стороны
    
- `b` (float) - длина второй стороны
    
- `c` (float) - длина третьей стороны
    

**Возвращаемое значение:**

- float - периметр треугольника
    

**Пример вызова:**

```python
>>> perimeter(3, 4, 5)
12.0
>>> perimeter(5, 5, 5)
15.0
```

### Модуль: circle.py

#### Функция area(r)

Вычисляет площадь круга.

**Параметры:**

- `r` (float) - радиус круга
    

**Возвращаемое значение:**

- float - площадь круга
    

**Пример вызова:**

```python
>>> area(5)
78.53981633974483
>>> area(2.5)
19.634954084936208
```

#### Функция perimeter(r)

Вычисляет длину окружности (периметр круга).

**Параметры:**

- `r` (float) - радиус круга
    

**Возвращаемое значение:**

- float - длина окружности
    

**Пример вызова:**

```python
>>> perimeter(5)
31.41592653589793
>>> perimeter(2.5)
15.707963267948966
```


## История изменения проекта

### 38af648 feat: new file rectangle.py

commit 38af6488a5f1a6436a03bde46dcfde6d9b5b6f06
Author: YutaJ17 <krusakovski@yandex.ru>
Date:   Mon Oct 27 17:40:32 2025 +0300

    feat: new file rectangle.py

diff --git a/rectangle.py b/rectangle.py
new file mode 100644
index 0000000..beed4b8
--- /dev/null
+++ b/rectangle.py
@@ -0,0 +1,5 @@
+def area(a, b): 
+    return a * b 
+
+def perimeter(a, b): 
+    return a + b 
### a880e01 fix: function perimeter in rectangle.py

commit 38af6488a5f1a6436a03bde46dcfde6d9b5b6f06
Author: YutaJ17 <krusakovski@yandex.ru>
Date:   Mon Oct 27 17:40:32 2025 +0300

    feat: new file rectangle.py

diff --git a/rectangle.py b/rectangle.py
new file mode 100644
index 0000000..beed4b8
--- /dev/null
+++ b/rectangle.py
@@ -0,0 +1,5 @@
+def area(a, b): 
+    return a * b 
+
+def perimeter(a, b): 
+    return a + b 
### 5856db4 feat: new file triangle.py

commit 5856db48c77911b9458faa2d4c9f13ca3027d4e6
Author: YutaJ17 <krusakovski@yandex.ru>
Date:   Mon Oct 27 17:46:23 2025 +0300

    feat: new file triangle.py

diff --git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..49864a2
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,5 @@
+def area(a, h): 
+    return a * h / 2 
+
+def perimeter(a, b, c): 
+    return a + b + c 