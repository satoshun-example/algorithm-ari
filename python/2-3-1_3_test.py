#!/usr/local/bin/python3

#動的計画法


## ナップサック with 漸化式
def knapsack(n, l, w):
    m = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for ci in range(n - 1, -1, -1):
        for cw in range(w + 1):
            if cw >= l[ci][0]:
                m[ci][cw] = max(
                    m[ci + 1][cw],
                    m[ci + 1][cw - l[ci][0]] + l[ci][1],
                )
            else:
                m[ci][cw] = m[ci + 1][cw]
    return m[0][w]


def test_knapsack3():
    for (n, l, w, result) in [
        (4, [(2, 3), (1, 2), (3, 4), (2, 2)], 5, 7),
    ]:
        assert knapsack(n, l, w) == result
