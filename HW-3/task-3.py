# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    print(round(arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3), 5))


arg_1 = float(input('Введите первый аргумент: '))
arg_2 = float(input('Введите второй аргумент: '))
arg_3 = float(input('Введите третий аргумент: '))

my_func(arg_1, arg_2, arg_3)
