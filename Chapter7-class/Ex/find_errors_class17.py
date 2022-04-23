"""Examine a program."""


class Backward(object):
    def __init__(self, f, h=1E-9):
        self.f, self.h = f, h

    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x-h))/h
