class Ex(Exception):
    def __init__(self, message):
        self.message = message


result = []
while True:
    number = input('Введите число или букву "Q" для завершения: ')

    if number == "Q" or number == "q":
        break

    try:
        if number.replace('.', '').replace(',' ,'').replace(' ' ,'').replace('/', '').isdigit():
            result.append(number)
        else:
            print(Ex('NOT A NUMBER!'))
            continue
    except Ex as error:
        Ex('WoW! NOT SOMETHING WENT WRONG! ')
    print(result)
