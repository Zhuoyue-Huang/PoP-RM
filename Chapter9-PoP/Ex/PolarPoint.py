class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PolarPoint(Point):
    def __init__(self, r, theta):
        from math import sin, cos
        self.r = r
        self.theta = theta
        super().__init__(r*cos(theta), r*sin(theta))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.r}, {self.theta})"
