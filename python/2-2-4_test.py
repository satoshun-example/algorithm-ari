#!/usr/local/bin/python3


## saruman army
def saruman_army(n, r, x):
    s = 0
    before = x[0]
    for e in x[1::]:
        # containt point
        if e - r >= before:
            continue
        before = e
        s += 1
    return s


def test_saruman_army():
    for (n, r, x, result) in [
        (6, 10, [1, 7, 15, 20, 30, 50], 3),
    ]:
        assert saruman_army(n, r, x) == result
