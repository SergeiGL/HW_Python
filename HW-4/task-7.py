# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.


def fact(stop):
    for el in range(1, stop + 1):
        result = 1
        for number in range(1, el + 1):
            result *= number
        yield result


stop_number = int(input('Введите число: '))

for number, el in enumerate(fact(stop_number), 1):
    print(f'Факториал числа {number} = {el}')
