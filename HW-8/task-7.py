class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real) - (self.img * other.img), (self.real * other.img) + (other.real * self.img))

    def __str__(self):
        return f'Real part: {self.real} \nImaginary part: {self.img} \n'


num_1 = ComplexNumber(1, 2)
num_2 = ComplexNumber(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
