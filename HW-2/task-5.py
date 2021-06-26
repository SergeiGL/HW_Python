# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [1]

while True:
    new_element = int(input('Введите натуральное число чтобы добавить число в Рейтинг или "0", чтобы закончить: '))

    if new_element == 0:
        break
    elif new_element < 0:
        print('Вы ввели не натуральное число')
        continue

    for i in range(len(my_list)):
        if new_element > my_list[i]:
            my_list.insert(i, new_element)
            break
        elif i == len(my_list) - 1:
            my_list.append(new_element)
        elif new_element <= my_list[i] and new_element > my_list[i + 1]:
            my_list.insert(i + 1, new_element)
            break

    print(my_list)
