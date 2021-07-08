# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

dict = {}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for number in range(len(lines)):
        lines[number] = lines[number].split()
    for number in range(len(lines)):
        total_hours = 0
        last_subject = 0
        for position in range(len(lines[number])):
            if position == 0:
                last_subject = position
                dict[lines[number][position]] = 0
                continue
            elif lines[number][position] == '-':
                continue
            else:
                _ = lines[number][position].split("(")
                total_hours += int(_[0])
                dict[lines[number][last_subject]] = total_hours

    print(dict)
