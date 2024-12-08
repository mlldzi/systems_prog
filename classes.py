import math


class Fraction:
    def __init__(self, num, denom=1):
        if denom == 0:
            raise ValueError("denominator cannot be zero")

        if isinstance(num, float):
            num, denom = self._float_to_fraction(num)
        if isinstance(denom, float):
            temp_num, temp_denom = self._float_to_fraction(denom)
            num, denom = temp_denom, temp_num

        if isinstance(num, Fraction) or isinstance(denom, Fraction):
            if isinstance(num, Fraction) and isinstance(denom, Fraction):
                num = num.numerator * denom.denominator
                denom = num.denominator * denom.numerator

            elif isinstance(num, Fraction):
                num_numerator = num.numerator
                num_denominator = num.denominator
                num = num_numerator
                denom = num_denominator * denom

            else:
                num = num * denom.denominator
                denom = denom.numerator

        if not isinstance(num, int) or not isinstance(denom, int):
            raise TypeError("numerator and denominator must be integers")

        gcd_val = math.gcd(num, denom)
        self.numerator = num // gcd_val
        self.denominator = denom // gcd_val

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def _float_to_fraction(self, num, epsilon=1e-9,
                           max_iter=200):  # https://stackoverflow.com/questions/5124743/algorithm-for-simplifying-decimal-to-fractions/5124834#5124834
        d = [0, 1] + ([0] * max_iter)
        z = num
        n = 1
        t = 1
        if z.is_integer():
            return int(z), 1
        while num and t < max_iter and abs(n / d[t] - num) > epsilon:
            t += 1
            z = 1 / (z - int(z))
            d[t] = d[t - 1] * int(z) + d[t - 2]
            n = int(num * d[t] + 0.5)

        return n, d[t]

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        # if self.denominator == 1:
        #     return str(self.numerator)
        # return f"{self.numerator}/{self.denominator}"
        return f"{self.__class__.__name__}(numerator={self.numerator}, denominator={self.denominator})"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __pow__(self, n):
        if isinstance(n, int | float):
            return Fraction(self.numerator ** n, self.denominator ** n)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.numerator != other.numerator or self.denominator != other.denominator
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int | float):
            return self.numerator < other * self.denominator
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, int | float):
            return self.numerator <= other * self.denominator
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int | float):
            return self.numerator > other * self.denominator
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, int | float):
            return self.numerator >= other * self.denominator
        return NotImplemented

    def __round__(self, n=None):
        if n is None:
            return Fraction(round(self.numerator / self.denominator))
        else:
            factor = 10 ** n
            rounded_numerator = round(self.numerator * factor / self.denominator)
            return Fraction(rounded_numerator, factor)

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))


class Complex:
    def __init__(self, real: Fraction | int | float, imagine: Fraction | int | float = 0):
        self._real = Fraction(real)
        self._imagine = Fraction(imagine)

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imagine(self):
        return self._imagine

    @imagine.setter
    def imagine(self, value):
        self._imagine = value

    def __str__(self):
        if self.imagine.numerator == 0:
            return f'{self.real}'
        if self.imagine.numerator < 0:
            return f'{self.real} - {-self.imagine}i'
        return f'{self.real} + {self.imagine}i'

    def __repr__(self):
        return f'{self.__class__.__name__}(real={self.real}, imagine={self.imagine})'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.real + other.real, self.imagine + other.imagine)
        if isinstance(other, int | float | Fraction):
            return self.__class__(self.real + other, self.imagine)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.real - other.real, self.imagine - other.imagine)
        if isinstance(other, int | float | Fraction):
            return self.__class__(self.real - other, self.imagine)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            real = self.real * other.real - self.imagine * other.imagine
            imagine = self.real * other.imagine + self.imagine * other.real
            return self.__class__(real, imagine)
        if isinstance(other, int | float | Fraction):
            return self.__class__(self.real * other, self.imagine * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            denom = other.real ** 2 + other.imagine ** 2
            if denom == 0:
                raise ZeroDivisionError
            real = (self.real * other.real + self.imagine * other.imagine) / denom
            imagine = (self.imagine * other.real - self.real * other.imagine) / denom
            return self.__class__(real, imagine)
        if isinstance(other, int | float | Fraction):
            if other == 0:
                raise ZeroDivisionError
            return self.__class__(self.real / other, self.imagine / other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.real == other.real and self.imagine == other.imagine
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.real != other.real or self.imagine != other.imagine
        return NotImplemented

    def __abs__(self):
        return round((self.real ** 2 + self.imagine ** 2) ** 0.5, 4)

    def __pow__(self, n):
        if isinstance(n, int):
            r = math.sqrt(self.real ** 2 + self.imagine ** 2)
            theta = math.atan2(self.imagine, self.real)

            r_n = r ** n
            theta_n = theta * n

            real = round(r_n * math.cos(theta_n), 4)
            imagine = round(r_n * math.sin(theta_n), 4)
            if real.is_integer():
                real = int(real)
            if imagine.is_integer():
                imagine = int(imagine)

            return self.__class__(real, imagine)

        return TypeError("argument must be an integer")

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.real += other.real
            self.imagine += other.imagine
        elif isinstance(other, int | float | Fraction):
            self.real += other
        return self

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.real -= other.real
            self.imagine -= other.imagine
        elif isinstance(other, int | float | Fraction):
            self.real -= other
        return self

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            real = self.real * other.real - self.imagine * other.imagine
            imagine = self.real * other.imagine + self.imagine * other.real
            self.real = real
            self.imagine = imagine
        elif isinstance(other, int | float | Fraction):
            self.real *= other
            self.imagine *= other
        return self

    def __idiv__(self, other):
        if isinstance(other, self.__class__):
            denom = other.real ** 2 + other.imagine ** 2
            if denom == 0:
                raise ZeroDivisionError
            real = (self.real * other.real + self.imagine * other.imagine) / denom
            imagine = (self.imagine * other.real - self.real * other.imagine) / denom
            self.real = real
            self.imagine = imagine
        elif isinstance(other, int | float | Fraction):
            if other == 0:
                raise ZeroDivisionError
            self.real /= other
            self.imagine /= other
        return self

    def __neg__(self):
        return self.__class__(-self.real, -self.imagine)

    def arg(self):
        return math.atan2(float(self.imagine), float(self.real))
