"""Implement special methods in a class."""


class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        from math import sin, exp
        a = self.a
        w = self.w
        return exp(-a*x)*sin(w*x)

    def __call__(self, x):
        from math import sin, exp
        a = self.a
        w = self.w
        return exp(-a*x)*sin(w*x)

    def __str__(self):
        return "exp(-a*x)*sin(w*x)"
