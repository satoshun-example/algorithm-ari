#!/usr/local/bin/python3

## 深さ優先探索
def depth(n, a, k):
    if k == 0:
        return True
    if len(a) == 0:
        return False
    v = a[0]
    return depth(n - 1, a[1::], k - v) or depth(n - 1, a[1::], k)

def test_depth():
    for (n, a, k, result) in [
        (4, [1, 2, 4, 7], 13, True),
        (4, [1, 2, 4, 7], 15, False)
    ]:
        assert depth(n, a, k) is result
