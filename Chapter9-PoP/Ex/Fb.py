class F:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, t):
        from math import exp, sin
        return exp(-self.a*t)*sin(self.b*t)


class Fb(F):
    def __init__(self, a, t):
        self.a, self.t = a, t

    def __call__(self, b):
        f = F(self.a, b)
        return f(self.t)
