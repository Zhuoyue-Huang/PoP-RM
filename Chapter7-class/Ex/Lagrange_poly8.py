"""Wrap functions in a class."""


class LagrangeInterpolation:
    def __init__(self, xp, yp):
        self.xp = xp
        self.yp = yp

    def plot(self):
        from matplotlib.pyplot import plot
        xp = self.xp
        yp = self.yp
        pp = [p_L(x, xp, yp) for x in xp]
        plot(xp, pp)


def p_L(x, xp, yp):
    n = len(xp)
    p_L = 0
    for i in range(n):
        p_L += yp[i] * L_k(x, i, xp)
    return p_L


def L_k(x, k, xp):
    n = len(xp)
    xp = list(xp)
    L_k = 1
    xk = xp[k]
    xp = xp[:k] + xp[k+1:]
    for i in range(n-1):
        L_k *= (x-xp[i])/(xk-xp[i])
    return L_k
