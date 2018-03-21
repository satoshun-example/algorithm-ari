#!/usr/local/bin/python3


## 最長共通部分列問題(Longest Common Subsequence)
def common_text(n, m, s, t):
    return _common_text(n - 1, m - 1, s, t, 0)


def _common_text(nc, mc, s, t, count):
    if nc == -1:
        return count
    ch = s[nc]
    if ch in t[0:mc + 1]:
        for i in range(mc, -1, -1):
            if t[i] == ch:
                break
        return _common_text(nc - 1, i, s, t, count + 1)
    else:
        return _common_text(nc - 1, mc, s, t, count)


def test_common_text():
    for (n, m, s, t, result) in [
        (4, 4, 'abcd', 'becd', 3),
    ]:
        assert common_text(n, m, s, t) == result
