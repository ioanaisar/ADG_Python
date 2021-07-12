if __name__ == '__main__':
    def gcd(x, y):
        if x >= y:
            if y == 0:
                return x
            return gcd(x % y, y)
        else:
            if x == 0:
                return y
            return gcd(x, y % x)

    def lcm(x, y):
        return (x / gcd(x, y)) * y

    class Fractie:
        def __init__(self, numerator, denominator):
            self.numerator = numerator
            self.denominator = denominator

        def __str__(self):
            print(f'{self.numerator}/{self.denominator}')

        def __add__(self, fraction2):
            common_denominator = lcm(self.denominator, fraction2.denominator)
            common_numerator = self.numerator * (common_denominator//self.denominator)+fraction2.numerator * (common_denominator//fraction2.denominator)
            return Fractie(common_numerator, common_denominator)

        def __sub__(self, fraction2):
            common_denominator = lcm(self.denominator, fraction2.denominator)
            common_numerator = self.numerator * (common_denominator//self.denominator)-fraction2.numerator * (common_denominator//fraction2.denominator)
            return Fractie(common_numerator, common_denominator)

        def inverse(self):
            return Fractie(self.denominator, self.numerator)

    f1 = Fractie(1, 2)
    f2 = Fractie(1, 5)
    print("Fractions:")
    f1.__str__()
    f2.__str__()
    print("Sum is ")
    (f1.__add__(f2)).__str__()
    print("Difference is ")
    (f1.__sub__(f2)).__str__()
    print("Inverse is ")
    (f1.inverse()).__str__()
