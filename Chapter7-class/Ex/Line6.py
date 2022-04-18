"""Make a class for straight lines."""


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def value(self, x):
        (x1, y1) = self.p1
        (x2, y2) = self.p2
        a = (y2-y1) / (x2-x1)
        b = y2 - a*x2
        return a*x + b
