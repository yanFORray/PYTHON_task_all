#Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. Нужно вывести наибольшее количество идущих подряд положительных чисел.
from random import randint

n = int(input("Введите количество дней периода: "))
count_temp = 0
count_max = 0
for i in range(n):
    tempr = randint(-50, 50)
    print(tempr)
    if tempr > 0:
        count_temp += 1
    elif count_temp != 0:         
        if count_max < count_temp:
            count_max = count_temp
        count_temp = 0
if count_max < count_temp:
    count_max = count_temp
print(count_max)