""" Flexible handling of function arguments."""


from numbers import Number


class Line2:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def value(self, x):
        p1 = self.p1
        p2 = self.p2
        flag1 = 0
        flag2 = 0
        if isinstance(p1, Number):
            flag1 += 1
        if isinstance(p2, Number):
            flag2 += 1
        if flag1 == 0 and flag2 == 0:
            (x1, y1) = p1
            (x2, y2) = p2
            a = (y2-y1) / (x2-x1)
            b = y2 - a*x2
            return a*x + b
        elif flag1 == 1 and flag2 == 1:
            return p1*x + p2
        else:
            if flag1 == 1:
                (x2, y2) = p2
                return y2 + p1*(x-x2)
            elif flag2 == 1:
                (x1, y1) = p1
                return y1 + p2*(x-x1)
