class Rational:
    def __init__(self, numer, denom):
        # Constructor method that initializes a new Rational object
        # with numerator numer and denominator denom.
        # It calls the get_gcd method to reduce the fraction to its simplest form.
        self.numer, self.denom = self.get_gcd(numer, denom)
    
    def get_gcd(self, numer, denom):
        # Method that calculates the greatest common divisor (GCD) of two numbers
        # using the Euclidean algorithm.
        a = numer
        b = denom
        while b:
            a, b = b, a % b
        # Returns a tuple of two integers representing the reduced fraction.
        return (int(numer/a), int(denom/a))

    def __eq__(self, other):
        # Method that checks whether two Rational objects are equal by comparing
        # their numerators and denominators.
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        # Method that returns a string representation of the Rational object
        # in the form of a fraction.
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        # Method that adds two Rational objects and returns the result as a new Rational object.
        numer_add = ((self.numer * other.denom) + (self.denom * other.numer))
        denom_add = (self.denom * other.denom)
        return Rational(numer_add, denom_add)

    def __sub__(self, other):
        # Method that subtracts two Rational objects and returns the result as a new Rational object.
        numer_sub = ((self.numer * other.denom) - (self.denom * other.numer))
        denom_sub = (self.denom * other.denom)
        return Rational(numer_sub, denom_sub)

    def __mul__(self, other):
        # Method that multiplies two Rational objects and returns the result as a new Rational object.
        numer_mul = self.numer * other.numer
        denom_mul = self.denom * other.denom
        return Rational(numer_mul, denom_mul)

    def __truediv__(self, other):
        # Method that divides two Rational objects and returns the result as a new Rational object.
        numer_div = self.numer * other.denom
        denom_div = other.numer * self.denom
        return Rational(numer_div, denom_div)

    def __abs__(self):
        # Method that returns the absolute value of a Rational object as a new Rational object.
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        # Method that raises a Rational object to a given power and returns the result as a new Rational object.
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))

    def __rpow__(self, base):
        # Method that raises a given base to a Rational object and returns the result as a float value.
        return (base ** self.numer) ** (1 / self.denom)
