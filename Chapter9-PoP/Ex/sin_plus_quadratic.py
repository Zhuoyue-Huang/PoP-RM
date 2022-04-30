from Ex.Line_Para import Parabola


class Sin_plus_quadratic(Parabola):
    def __init__(self, A, w, a, b, c):
        super().__init__(c, b, a)
        self.A = A
        self.w = w

    def __call__(self, x):
        from math import sin
        return super().__call__(x) + self.A*sin(self.w*x)
