# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = int(input("Введите число n:"))
number2 = int(str(number) + str(number))
number3 = int(str(number2) + str(number))

print(number + number2 + number3)