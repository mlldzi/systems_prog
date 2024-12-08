from classes import *
import unittest

class TestComplex(unittest.TestCase):

    def test_init(self):
        c = Complex(1, 2)
        self.assertEqual(c.real, Fraction(1))
        self.assertEqual(c.imagine, Fraction(2))

        c = Complex(Fraction(1, 2), Fraction(3, 4))
        self.assertEqual(c.real, Fraction(1, 2))
        self.assertEqual(c.imagine, Fraction(3, 4))

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
        self.assertEqual(result.real, Fraction(4))
        self.assertEqual(result.imagine, Fraction(6))

        result = c1 + 1
        self.assertEqual(result.real, Fraction(2))
        self.assertEqual(result.imagine, Fraction(2))

    def test_sub(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 - c2
        self.assertEqual(result.real, Fraction(-2))
        self.assertEqual(result.imagine, Fraction(-2))

        result = c1 - 1
        self.assertEqual(result.real, Fraction(0))
        self.assertEqual(result.imagine, Fraction(2))

    def test_mul(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 * c2
        self.assertEqual(result.real, Fraction(-5))
        self.assertEqual(result.imagine, Fraction(10))

        result = c1 * 2
        self.assertEqual(result.real, Fraction(2))
        self.assertEqual(result.imagine, Fraction(4))

    def test_truediv(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 / c2
        self.assertEqual(result.real, Fraction(11, 25))
        self.assertEqual(result.imagine, Fraction(2, 25))

        result = c1 / 2
        self.assertEqual(result.real, Fraction(1, 2))
        self.assertEqual(result.imagine, Fraction(1))

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
        self.assertEqual(abs(c), Fraction(5))

    def test_pow(self):
        c = Complex(1, 1)
        result = c ** 2
        self.assertEqual(result.real, Fraction(0))
        self.assertEqual(result.imagine, Fraction(2))

    def test_iadd(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 += c2
        self.assertEqual(c1.real, Fraction(4))
        self.assertEqual(c1.imagine, Fraction(6))

    def test_isub(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 -= c2
        self.assertEqual(c1.real, Fraction(-2))
        self.assertEqual(c1.imagine, Fraction(-2))

    def test_imul(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 *= c2
        self.assertEqual(c1.real, Fraction(-5))
        self.assertEqual(c1.imagine, Fraction(10))

    def test_idiv(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 /= c2
        self.assertEqual(c1.real, Fraction(11, 25))
        self.assertEqual(c1.imagine, Fraction(2, 25))

    def test_neg(self):
        c = Complex(1, 2)
        self.assertEqual(str(-c), "-1 - 2i")

    def test_arg(self):
        c = Complex(1, 1)
        self.assertEqual(c.arg(), math.pi / 4)

if __name__ == '__main__':
    unittest.main()