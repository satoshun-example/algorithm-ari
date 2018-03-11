#!/usr/local/bin/python3


## section/区間 解答
def section2(n, s, t):
    count = 0
    current = 0
    while True:
        next_pos = None
        for i in range(n):
            if s[i] >= current:
                if next_pos is None or next_pos > t[i]:
                    next_pos = t[i]
        if next_pos is None:
            break
        current = next_pos
        count += 1
    return count


def test_section2():
    for (n, s, t, result) in [
        (5, [1, 2, 4, 6, 8], [3, 5, 7, 9, 10], 3),
    ]:
        assert section2(n, s, t) is result


## section/区間
def section(n, s, t):
    costs = [c - st for (st, c) in zip(s, t)]
    return _section(s, costs, 0)


def _section(s, t, total):
    m = total
    for i in range(len(s)):
        start = s[i]
        cost = t[i]
        # remove over start time
        over_time = i + 1
        for j in range(i + 1, len(s)):
            if s[j] < start + cost:
                over_time = j
        over_time += 1
        m = max(_section(s[over_time::], t[over_time::], total + 1), m)
    return m


def test_section():
    for (n, s, t, result) in [
        (5, [1, 2, 4, 6, 8], [3, 5, 7, 9, 10], 3),
    ]:
        assert section(n, s, t) is result
