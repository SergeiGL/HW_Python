# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle


def list_generator(start):
    for el in count(start):
        if el > start + 10:
            break
        else:
            yield el


start = int(input('Введите начальное число: '))
g = list_generator(start)
for el in g:
    print(el)


def rounded_circle(list):
    counter = 0
    for el in cycle(list):
        if counter > len(list) * 5:
            break
        else:
            yield el
            counter += 1


c = rounded_circle([1, 2, 3, 4])

for el in c:
    print(el)
