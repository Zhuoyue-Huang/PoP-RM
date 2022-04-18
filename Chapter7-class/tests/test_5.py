from Ex.Quadratic5 import Quadratic


def test_value():
    f = Quadratic(1, -3, 2)
    expected = 2
    computed = f.value(0)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_roots():
    f = Quadratic(1, -3, 2)
    expected = (2, 1)
    computed = f.roots()
    success = expected == computed
    msg = f"computed roots={computed} != {expected} (expected)"
    assert success, msg
