# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def all_string(name, surname, birth_date, town, email, tel):
    print(f'Ваше имя: {name}, Ваша фамилия: {surname}, Ваш год рождения: {birth_date}, '
          f'Ваш город проживания: {town}, Ваш email: {email}, Ваш телефон: {tel}')


name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
birth_date = input('Введите Ваш год рождения: ')
town = input('Введите Ваш город: ')
email = input('Введите Ваш email: ')
tel = input('Введите Ваш телефон: ')

all_string(tel=tel, name=name, town=town, birth_date=birth_date, email=email, surname=surname)
