# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class Ex(Exception):
    def __init__(self, message):
        self.message = message


result1 = lambda x, y: x / y if y > 0 else Ex('Zero division Error')

print(result1(int(input('Enter devidend: ')), int(input('Enter devider: '))))
