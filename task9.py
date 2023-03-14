n = int(input("Введите число для вычисления факториала: "))

i = 1
result = 1

# Выполняем цикл, пока i <= n
while i <= n:
    result *= i
    i += 1

# Выводим результат
print(f"{n}! = {result}")