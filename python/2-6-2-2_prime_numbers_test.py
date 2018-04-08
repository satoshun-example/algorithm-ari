#!/usr/local/bin/python3


# 素数の個数
# エラトステネス
def prime_numbers(n):
    q = [False if i in (0, 1) else True for i in range(n + 1)]
    c = 0
    for i, v in enumerate(q):
        if v:
            c += 1
            for ii in range(i * 2, n + 1, i):
                q[ii] = False
    return c


def test_prime_numbers():
    for (n, result) in [
        (11, 5),
        (1000000, 78498),
    ]:
        assert prime_numbers(n) == result
