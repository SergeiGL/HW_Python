# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
from functools import reduce

with open('my_text_5', 'w', encoding='utf-8') as f:
    for i in range(randint(0, 30)):
        f.write(str(randint(-100, 100)) + ' ')

def summa(a, b):
    return a + b

with open('my_text_5', 'r', encoding='utf-8') as f:
    numbers = f.read().split()
    for number in range(len(numbers)):
        numbers[number] = float(numbers[number])
    print(reduce(summa, numbers))
