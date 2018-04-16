#!/usr/local/bin/python3


def cable_master(n, k, l):
    s = round(sum(l) / k, 2)
    d = round(sum(l) / k / 2, 2)

    def count(v):
        c = 0
        for e in l:
            c += e // v
        return c

    while True:
        c = count(s)
        if d <= 0.01:
            break
        if c < k:
            s = round(s - d, 2)
        else:
            s = round(s + d, 2)
        d = round(d / 2, 2)
    return s


def test_cable_master():
    for (n, k, l, result) in [
        (4, 11, (8.02, 7.43, 5.57, 5.39), 2.00),
    ]:
        assert cable_master(n, k, l) == result
