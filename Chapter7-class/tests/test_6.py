from Ex.Line6 import Line


def test_value_1():
    p1 = [0, 0]
    p2 = [1, 1]
    f = Line(p1, p2)
    expected = 2
    computed = f.value(2)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_2():
    p1 = [0, 2]
    p2 = [1, 3]
    f = Line(p1, p2)
    expected = 6
    computed = f.value(4)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg
