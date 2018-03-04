#!/usr/local/bin/python3

##三角形##

def triangle1(n: int, a: list):
    size = len(a)
    m = 0
    for x1 in range(size):
        for x2 in range(size):
            for x3 in range(size):
                if x1 == x2 or x1 == x3 or x2 == x3:
                    continue
                l1 = max(a[x1], a[x2], a[x3])
                if a[x1] + a[x2] + a[x3] - l1 > l1:
                    m = max(m, a[x1] + a[x2] + a[x3])
    return m


def test_triangle1():
    for (n, a, result) in [
        (5, [2, 3, 4, 5, 10], 12),
        (4, [4, 5, 10, 20], 0)
    ]:
        assert result == triangle1(n, a)
