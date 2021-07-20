# >Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for el in self.matrix:
            for number in el:
                result += f"{number} \t"
            result += f"\n"

        return result

    def __add__(self, other):

        copy = self.matrix.copy()

        for num in range(len(self.matrix)):
            for other_num in range(len(other.matrix)):
                for number in range(len(self.matrix[num])):
                    for other_number in range(len(other.matrix[other_num])):
                        if number == other_number and num == other_num:
                            self.matrix[num][number] = other.matrix[other_num][other_number] + self.matrix[num][number]

        result = Matrix(self.matrix)
        self.matrix = copy
        return result


test = Matrix([[1, 3], [3, 4], [5, 6], [7, 8]])
test_2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
test_3 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(test + test_2 + test_3)
