'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12'''
from random import randint
try:
    first_range = int(input('Введите количество элементов первого множества: '))
    second_range = int(input('Введите количество элементов второго множества: '))
    first_multi = [randint(-10, 11) for _ in range(first_range)]
    second_multi = [randint(-10, 11) for _ in range(second_range)]
    print('Первое множество:', end=' ')
    print(*first_multi)
    print('Второе множество:', end=' ')
    print(*second_multi)
    intersection_multi = set(first_multi).intersection(set(second_multi))
    if intersection_multi != set():
        intersection_multi = tuple(sorted(intersection_multi))
        print('Одинаковый(-ые) элемент(-ы) в первом и во втором множествах:', end=' ')
        print(*intersection_multi)
    else:
        print('Одинаковых элементов в первом и во втором множествах нет')
except:
    print('Введено недопустимое значение')