while True:

    ticket = input("Введите номер билета: ")

# Проверяем, является ли номер билета шестизначным
    if len(ticket) != 6:
        print("Неверный формат номера билета!")
    else:
        int_ticket = [int(d) for d in ticket]
    # Суммируем первые три цифры и последние три цифры
    sum1 = sum(int_ticket[:3])
    sum2 = sum(int_ticket[3:])
    # Проверяем, равны ли суммы
    if sum1 == sum2:
        print("Счастливый билет!")
    else:
        print("Обычный билет.")
    answer = input("Хотите продолжить? (да/нет): ")
    if answer.lower() != "да":
        break 