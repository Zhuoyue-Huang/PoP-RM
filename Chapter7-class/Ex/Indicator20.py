"""Make a class for the indicator function."""
from Ex.Heaviside_class19 import Heaviside


class Indicator:
    def __init__(self, a, b, eps=0):
        self.a = a
        self.b = b
        self.eps = eps

    def __call__(self, x):
        a = self.a
        b = self.b
        eps = self.eps
        H = Heaviside(eps)
        return H(x-a)*H(b-x)
