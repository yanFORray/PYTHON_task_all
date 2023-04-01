# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

lst = input("Введите список чисел через пробел: ").split()
lst = [int(num) for num in lst] # преобразуем каждый элемент списка из строкового в целочисленный тип

k = int(input("Введите количество элементов для сдвига вправо: "))

n = len(lst)
k = k % n # если k > n, то сдвиг на k элементов эквивалентен сдвигу на k % n элементов

lst = lst[-k:] + lst[:-k]

print("Сдвинутый список:", lst)