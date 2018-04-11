#!/usr/local/bin/python3


# しゃくとり法
def subsequence(n, s, a):
    m = 10000
    left = 0
    right = 0
    while True:
        if left != right:
            if sum(a[left + 1:right]) >= s:
                left += 1
                if m > right - left:
                    m = right - left
                continue
        right += 1
        if right == s:
            break
    return m


def test_subsequence():
    for (n, s, a, result) in [
        (10, 15, (5, 1, 3, 5, 10, 7, 4, 9, 2, 8), 2),
        (5, 11, (1, 2, 3, 4, 5), 3),
    ]:
        assert subsequence(n, s, a) == result
