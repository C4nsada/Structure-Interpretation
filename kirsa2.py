from math import gcd


class RationalNumber:
    def __init__(self, high, low=1):
        if low == 0:
            raise ValueError("denominator must not be 0")
        self.high = high
        self.low = low
        self.reduce()

# Minimizes the rational number by its 
# greatest common divisor
    def reduce(self):
        g = gcd(self.high, self.low)
        self.high //= g
        self.low //= g

    def get_low(self):
        return self.low

    def get_high(self):
        return self.high

    def added_num_dem(self):
        return self.high+self.low


# Usage example
rat = RationalNumber(10,2)
print(rat.get_high())
print(rat.get_low())
print(rat.added_num_dem())
