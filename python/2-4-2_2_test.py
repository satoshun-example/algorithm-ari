#!/usr/local/bin/python3


# トラックで距離L
def priority_queue2(n, l, p, a, b):
    q = []
    c = 0
    while True:
        if l <= p:
            break
        s = 0
        for e in a:
            if e < p:
                break
            s += 1
        for _ in range(s):
            a.pop(0)
            q += [b.pop(0)]
        if len(q) == 0:
            return -1
        c += 1
        q = sorted(q, reverse=True)
        p += q.pop(0)
    return c


def test_priority_queue2():
    for (n, l, p, a, b, result) in [
        (4, 25, 10, [10, 14, 20, 21], [10, 5, 2, 4], 2),
    ]:
        assert priority_queue2(n, l, p, a, b) == result
