"""Flexible handling of function arguments."""
from numpy import linspace
from Ex.Lagrange_poly8 import p_L


class LagrangeInterpolation:
    def __init__(self, func, x, n):
        self.func = func
        self.x = x
        self.n = n
        self.p1 = linspace(x[0], x[1], n)
        self.p2 = [func(x) for x in self.p1]

    def plot(self):
        from matplotlib.pyplot import plot
        xp = self.xp
        yp = self.yp
        pp = [p_L(x, xp, yp) for x in xp]
        plot(xp, pp)
