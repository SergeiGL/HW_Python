#3.
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры классаов, вызвать методы экземпляров).


class Worker:
    name = 'Sergei'
    surname = 'Glukhov'
    position = 'CEO Apple'
    _income = {"wage": 1000000, "bonus": 3000}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя Сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        wage = self._income["wage"] + self._income['bonus']
        print(f'ЗП сотрудника с учётом бонуса: {wage}')


pos = Position()
pos.get_full_name()
pos.get_total_income()




