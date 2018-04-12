#!/usr/local/bin/python3


def lower_bound1(n, a, k):
    for i, e in enumerate(a):
        if e >= k:
            return i
    return -1


def test_lower_bound1():
    for (n, a, k, result) in [
        (5, (2, 3, 3, 5, 6), 3, 1),
    ]:
        assert lower_bound1(n, a, k) == result


def lower_bound2(n, a, k):
    pivot = n // 2
    c = None
    while True:
        if c == pivot:
            break
        e = a[pivot]
        if e >= k:
            c = pivot
            pivot = pivot // 2
            continue
        pivot += 1
    return c


def test_lower_bound2():
    for (n, a, k, result) in [
        (5, (2, 3, 3, 5, 6), 3, 1),
    ]:
        assert lower_bound2(n, a, k) == result


def lower_bound3(n, a, k):
    left = 0
    right = n - 1
    pivot = (left + right) // 2
    c = None
    while True:
        e = a[pivot]
        if e >= k:
            c = pivot
            right = c
            pivot = (left + right) // 2
            continue
        left = pivot
        n = (left + right) // 2
        if pivot == n:
            break
        pivot = n
    return c


def test_lower_bound3():
    for (n, a, k, result) in [
        (5, (2, 3, 3, 5, 6), 3, 1),
    ]:
        assert lower_bound3(n, a, k) == result
