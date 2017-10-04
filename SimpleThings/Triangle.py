import math

class Triangle:
    def __init__(self, *sides):
        if len(sides) == 1:
            self.one = self.two = self.three = sides[0]
        elif len(sides) == 3:
            self.one = sides[0]
            self.two = sides[1]
            self.three = sides[2]

    def __repr__(self):
        return "<Triangle with A = %d" % self.one \
               + ", B = %d" % self.two \
               + ", C = %d" % self.three + ">"

    def perimeter(self):
        return self.one + self.two + self.three

    def area(self):
        p = (self.perimeter()) / 2
        return math.sqrt(p * (p - self.one) * (p - self.two) * (p - self.three))
