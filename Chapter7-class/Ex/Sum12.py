"""Make a class for summation of series."""
import math


class Sum:
    def __init__(self, term, M, N):
        self.term = term
        self.M = M
        self.N = N

    def __call__(self, x):
        n = self.N - self.M + 1
        S = 0
        for i in range(n):
            S += self.term(i, x)
        return S


def term(k, x):
    """Apply Taylor approximation."""
    return (-1) ** k * x ** (2 * k + 1) / math.factorial(2 * k + 1)
