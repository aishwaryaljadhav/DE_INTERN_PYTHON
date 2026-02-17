class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, num2):
        newReal=self.real + num2.real
        newImag=self.imag + num2.imag
        return Complex(newReal, newImag)
    def __sub__(self, num2):
        newReal=self.real - num2.real
        newImag=self.imag - num2.imag
        return Complex(newReal, newImag)

num1=Complex(2, 3)
num2=Complex(4, 5)
print(num1)
print(num2)
num3=num1+num2
print(num3)
num4=num1-num2
print(num4)
