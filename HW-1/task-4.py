# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number = int(input('Введите число: '))

maxdigit = 0

while number != 0:
    digit = number % 10
    if maxdigit < digit:
        maxdigit = digit
    number = number // 10

print(maxdigit)
