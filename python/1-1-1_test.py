#!/usr/local/bin/python3

##くじ引き##
# O(n**2 * log(n))
def kujibiki3(n: int, m: int, k: list) -> bool:
    size = len(k)
    k = _sort(k)
    kk = _sort([k[x1] + k[x2] for x1 in range(size) for x2 in range(size)])
    for x1 in range(size):
        for x2 in range(size):
            if _binary_search(kk, m - k[x1] - k[x2]):
                return True
    return False

def test_kujibiki3():
    for (n, m, k, result) in [
        (3, 10, [1, 3, 5], True),
        (3, 9, [1, 3, 5], False),
        (4, 9, [1, 3, 5, 6], True),
    ]:
        assert result == kujibiki3(n, m, k)

# O(n**3 * log(n))
def kujibiki2(n: int, m: int, k: list) -> bool:
    k = _sort(k)
    size = len(k)
    for x1 in range(size):
        for x2 in range(size):
            for x3 in range(size):
                if (_binary_search(k, m - k[x1] - k[x2] - k[x3])):
                    return True
    return False

# include bug
def _binary_search(k: list, x: int) -> bool:
    s = int(len(k) / 2)
    d = s
    while True:
        if k[s] == x:
            return True
        if s == 0 or s == len(k) - 1 or d == 0:
            break
        d = int(d / 2)
        if k[s] > x:
            s -= d
        else:
            s += d
    return False

def _sort(k: list) -> list:
    return sorted(k)

def test_kujibiki2():
    for (n, m, k, result) in [
        (3, 10, [1, 3, 5], True),
        (3, 9, [1, 3, 5], False),
        (4, 9, [1, 3, 5, 6], True),
    ]:
        assert result == kujibiki2(n, m, k)


# O(n**4)
def kujibiki1(n: int, m: int, k: list):
    size = len(k)
    for x1 in range(size):
        for x2 in range(size):
            for x3 in range(size):
                for x4 in range(size):
                    if k[x1] + k[x2] + k[x3] + k[x4] == m:
                        return True
    return False

def test_kujibiki1():
    for (n, m, k, result) in [
        (3, 10, [1, 3, 5], True),
        (3, 9, [1, 3, 5], False),
        (4, 9, [1, 3, 5, 6], True),
    ]:
        assert result == kujibiki1(n, m, k)
