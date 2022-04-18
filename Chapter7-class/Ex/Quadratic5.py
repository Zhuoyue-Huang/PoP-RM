"""Make a class for quadratic functions."""


class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c

    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        x1 = (-b+(b**2-4*a*c)**2) / (2*a)
        x2 = (-b-(b**2-4*a*c)**2) / (2*a)
        return x1, x2
