from Ex.Polynomial import Polynomial


class Parabola(Polynomial):
    def __init__(self, c0, c1, c2):
        super().__init__([c0, c1, c2])
        self.c0 = self.coeff[0]
        self.c1 = self.coeff[1]
        self.c2 = self.coeff[2]


class Line(Parabola):
    def __init__(self, c0, c1):
        super().__init__(c0, c1, 0)
