name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
ice = bool(input('Вы любите мороженое? (Оставьте поле ПУСТЫМ если НЕТ и напишите что то если ДА) '))
print(type(ice), ice)
my_name = 'Sergei'
my_age = 19

while age < 1:
    print('Вы ошиблись')
    age = int(input('Введите Ваш возраст повторно: '))
else:
    print(f'Какое у Вас красивое имя, {name}, и прекрасный возраст {age} лет')
    if ice:
        print('А меня зовут {}, мне {} и я тоже люблю мороженое!'.format(my_name, my_age))
    else:
        print('А меня зовут {}, мне {} и я тоже ненавижу мороженое!'.format(my_name, my_age))
