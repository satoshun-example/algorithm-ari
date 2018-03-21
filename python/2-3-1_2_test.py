#!/usr/local/bin/python3

#動的計画法


## ナップサック with メモ化
def knapsack(n, l, w):
    return _knapsack(
        l,
        len(l) - 1,
        w,
        [[0 for _ in range(w + 1)] for _ in range(len(l) + 1)],
    )


def _knapsack(l, cp, cw, memo):
    if cp == -1:
        return 0
    if cw == 0:
        return 0
    if memo[cp][cw] != 0:
        return memo[cp][cw]
    if cw - l[cp][0] < 0:
        res = _knapsack(l, cp - 1, cw, memo)
    else:
        res = max(
            _knapsack(l, cp - 1, cw, memo),
            _knapsack(l, cp - 1, cw - l[cp][0], memo) + l[cp][1],
        )
    memo[cp][cw] = res
    return res


def test_knapsack2():
    for (n, l, w, result) in [
        (4, [(2, 3), (1, 2), (3, 4), (2, 2)], 5, 7),
    ]:
        assert knapsack(n, l, w) == result
