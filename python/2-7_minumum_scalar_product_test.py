#!/usr/local/bin/python3


def minimum_scalar_product(n, v1, v2):
    v1 = sorted(v1, reverse=True)
    v2 = sorted(v2)
    s = 0
    while v1:
        l, r = v1.pop(), v2.pop()
        s += l * r
    return s


def test_minimum_scalar_product():
    for (n, v1, v2, result) in [
        (3, (1, 3, -5), (-2, 4, 1), -25),
        (5, (1, 2, 3, 4, 5), (1, 0, 1, 0, 1), 6),
    ]:
        assert minimum_scalar_product(n, v1, v2) == result
