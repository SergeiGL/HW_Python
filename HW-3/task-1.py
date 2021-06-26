# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(arg_1, arg_2):
    while True:
        try:
            return print(round(arg_1 / arg_2, 2))
        except ZeroDivisionError:

            print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!')
            arg_1 = float(input('Введите делимое: '))
            arg_2 = float(input('Введите делитель: '))
            continue


arg_1 = float(input('Введите делимое: '))
arg_2 = float(input('Введите делитель: '))

divide(arg_1, arg_2)
