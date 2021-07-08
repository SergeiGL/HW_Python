# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

cursor_position = 0
stuff_counter = 0
total_salaries = 0

with open('text_3.txt', 'r', encoding='utf-8') as f:
    f.seek(0)
    while True:
        if f.readline():
            stuff_counter += 1
            f.seek(cursor_position)
            line = f.readline().split()
            cursor_position = f.tell()
            total_salaries += float(line[1])
            if float(line[1]) < 20000.0:
                print(f'У сотрудника "{line[0]}" зароботная плата всего {line[1]} рублей!')
            else:
                continue
        else:
            print(f'Средняя зп сотрудников равна: {total_salaries / stuff_counter:02}')
            break
