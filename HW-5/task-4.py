# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.



Eng_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять',
}

with open('task_4_result.txt', "w", encoding='utf-8') as result_file:
    with open('text_4.txt', "r", encoding='utf-8') as f:
        f.seek(0)
        array = f.readlines()
        for el in array:
            words = el.split()
            for word in words:
                if Eng_numbers.get(word):
                    translation = Eng_numbers.get(word)
                    words[words.index(word)] = translation
                    for i in words:
                        result_file.write(i + " ")
                        if i == words[-1]:
                            result_file.write("\n")
