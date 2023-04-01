'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''
import random

try:
    size = int(input('Введите размерность массива: '))
    min_value = int(input('Введите минимальное значение диапазона: '))
    max_value = int(input('Введите максимальное значение диапазона: '))
    
    if size > 1 and min_value < max_value:
        array = [random.randint(-50, 50) for _ in range(size)]
        print(f'Массив: {array}')
        indices = [index for index, value in enumerate(array) if min_value <= value <= max_value]
        if indices:
            print(f'Индексы элементов входящих в диапазон от {min_value} до {max_value}: {indices}')
        else:
            print(f'В массиве нет элементов входящих в диапазон от {min_value} до {max_value}')
    else:
        print('Введено недопустимое значение')
except ValueError:
    print('Введено недопустимое значение')
