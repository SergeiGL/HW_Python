class Stationery:
    title = 'Stery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Ручки')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Карандаша')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Маркера')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

smth = Stationery()
smth.draw()
