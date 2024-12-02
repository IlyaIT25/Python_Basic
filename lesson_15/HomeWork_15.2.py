from math import gcd

class Fraction:
    def __init__(self, a, b, simplify_on_create=True):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        self.a = a
        self.b = b
        if simplify_on_create:
            self.simplify()

    def simplify(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b + other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator, simplify_on_create=False)
        raise ValueError("Можна додавати лише екземпляр класу Fraction")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b, simplify_on_create=False)
        raise ValueError("Можна множити лише на екземпляр класу Fraction")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b - other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator, simplify_on_create=False)
        raise ValueError("Можна віднімати лише екземпляр класу Fraction")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        raise ValueError("Можна порівнювати лише екземпляри класу Fraction")

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        raise ValueError("Можна порівнювати лише екземпляри класу Fraction")

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тестування
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18', f"Expected 'Fraction: 21, 18', got {str(f_c)}"
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18', f"Expected 'Fraction: 6, 18', got {str(f_d)}"
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18', f"Expected 'Fraction: 3, 18', got {str(f_e)}"

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print("OK")
