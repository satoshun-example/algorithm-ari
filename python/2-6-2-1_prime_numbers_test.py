#!/usr/local/bin/python3


# 素数の個数
# エラトステネス
def prime_numbers(n):
    q = [i for i in range(2, n + 1)]
    i = 0
    while len(q) > i:
        v = q[i]
        qq = q[:i + 1]
        for j in range(i + 1, len(q)):
            if q[j] % v != 0:
                qq += [q[j]]
        q = qq
        i += 1
    return len(q)


def test_prime_numbers():
    for (n, result) in [
        (11, 5),
            # (1000000, 78498), todo
    ]:
        assert prime_numbers(n) is result
