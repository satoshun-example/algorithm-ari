#!/usr/local/bin/python3

#動的計画法


## ナップサック
def knapsack(n, l, w):
    return _knapsack(l, w, 0, 0)


def _knapsack(l, mw, cw, cv):
    if len(l) == 0:
        return cv
    iw = l[0][0]
    iv = l[0][1]
    if iw + cw > mw:
        return _knapsack(l[1::], mw, cw, cv)
    return max(
        _knapsack(l[1::], mw, cw, cv), _knapsack(l[1::], mw, cw + iw, cv + iv))


def test_knapsack():
    for (n, l, w, result) in [
        (4, [(2, 3), (1, 2), (3, 4), (2, 2)], 5, 7),
    ]:
        assert knapsack(n, l, w) == result
