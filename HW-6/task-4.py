# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов,
# передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость {self.speed} недопустима так как она выше допустимой для TownCar')
        else:
            print(f'Ваша скорость {self.speed} приемлема')


class SportCar(Car):
    def show_speed(self):
        print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Ваша скорость {self.speed} недопустима так как она выше допустимой для TownCar')
        else:
            print(f'Ваша скорость {self.speed} приемлема')


class PoliceCar(Car):
    pass


tesla = SportCar(120, 'blue', 'Tesla')
tesla.turn('right')
tesla.go()
tesla.stop()
tesla.show_speed()

opel = TownCar(70, 'blue', 'Tesla')
opel.show_speed()

kamaz = WorkCar(70, 'blue', 'Tesla')
kamaz.show_speed()

k = Car(20, 'blue', 'Tesla')
k.show_speed()
