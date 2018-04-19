#!/usr/local/bin/python3


def aggressive_cows(n, m, x):
    x = sorted(x)
    m = m - 2
    p = [x[0], x[-1]]
    x = x[1:-1]

    def distance(hoge):
        dd = 10000
        for i in range(len(p)):
            ddd = abs(p[i] - hoge)
            if dd > ddd:
                dd = ddd
        return dd

    while m:
        m -= 1
        dd = distance(x[0])
        i = 0
        for ii in range(1, len(x)):
            d = distance(x[ii])
            if dd < d:
                i = ii
        p += [x[i]]
        del x[i]
    p = sorted(p)
    d = 10000
    for i in range(len(p) - 1):
        dd = p[i + 1] - p[i]
        if dd < d:
            d = dd
    return d


def test_aggressive_cows():
    for (n, m, x, result) in [
        (5, 3, (1, 2, 8, 4, 9), 3),
    ]:
        assert aggressive_cows(n, m, x) == result
