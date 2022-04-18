"""Make classes for a rectangle and a triangle."""


class Rectangle:
    def __init__(self, w, h, ll_corner):
        self.w = w
        self.h = h
        self.point = ll_corner

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w+self.h)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        (x1, y1) = self.p1
        (x2, y2) = self.p2
        (x3, y3) = self.p3
        return abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1) / 2

    def perimeter(self):
        (x1, y1) = self.p1
        (x2, y2) = self.p2
        (x3, y3) = self.p3
        line12 = ((x1-x2)**2+(y1-y2)**2)**0.5
        line13 = ((x1-x3)**2+(y1-y3)**2)**0.5
        line32 = ((x3-x2)**2+(y3-y2)**2)**0.5
        return line12 + line13 + line32
