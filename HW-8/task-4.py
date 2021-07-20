class Ex(Exception):
    def __init__(self, message):
        self.message = message


class StorageOfficeEquipment:
    storage = []
    el_count = 0

    # @staticmethod
    #   def cdemp(bool):
    #      if bool == 0:
    #         StorageOfficeEquipment.el_count -= 1
    #    if bool == 1:
    #       StorageOfficeEquipment.el_count += 1
    #
    #       print(StorageOfficeEquipment.el_count)

    def remove(self, model):
        if not self.el_count == 0:
            for number in range(len(self.storage)):
                if self.storage[number][0] == model:
                    self.storage.remove(self.storage[number])
                    self.el_count -= 1
                    break
        else:
            print(Ex('Removing object from empty storage!!! '))

        print(self.storage)

    def __str__(self):
        return f'In the storage: {self.storage}'

    def __call__(self, arg):
        if not self.el_count == 0:
            self.storage[len(self.storage) - 1][1] = arg
        else:
            print(Ex('Storage is empty, cannot change amount!!!'))

        print(self.storage)

    def add(self, thing_to_add):
        self.el_count += 1
        self.storage.append(thing_to_add)
        print(self.storage)


class OfficeEquipment:
    def __init__(self, model, amount, condition='new', rating=5):
        while True:
            try:
                self.amount = int(amount)
            except ValueError:
                print(Ex('Amount is not a digit !!!'))
                amount = input('Enter valid amount: ')
                continue
            try:
                self.rating = (int(rating * 100000)) / 100000
                break
            except ValueError:
                print(Ex('Rating is not a digit !!!'))
                rating = input('Enter valid rating: ')
                continue

        self.model = model
        self.condition = condition

    def go_to_stock(self, stock_name, number_of_equip):
        while True:
            try:
                number_of_equip = int(number_of_equip)
            except ValueError:
                print(Ex(f"Number of {self.model} to go to stock is not a number "))
                number_of_equip = input('Enter valid number to go: ')
                continue

            if self.amount - number_of_equip < 0:
                print(Ex(f"Number of {self.model} to go to stock is more than we have in stock"))
                number_of_equip = input('Enter valid number to go: ')
                continue
            else:
                break

        self.amount = self.amount - number_of_equip
        self.good_info = [self.model, number_of_equip, {'condition': self.condition, 'rating': self.rating}]
        StorageOfficeEquipment.add(stock_name, self.good_info)


class Printer(OfficeEquipment):
    def __init__(self, model, amount, speed, condition='new', rating=5):
        while True:
            try:
                self.amount = int(amount)
            except ValueError:
                print(Ex('Amount is not a digit !!!'))
                amount = input('Enter valid amount: ')
                continue
            try:
                self.rating = (int(rating * 100000)) / 100000

            except ValueError:
                print(Ex('Rating is not a digit !!!'))
                rating = input('Enter valid rating: ')
                continue
            try:
                self.speed = int(speed)
                break
            except ValueError:
                print(Ex('Speed is not a digit !!!'))
                speed = input('Enter valid speed: ')
                continue

        self.model = model
        self.condition = condition


class Scanner(OfficeEquipment):
    def __init__(self, model, amount, speed, insurance, condition='new', rating=5):
        while True:
            try:
                self.amount = int(amount)
            except ValueError:
                print(Ex('Amount is not a digit !!!'))
                amount = input('Enter valid amount: ')
                continue
            try:
                self.rating = (int(rating * 100000)) / 100000

            except ValueError:
                print(Ex('Rating is not a digit !!!'))
                rating = input('Enter valid rating: ')
                continue
            try:
                self.speed = int(speed)
                break
            except ValueError:
                print(Ex('Speed is not a digit !!!'))
                speed = input('Enter valid speed: ')
                continue

        self.model = model
        self.condition = condition
        self.insurance = insurance


class Xerox(OfficeEquipment):
    pass


storage_1 = StorageOfficeEquipment()
print(storage_1)
printer_1 = Printer('Canon', 12, 12.1)
printer_2 = Printer('Xerox', 'sd', 100)
scanner = Scanner('Scan', 500, 'sdsdf', 'Yes')
scanner.go_to_stock(storage_1, 'dsfsd')
scanner.go_to_stock(storage_1, 500000)
printer_1.go_to_stock(storage_1, 5)

storage_1(20)  ##call заменяет количество у последнего предмета (допустим, что это количество берется из воздуха))
storage_1.remove("Canon")  ##выбрасывает первый с начала предмет данного названия со склада


##понятно, что если захотеть, в данной программе можно найти баги, но я уже устал их отлавливать
