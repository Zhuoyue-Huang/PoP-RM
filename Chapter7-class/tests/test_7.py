from Ex.Line7 import Line2


def test_value_1():
    p1 = [0, 0]
    p2 = [1, 1]
    f = Line2(p1, p2)
    expected = 2
    computed = f.value(2)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_2():
    p1 = [0, 2]
    p2 = [1, 3]
    f = Line2(p1, p2)
    expected = 6
    computed = f.value(4)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_3():
    p1 = 1
    p2 = [1, 3]
    f = Line2(p1, p2)
    expected = 6
    computed = f.value(4)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_4():
    p1 = [1, 3]
    p2 = 1
    f = Line2(p1, p2)
    expected = 6
    computed = f.value(4)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_5():
    p1 = 1
    p2 = 2
    f = Line2(p1, p2)
    expected = 6
    computed = f.value(4)
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg
