"""Modify a class for numerical differentiation."""


class Derivative:
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)

    def __call__(self, x):
        f, h = self._f, self._h
        return (f(x+h) - f(x))/h

    def get_precision(self):
        h = self._h
        return h

    def set_precision(self, h):
        self._h = h
