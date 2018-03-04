#!/usr/local/bin/python3

##Ants##

def ants1(l: int, n: int, x: list):
    def _cal_max(e: int):
        if l / 2 > e:
            return l - e
        return e
    def _cal_min(e: int):
        if l / 2 > e:
            return e
        return l - e
    result = []
    mini = 0
    for e in x:
        if _cal_min(e) > mini:
            mini = _cal_min(e)
    result += [mini]

    maxi = 0
    for e in x:
        if _cal_max(e) > maxi:
            maxi = _cal_max(e)
    result += [maxi]
    return result

def test_ants():
    for (n, m, k, result) in [
        (10, 3, [2, 6, 7], [4, 8])
    ]:
        assert result == ants1(n, m, k)


def ants2(l: int, n: int, x: list):
    return [
        max(min(e, l - e) for e in x),
        max(max(e, l - e) for e in x),
    ]

def test_ants2():
    for (n, m, k, result) in [
        (10, 3, [2, 6, 7], [4, 8])
    ]:
        assert result == ants2(n, m, k)
