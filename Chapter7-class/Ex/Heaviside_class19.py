"""Make a class for the Heaviside function."""
from math import pi, sin


class Heaviside:
    def __init__(self, eps=0):
        self.eps = eps

    def __call__(self, x):
        eps = self.eps
        if eps == 0:
            if x < 0:
                return 0
            else:
                return 1
        elif eps > 0:
            if x < eps:
                return 0
            elif -eps <= x <= eps:
                return 1/2 + x/(2*eps) + sin(pi*x/eps)/(2*pi)
            else:
                return 1
        else:
            return NotImplemented
