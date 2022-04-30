from Ex.Line_Para import Parabola


class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        super().__init__(c0, c1, c2)  # let Line store c0 and c1
        self.c3 = c3

    def __call__(self, x):
        return super().__call__(x) + self.c3*x**3


class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        super().__init__(c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        return super().__call__(x) + self.c4*x**4
