#!/usr/local/bin/python3


## fence repair(間違っている)
def fence_repair(n, l):
    cost = 0
    l = sorted(l, reverse=True)
    for i, e in enumerate(l[:-1]):
        cost += e
        cost += sum(l[i + 1:])
    return cost


def test_fence_repair():
    for (n, l, result) in [
        (3, [8, 5, 8], 34),
    ]:
        assert fence_repair(n, l) == result
