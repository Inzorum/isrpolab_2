# Geometric_lib

## Описание

### geometric_lib - библиотека, позволяющая определить плошадь и периметр квадрата и круга в проектах на Python

---

## Как работать с библиотекой

### При помощи команды git clone клонируйте библиотеку в свой проект

```bash
cd yourproject/path
git clobe https://github.com/bxrzxr/geometric_lib.git
```

### В python файле импортируйте библиотеку

```py
import geometric_lib.circle as circle
import geometric_lib.square as square

print(circle.perimetr(5)) # output: 31.41592653589793
print(square.area(5)) # output: 25
```

### Функции в библиотеке и примеры их вызова

```py
circle.area(r) # Площадь круга с радиусом r
pie_area = circle.area(3) # 28.274333882308138

circle.perimetr(r) # Периметр круга с радиусом r
pie_perimetr = circle.perimetr(3) # 18.84955592153876

square.area(a) # Площадь квадрата со стороной a
room_area = square.area(4) # 16

square.perimetr(a) # Периметр квадрата со стороной a
room_perimetr = square.perimetr(4) # 16
```
---
## Тестирование

### В библиотеке есть папка ```tests```, в которой лежит набор юнит-тестов для проверки работоспособности функций

### Для запуска тестов введите в консоль:
```
python3 -m unittest tests.Geometric_lib_test
```

### Описание тестов:
- Проверяют корректность вычисления площади квадрата и круга
- Проверяют корректность вычисления периметра квадрата и круга
- Проверяют различные входные данные(целые,дробные,0,большие целые и дробные значения)

---
### История изменений

```
commit b592c336ce33863e95918104647ff581d0cec7d1 (HEAD -> Tests)
Author: bxrzxr <ahmedalievruslan6@gmail.com>
Date:   Tue Nov 18 17:06:16 2025 +0300

    tests added


commit 08a0725de23855716ca45665b544677f56e60f40 (HEAD -> task_1)
Author: bxrzxr <ahmedalievruslan6@gmail.com>
Date:   Fri Sep 26 15:41:09 2025 +0300

    Добавлена документация

commit 97625b1cc6822731198003271ec202fc4c1f3d1d
Author: bxrzxr <ahmedalievruslan6@gmail.com>
Date:   Fri Sep 26 15:20:17 2025 +0300

    Добавлен блок комментариев, в котором описывается функция и пример её вызова
```
