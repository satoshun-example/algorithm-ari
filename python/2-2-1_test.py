#!/usr/local/bin/python3


## コイン/貪欲法
def coin(c1, c5, c10, c50, c100, c500, s):
    coins = [c500, c100, c50, c10, c5, c1]
    coinMap = [500, 100, 50, 10, 5, 1]
    c = 0
    while True:
        if s == 0:
            break
        for i, v in enumerate(coins):
            if v != 0 and coinMap[i] <= s:
                s -= coinMap[i]
                c += 1
                coins[i] -= 1
                break
    return c


def test_coin():
    for (c1, c5, c10, c50, c100, c500, s, result) in [
        (3, 2, 1, 3, 0, 2, 620, 6),
    ]:
        assert coin(c1, c5, c10, c50, c100, c500, s) is result
