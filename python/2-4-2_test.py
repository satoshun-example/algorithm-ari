#!/usr/local/bin/python3


# トラックで距離L
def priority_queue(n, l, p, a, b):
    c = 0
    cp = 0
    while True:
        l -= p
        cp += p
        if l <= 0:
            break
        ii = -1
        for i, e in enumerate(a):
            if e <= cp:
                if b[i] >= b[ii]:
                    ii = i
        if ii == -1:
            return -1
        p = b[ii]
        c += 1
        del b[ii]
        del a[ii]
    return c


def test_priority_queue():
    for (n, l, p, a, b, result) in [
        (4, 25, 10, [10, 14, 20, 21], [10, 5, 2, 4], 2),
    ]:
        assert priority_queue(n, l, p, a, b) == result
