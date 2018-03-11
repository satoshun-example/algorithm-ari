#!/usr/local/bin/python3


## section/区間
def best_cow_line(n, s):
    r = ''
    i = 0
    j = n - 1
    while True:
        if i == j:
            r += s[i]
            i += 1
            break
        if s[i] < s[j]:
            r += s[i]
            i += 1
            continue
        if s[i] > s[j]:
            r += s[j]
            j -= 1
            continue
        ii = i
        jj = j
        while True:
            ii += 1
            jj -= 1
            if ii == jj:
                r += s[i]
                i += 1
                break
            if s[ii] < s[jj]:
                r += s[i]
                i += 1
                break
            if s[ii] > s[jj]:
                r += s[j]
                j -= 1
                break
    return r


def test_best_cow_line():
    for (n, s, result) in [
        (6, 'ACDBCB', 'ABCBCD'),
    ]:
        assert best_cow_line(n, s) == result
