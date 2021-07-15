# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

digit = input('Введите число n: ')

doubledigit = digit + digit

trippledigit = doubledigit + digit

result = int(digit) + int(doubledigit) + int(trippledigit)

print(result)
