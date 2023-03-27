'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
Пример:
2 2
4'''
def get_sum_numbers(a,b):
    if a > 0:
        a -= 1
        return get_sum_numbers(a,b) + 1
    elif b > 0:
        b -= 1
        return get_sum_numbers(a,b) + 1
    else:
        return 0

try:
    number_first, number_second = int(input('Введите число: ')), int(input('Введите число: '))
    if number_first >= 0 and number_second >= 0:
        print(f'Решение: {number_first} + {number_second} = {get_sum_numbers(number_first, number_second)}')
    else:
        print('Введено недопустимое значение')
except:
    print('Введено недопустимое значение')