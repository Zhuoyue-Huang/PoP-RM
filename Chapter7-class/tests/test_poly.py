from Ex.Polynomial import Polynomial
import numpy


def test_polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    assert p3.coeff == p3_exact.coeff

    p4 = p1*p2
    p4_exact = Polynomial(numpy.array([0, 1, -1, 0, -6, 5, 1]))
    assert numpy.allclose(p4.coeff, p4_exact.coeff, rtol=1E-14)

    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    assert p5.coeff == p5_exact.coeff

    p6 = Polynomial([0, 1, 0, 0, -6, -1])  # p2
    p6.differentiate()
    p6_exact = p5_exact
    assert p6.coeff == p6_exact.coeff

    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 - p2
    p3_exact = Polynomial([1, -2, 0, 0, 6, 1])
    assert p3.coeff == p3_exact.coeff
