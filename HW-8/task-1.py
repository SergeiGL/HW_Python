# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, dirty_string):
        self.dirty_string = dirty_string
        self.clear_string = self.puring(self.dirty_string)
        self.validation(self.clear_string)

    @classmethod
    def puring(cls, dirty_string):
        while True:
            dirty_string = dirty_string.split('-')
            for number in range(len(dirty_string)):
                try:
                    dirty_string[number] = int(dirty_string[number])
                    if number == len(dirty_string)-1:
                        return dirty_string
                except ValueError as err:
                    print(err)
                    print('Вы ввели не целое число в качестве даты')
                    dirty_string = str(input('Enter data again: '))
                    break

    @staticmethod
    def validation(clear_string):
        if clear_string[0] < 1 or clear_string[0] > 31:
            print(f'Date <<{clear_string[0]}>> is out of borders 0-31') #тут у меня случился приступ лени делать бесконечный цикл (как в классе выше) и добиваться правильной даты
            return

        if clear_string[1] < 1 or clear_string[0] > 12:
            print(f'Month number <<{clear_string[1]}>> is out of borders 0-12')
            return


test = Data('11a-11-2001')
