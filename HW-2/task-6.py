# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента —
# номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

goods_list = []
i = 1

while True:
    title = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    units = input('Введите единицы измерение товара: ')

    dict = {
        'Название': title,
        'Цена': price,
        'Количество': quantity,
        'Ед': units
    }
    goods_list.append((i, dict))
    i += 1

    decider = input('Вы хотите еще ввести товары "YES" / "NO": ')
    if decider == 'NO' or decider == 'No' or decider == 'no':
        break


for i in range(len(goods_list)):
    print(goods_list[i])


all_names = []
all_prices = []
all_quantity = []
all_units = []

for i in range(len(goods_list)):
    all_names.append(goods_list[i][1].get('Название'))
    all_prices.append(goods_list[i][1].get('Цена'))
    all_quantity.append(goods_list[i][1].get('Количество'))
    all_units.append(goods_list[i][1].get('Ед'))

final_dict = {
    'Названия': all_names,
    'Цены': all_prices,
    'Количества': all_quantity,
    'Единицы': all_units
}
print(final_dict)
