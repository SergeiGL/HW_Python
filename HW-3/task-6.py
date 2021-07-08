# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


#Раскомментите сточки ниже для того чтобы функция фильтровала цифры

"""def filter(string):
    while True:
        for word in string:
            for letter in word:
                if letter.isdigit():
                    string = input('Введите слова из маленьких латинских букв разделенных пробелом: ').split()
                    filter(string)
        return (string)"""


def int_func(string):

    """string = filter(string)"""

    result = ''

    copy = string[:]

    for word in string:
        for letter in word:
            if ord(letter) > 122 or ord(letter) < 65:
                copy.remove(word)
                break

    string = copy

    for i in range(len(string)):
        string[i] = string[i].capitalize()
        result = result + string[i] + ' '

    print(result)


string = input('Введите слова из маленьких латинских букв разделенных пробелом: ').split()

int_func(string)
