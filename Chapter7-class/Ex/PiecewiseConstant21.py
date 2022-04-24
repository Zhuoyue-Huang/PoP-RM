"""Make a class for piecewise constant functions."""


from array import array
from numbers import Number


class PiecewiseConstant:
    def __init__(self, lis, xmax=100):
        self.lis = lis
        self.xmax = xmax

    def __call__(self, x):
        if isinstance(x, array):
            f = []
            for xi in x:
                f.append(self.__call__(xi))
            return f
        if isinstance(x, Number):
            lis = self.lis
            if lis[-1][1] < x < self.xmax:
                return lis[-1][0]
            elif x > self.xmax:
                return 0
            for i in len(lis):
                if x < lis[i][1]:
                    return lis[i-1][0]
