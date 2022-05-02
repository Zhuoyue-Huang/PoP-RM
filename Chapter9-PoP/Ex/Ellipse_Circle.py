class Ellipse:
    def __init__(self, x0, y0, a, b):
        self.x0 = x0
        self.y0 = y0
        self.a = a
        self.b = b

    def area(self):
        from math import pi
        return pi*self.a*self.b

    def circumference(self):
        from math import pi, sqrt
        return 2*pi*sqrt((self.a**2+self.b**2)/2)


class Circle(Ellipse):
    def __init__(self, x0, y0, r):
        super().__init__(x0, y0, r, r)
