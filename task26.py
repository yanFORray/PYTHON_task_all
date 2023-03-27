'''Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую 
степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
def get_number_degree(a,b):
    if b > 0:
        return a * get_number_degree(a, b - 1)
    elif b < 0:
        return get_number_degree(a, b + 1) / a
    else:
        return 1.0

try:
    number, degree = float(input('Введите число : ')), int(input('Введите степень: '))
    print(f'Решение: {number} ^ {degree} = {round(get_number_degree(number, degree),2)}')
except:
    print('Введено недопустимое значение')