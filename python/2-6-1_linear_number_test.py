#!/usr/local/bin/python3


# 線分上の格子点の個数
def linear_number(p1, p2):
    y = p1[1]
    d = (p1[1] - p2[1]) / (p1[0] - p2[0])
    c = 0
    for x in range(p1[0] + 1, p2[0]):
        y += d
        if int(y) == y:
            c += 1
    return c


def test_linear_number():
    for (p1, p2, result) in [
        ((1, 11), (5, 3), 3),
    ]:
        assert linear_number(p1, p2) is result
