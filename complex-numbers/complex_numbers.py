import math


class ComplexNumber:
    # initiates the class with the real and imaginary values
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # test for equivalent if real and imaginary values
    # are equal in both objects
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    # dunder method add. If the other object is an int,
    # creates a new ComplexNumber object
    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        real = (a + c)
        imaginary = (b + d)
        return ComplexNumber(real, imaginary)

    # allows to add an int and a ComplexNumber object
    def __radd__(self, other):
        return self.__add__(other)

    # multiplies both complex numbers. If the other object
    # is an int, creates a new ComplexNumber object
    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        real = (a * c - b * d)
        imaginary = (b * c + a * d)
        return ComplexNumber(real, imaginary)

    # allows to multiply an int and a ComplexNumber object
    def __rmul__(self, other):
        return self.__mul__(other)

    # substract the other ComplexNumber from the self ComplexNumber.
    # If the other number is an int, creates a new ComplexNumber
    def __sub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        real = (a - c)
        imaginary = (b - d)
        return ComplexNumber(real, imaginary)

    # allows to substract a ComplexNumber from an int by
    # converting first the int into a ComplexNumber
    def __rsub__(self, other):
        return ComplexNumber(other, 0) - self

    # divides a ComplexNumber by another ComplexNumber.
    # If the other number is an int, creates a new ComplexNumber
    def __truediv__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other, 0)
        a = self.real
        b = self.imaginary
        c = other.real
        d = other.imaginary
        real = (a * c + b * d)/(c**2 + d**2)
        imaginary = (b * c - a * d)/(c**2 + d**2)
        return ComplexNumber(real, imaginary)

    # allows to divide an int by a ComplexNumber by
    # converting first the int into a ComplexNumber
    def __rtruediv__(self, other):
        return ComplexNumber(other, 0) / self

    # returns the absolute value of a ComplexNumber
    def __abs__(self):
        a = self.real
        b = self.imaginary
        abs_value = math.sqrt((a**2) + (b**2))
        return abs_value

    # returns the conjugate of a ComplexNumber
    def conjugate(self):
        return ComplexNumber(self. real, -1 * self.imaginary)

    # returns the exponential of a ComplexNumber
    def exp(self):
        real = math.exp(self.real) * (math.cos(self.imaginary))
        imaginary = math.exp(self.real) * (math.sin(self.imaginary))
        return ComplexNumber(real, imaginary)
