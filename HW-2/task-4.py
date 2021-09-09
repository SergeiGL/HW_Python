# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_imp = input('Введите строку из нескольких слов через пробел: ')
separated_imp = user_imp.split(' ')
for i in range(len(separated_imp)):
    separated_imp[i] = separated_imp[i][:10]

for num, el in enumerate(separated_imp, 1):
    print(num, el)
