from Ex.Rope14 import Rope


def test_value_1():
    rope1 = Rope(2)
    rope2 = Rope(2)
    rope3 = rope1 + rope2
    expected = 5
    computed = rope3.nodes
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg


def test_value_2():
    rope1 = Rope(2)
    rope2 = Rope(2)
    rope3 = rope1 + rope2
    rope3 += rope1 + rope2
    expected = 11
    computed = rope3.nodes
    success = expected == computed
    msg = f"computed value={computed} != {expected} (expected)"
    assert success, msg
