# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [list[i] for i in range(len(list)) if list[i] > list[i - 1] and i != 0]
print(new_list)
