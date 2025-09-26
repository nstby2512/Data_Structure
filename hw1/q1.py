import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self._simplify()

    def _simplify(self):
        #化简分数
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        if self.denominator < 0 :
            self.denominator *= -1
            self.numerator *= -1

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)
    
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"
    
a, b, c, d = map(int, input().split())
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1 + f2)