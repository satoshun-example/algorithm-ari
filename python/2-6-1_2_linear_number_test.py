#!/usr/local/bin/python3


# 線分上の格子点の個数
# ユークリッドの互除法
def linear_number(p1, p2):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    return gcd(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) - 1


def test_linear_number():
    for (p1, p2, result) in [
        ((1, 11), (5, 3), 3),
    ]:
        assert linear_number(p1, p2) is result
