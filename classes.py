import math


class Fraction:
    def __init__(self, num, denom=1):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")

        if isinstance(num, Fraction) or isinstance(denom, Fraction):
            self._handle_fraction_input(num, denom)
        else:
            self._handle_float_input(num, denom)

        self._simplify()

    def _handle_fraction_input(self, num, denom):
        """num или denom — это объект Fraction"""
        if isinstance(num, Fraction) and isinstance(denom, Fraction):
            self.numerator = num.numerator * denom.denominator
            self.denominator = num.denominator * denom.numerator
        elif isinstance(num, Fraction):
            self.numerator = num.numerator
            self.denominator = num.denominator * denom
        elif isinstance(denom, Fraction):
            self.numerator = num * denom.denominator
            self.denominator = denom.numerator

    def _handle_float_input(self, num, denom):
        """num или denom — это вещественные числа"""
        num_num, num_denom = None, None
        den_num, den_denom = None, None

        if isinstance(num, float):
            num_num, num_denom = self._float_to_fraction(num)
        if isinstance(denom, float):
            den_num, den_denom = self._float_to_fraction(denom)

        # Обработка полученных чисел и знаменателей
        if num_num is not None and den_num is not None:
            self.numerator = num_num * den_denom
            self.denominator = den_num * num_denom
        elif num_num is not None:
            self.numerator = num_num
            self.denominator = num_denom * denom
        elif den_num is not None:
            self.numerator = den_denom * num
            self.denominator = den_num

        # Если переданы только целые числа
        elif isinstance(num, int) and isinstance(denom, int):
            self.numerator = num
            self.denominator = denom

    def _simplify(self):
        gcd_val = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd_val
        self.denominator //= gcd_val

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def _float_to_fraction(self, num):
        if num.is_integer():
            return int(num), 1

        sign = -1 if num < 0 else 1
        num = abs(num)
        decimal_places = len(str(num).split('.')[-1])
        denom = 10 ** decimal_places
        numerator = round(num * denom)

        gcd_val = math.gcd(numerator, denom)
        numerator //= gcd_val
        denom //= gcd_val

        return sign * numerator, denom

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
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
        if isinstance(self._real, Fraction):
            if self._real.denominator == 1:
                self._real = self._real.numerator

        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imagine(self):
        if isinstance(self._imagine, Fraction):
            if self._imagine.denominator == 1:
                self._imagine = self._imagine.numerator
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

        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self._real += other._real
            self._imagine += other._imagine
        elif isinstance(other, int | float | Fraction):
            self._real += Fraction(other)
            self._imagine += Fraction(other)
        else:
            return NotImplemented
        return self

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self._real -= other._real
            self._imagine -= other._imagine
        elif isinstance(other, int | float | Fraction):
            self._real -= Fraction(other)
            self._imagine -= Fraction(other)
        else:
            return NotImplemented
        return self

    def __imul__(self, other):
        if isinstance(other, self.__class__):
            real = self._real * other._real - self._imagine * other._imagine
            imagine = self._real * other._imagine + self._imagine * other._real
            self._real = real
            self._imagine = imagine
        elif isinstance(other, int | float | Fraction):
            self._real *= Fraction(other)
            self._imagine *= Fraction(other)
        else:
            return NotImplemented
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
            return self
        elif isinstance(other, int | float | Fraction):
            if other == 0:
                raise ZeroDivisionError
            self.real = Fraction(self.real)
            self.imagine = Fraction(self.imagine)
            self.real /= Fraction(other)
            self.imagine /= Fraction(other)
            return self
        return NotImplemented

    def __neg__(self):
        return self.__class__(-self.real, -self.imagine)

    def arg(self):
        return math.atan2(float(self.imagine), float(self.real))


