"""Implement a class for numerical differentiation."""


class Central:
    def __init__(self, func, h=1E-5):
        self.func = func
        self.h = h

    def __call__(self, x):
        f = self.func
        h = self.h
        return (f(x+h)-f(x-h)) / (2*h)
