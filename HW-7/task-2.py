# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Cloths:
    def __init__(self, V_H):
        self.V_H = V_H

    costs = 0

    @property
    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        Cloths.costs = Cloths.costs + self.calculate + other.calculate
        return Jacket(-1)

    def __str__(self):
        return f'{Cloths.costs:02f}'


class Jacket(Cloths):
    @property
    def calculate(self):
        if self.V_H == -1:
            return 0
        else:
            return self.V_H / 6.5 + 0.5


class Costume(Cloths):
    @property
    def calculate(self):
        return (2 * self.V_H + 0.3) / 100


jacket = Jacket(9)
costume = Costume(180)
print(jacket + costume)
