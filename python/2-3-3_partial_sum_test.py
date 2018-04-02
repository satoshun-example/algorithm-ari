#!/usr/local/bin/python3


## 個数制限付き部分和問題 part1
def partial_sum(n, a, m, k):
    dp = [[True if i == 0 and j == 0 else False for i in range(k + 1)]
          for j in range(n + 1)]
    for i in range(n):
        for v in range(1, k + 1):
            for c in range(0, m[i] + 1):
                d = c * a[i]
                if d > v:
                    break
                dp[i + 1][v] = dp[i + 1][v] or dp[i][v - d]
    return dp[-1][-1]


def test_partial_sum():
    for (n, a, m, k, result) in [
        (3, (3, 5, 8), (3, 2, 2), 17, True),
    ]:
        assert partial_sum(n, a, m, k) == result
