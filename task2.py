#Найдите сумму цифр числа
num = int(input("Введите число: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10 #находим последнюю цифру числа
    sum_of_digits += digit
    num //= 10
print("Сумма цифр введенного числа:", sum_of_digits)
