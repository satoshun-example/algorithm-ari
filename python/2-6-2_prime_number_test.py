#!/usr/local/bin/python3


# 素数
def prime_number(n):
    q = [i for i in range(2, n)]
    while q:
        v = q.pop(0)
        if n % v == 0:
            return False
        qq = []
        for vv in q:
            if vv % v != 0:
                qq += [vv]
        q = qq
    return True


def test_prime_number():
    for (n, result) in [
        (53, True),
        (55, False),
        (57, False),
        (59, True),
    ]:
        assert prime_number(n) is result
