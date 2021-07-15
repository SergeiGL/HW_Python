# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

strings_counter = 0
cursor_position = 0

with open('new.file.txt', encoding='utf-8') as f:
    f.seek(0)
    while True:
        if f.readline():
            f.seek(cursor_position)
            strings_counter += 1
            line = f.readline().split()
            cursor_position = f.tell()
            words = len(line)
            print(f'В строке номер {strings_counter} ровно {words} слов(а)')
        else:
            break
