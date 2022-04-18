from Ex.geometric_shapes4 import Triangle


def test_triangle_area():
    """Verify the area of a triangle with vertices (0,0), (1,0), and (0,2)."""
    v1 = (0, 0)
    v2 = (1, 0)
    v3 = (0, 2)
    vertices = [v1, v2, v3]
    expected = 1
    triangle = Triangle(*vertices)
    computed = triangle.area()
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected} (expected)"
    assert success, msg
