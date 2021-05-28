class ComplexNumber():
    real: float
    imaginary: float

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other. imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


comp1 = ComplexNumber(5, 2)
comp2 = ComplexNumber(10, 3)

print(comp1 + comp2)
print(comp1 * comp2)
