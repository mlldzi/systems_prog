from classes import *
import unittest


class TestFraction(unittest.TestCase):

    def test_init(self):
        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(2, 4)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_float_to_fraction(self):
        f = Fraction(0.5)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(0.75)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    def test_strange_input(self):
        f1 = Fraction(0.2, 1.4)
        self.assertEqual(str(f1), "1/7")

        f2 = Fraction(0.2)
        self.assertEqual(str(f2), "1/5")

        f3 = Fraction(2, 2.3)
        self.assertEqual(str(f3), "20/23")

        f4 = Fraction(2.3, 2)
        self.assertEqual(str(f4), "23/20")

        f5 = Fraction(Fraction(1, 3), Fraction(4, 7))
        self.assertEqual(str(f5), "7/12")

        f6 = Fraction(2, Fraction(4, 7))
        self.assertEqual(str(f6), "7/2")

        f7 = Fraction(Fraction(2, 3), 2)
        self.assertEqual(str(f7), "1/3")

    def test_str(self):
        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2")

        f = Fraction(2)
        self.assertEqual(str(f), "2")

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_truediv(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0)

        result = f1 / 2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

        self.assertEqual(f1.__truediv__("string"), NotImplemented)

    def test_pow(self):
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

        self.assertEqual(f.__pow__("string"), NotImplemented)

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 == f2)

        f3 = Fraction(2, 4)
        self.assertTrue(f1 == f3)

        f4 = Fraction(1, 3)
        self.assertFalse(f1 == f4)

        self.assertEqual(f1.__eq__("string"), NotImplemented)

    def test_ne(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertFalse(f1 != f2)

        f3 = Fraction(1, 3)
        self.assertTrue(f1 != f3)

        self.assertEqual(f1.__ne__("string"), NotImplemented)

    def test_lt(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertFalse(f1 < f2)

        f3 = Fraction(2, 3)
        self.assertTrue(f1 < f3)

        self.assertTrue(f1 < 1)
        self.assertFalse(f1 < 0)

        self.assertEqual(f1.__lt__("string"), NotImplemented)

    def test_le(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 <= f2)

        f3 = Fraction(2, 3)
        self.assertTrue(f1 <= f3)

        self.assertTrue(f1 <= 1)
        self.assertFalse(f1 <= 0)

        self.assertEqual(f1.__le__("string"), NotImplemented)

    def test_gt(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1 > f2)

        f3 = Fraction(2, 3)
        self.assertFalse(f1 > f3)

        self.assertFalse(f1 > 1)
        self.assertTrue(f1 > 0)

        self.assertEqual(f1.__gt__("string"), NotImplemented)

    def test_ge(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertTrue(f1 >= f2)

        f3 = Fraction(1, 3)
        self.assertTrue(f1 >= f3)

        self.assertFalse(f1 >= 1)
        self.assertTrue(f1 >= 0)

        self.assertEqual(f1.__ge__("string"), NotImplemented)

    def test_round(self):
        f = Fraction(3, 2)
        self.assertEqual(round(f), Fraction(2, 1))
        # почему-то не работает просто с 2, пишет:
        # Expected :Fraction(numerator=2, denominator=1)
        # Actual   :2

        f = Fraction(1, 3)
        self.assertEqual(round(f, 2), Fraction(33, 100))

    def test_float(self):
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

    def test_int(self):
        f = Fraction(3, 2)
        self.assertEqual(int(f), 1)

    def test_neg(self):
        f = Fraction(1, 2)
        self.assertEqual(-f, Fraction(-1, 2))

    def test_abs(self):
        f = Fraction(-1, 2)
        self.assertEqual(abs(f), Fraction(1, 2))

        f = Fraction(1, -2)
        self.assertEqual(abs(f), Fraction(1, 2))


class TestComplex(unittest.TestCase):

    def test_init(self):
        c = Complex(1, 2)
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imagine, 2)

        c = Complex(Fraction(1, 2), Fraction(3, 4))
        self.assertEqual(c.real, Fraction(1, 2))
        self.assertEqual(c.imagine, Fraction(3, 4))

    def test_setters(self):
        c = Complex(1, 2)
        c.real = -2
        c.imagine = 1000
        self.assertEqual(c, Complex(-2, 1000))

    def test_str(self):
        c = Complex(1, 2)
        self.assertEqual(str(c), "1 + 2i")

        c = Complex(1, -2)
        self.assertEqual(str(c), "1 - 2i")

        c = Complex(1, 0)
        self.assertEqual(str(c), "1")

    def test_add(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 + c2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imagine, 6)

        result = c1 + 1
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imagine, 2)

    def test_sub(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 - c2
        self.assertEqual(result.real, -2)
        self.assertEqual(result.imagine, -2)

        result = c1 - 1
        self.assertEqual(result.real, 0)
        self.assertEqual(result.imagine, 2)

    def test_mul(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 * c2
        self.assertEqual(result.real, -5)
        self.assertEqual(result.imagine, 10)

        result = c1 * 2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imagine, 4)

    def test_truediv(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 / c2
        self.assertEqual(result.real, Fraction(11, 25))
        self.assertEqual(result.imagine, Fraction(2, 25))

        result = c1 / 2
        self.assertEqual(result.real, Fraction(1, 2))
        self.assertEqual(result.imagine, 1)

        with self.assertRaises(ZeroDivisionError):
            c1 / 0

    def test_eq(self):
        c1 = Complex(1, 2)
        c2 = Complex(1, 2)
        self.assertTrue(c1 == c2)

        c3 = Complex(1, 3)
        self.assertFalse(c1 == c3)

    def test_abs(self):
        c = Complex(3, 4)
        self.assertEqual(abs(c), 5)

    def test_pow(self):
        c = Complex(1, 1)
        result = c ** 2
        self.assertEqual(result.real, 0)
        self.assertEqual(result.imagine, 2)

    def test_iadd(self):
        c1 = Complex(1, 2)
        c1 += 1
        self.assertEqual(c1.real, 2)
        self.assertEqual(c1.imagine, 3)

        c1 = Complex(1, 2)
        c1 += Complex(3, 4)
        self.assertEqual(c1.real, 4)
        self.assertEqual(c1.imagine, 6)

        c1 = Complex(Fraction(1, 3), Fraction(2, 3))
        c1 += Fraction(1, 5)
        self.assertEqual(c1.real, Fraction(8, 15))
        self.assertEqual(c1.imagine, Fraction(13, 15))

        self.assertEqual(c1.__iadd__("string"), NotImplemented)

    def test_isub(self):
        c1 = Complex(1, 2)
        c1 -= 1
        self.assertEqual(c1.real, 0)
        self.assertEqual(c1.imagine, 1)

        c1 = Complex(1, 2)
        c1 -= Complex(3, 4)
        self.assertEqual(c1.real, -2)
        self.assertEqual(c1.imagine, -2)

        c1 = Complex(1, 2)
        c1 -= Fraction(1, 2)
        self.assertEqual(c1.real, Fraction(1, 2))
        self.assertEqual(c1.imagine, Fraction(3, 2))

        self.assertEqual(c1.__isub__("string"), NotImplemented)

    def test_imul(self):
        c1 = Complex(1, 2)
        c1 *= 2
        self.assertEqual(c1.real, 2)
        self.assertEqual(c1.imagine, 4)

        c1 = Complex(1, 2)
        c1 *= Complex(3, 4)
        self.assertEqual(c1.real, -5)
        self.assertEqual(c1.imagine, 10)

        c1 = Complex(1, 2)
        c1 *= Fraction(1, 2)
        self.assertEqual(c1.real, Fraction(1, 2))
        self.assertEqual(c1.imagine, 1)

        self.assertEqual(c1.__imul__("string"), NotImplemented)

    def test_idiv(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 /= c2
        self.assertEqual(c1.real, Fraction(11, 25))
        self.assertEqual(c1.imagine, Fraction(2, 25))

        c1 = Complex(1, 2)
        c1 /= 2
        self.assertEqual(c1.real, Fraction(1, 2))
        self.assertEqual(c1.imagine, 1)

        with self.assertRaises(ZeroDivisionError):
            c1 /= 0

        self.assertEqual(c1.__idiv__("string"), NotImplemented)
        
    def test_temp(self):
        c1 = Complex(1, 2)
        with self.assertRaises(ZeroDivisionError):
            c1 /= 0

    def test_ne(self):
        c1 = Complex(1, 2)
        c2 = Complex(1, 2)
        self.assertFalse(c1 != c2)

        c3 = Complex(1, 3)
        self.assertTrue(c1 != c3)

        self.assertEqual(c1.__ne__("string"), NotImplemented)

    def test_neg(self):
        c1 = Complex(1, 2)
        self.assertEqual(c1.__neg__(), Complex(-1, -2))

    def test_arg(self):
        c = Complex(1, 1)
        self.assertEqual(c.arg(), math.pi / 4)

    def test_type_error_add(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c + "string"

    def test_type_error_sub(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c - "string"

    def test_type_error_mul(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c * "string"

    def test_type_error_truediv(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c / "string"

    def test_type_error_pow(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c ** "string"

    def test_not_implemented_add(self):
        c = Complex(1, 2)
        self.assertEqual(c.__add__("string"), NotImplemented)

    def test_not_implemented_sub(self):
        c = Complex(1, 2)
        self.assertEqual(c.__sub__("string"), NotImplemented)

    def test_not_implemented_mul(self):
        c = Complex(1, 2)
        self.assertEqual(c.__mul__("string"), NotImplemented)

    def test_not_implemented_truediv(self):
        c = Complex(1, 2)
        self.assertEqual(c.__truediv__("string"), NotImplemented)

    def test_not_implemented_pow(self):
        c = Complex(1, 2)
        self.assertEqual(c.__pow__("string"), NotImplemented)

    def test_type_error_iadd(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c += "string"

    def test_type_error_isub(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c -= "string"

    def test_type_error_imul(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c *= "string"

    def test_type_error_idiv(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c /= "string"

    def test_not_implemented_eq(self):
        c = Complex(1, 2)
        self.assertEqual(c.__eq__("string"), NotImplemented)

    def test_not_implemented_ne(self):
        c = Complex(1, 2)
        self.assertEqual(c.__ne__("string"), NotImplemented)

    def test_type_error_abs(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            abs(c, "extra_arg")

    def test_type_error_neg(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            -c("extra_arg")

    def test_type_error_arg(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c.arg("extra_arg")

    def test_repr(self):
        c = Complex(1, 2)
        self.assertEqual(repr(c), "Complex(real=1, imagine=2)")

        c = Complex(Fraction(1, 2), Fraction(3, 4))
        self.assertEqual(repr(c), "Complex(real=1/2, imagine=3/4)")

    def test_truediv_zero_division(self):
        c1 = Complex(1, 2)
        c2 = Complex(0, 0)
        with self.assertRaises(ZeroDivisionError):
            c1 / c2
