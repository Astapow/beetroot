class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self, num, den):
        while num % den != 0:
            oldm = num
            oldn = den

            num = oldn
            den = oldm % oldn
        return den

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator

        return first_num == second_num

    def __add__(self, other):
        sum_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        sum_denominator = self.denominator * other.denominator
        result = self.gcd(sum_numerator, sum_denominator)

        return Fraction(sum_numerator // result, sum_denominator // result)

    def __sub__(self, other):
        sub_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        sub_denominator = self.denominator * other.denominator
        result = self.gcd(sub_numerator, sub_denominator)

        return Fraction(sub_numerator // result, sub_denominator // result)

    def __mul__(self, other):
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        result = self.gcd(mul_numerator, mul_denominator)

        return Fraction(mul_numerator // result, mul_denominator // result)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("you're stupid")

        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        result = self.gcd(div_numerator, div_denominator)

        return Fraction(div_numerator // result, div_denominator // result)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)

assert x + y == Fraction(3, 4)
assert x - y == Fraction(1, 4)
assert x * y == Fraction(1, 8)
assert x / y == Fraction(2, 1)
