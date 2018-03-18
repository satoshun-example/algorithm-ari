#!/usr/local/bin/python3


## fence repair
## 2分木を作る。葉の位置が深いほどコストは低い
def fence_repair2(n, l):
    cut = 0
    while len(l) >= 2:
        l = sorted(l)
        leaf = l[0] + l[1]
        cut += leaf
        l[1] = leaf
        l = l[1:]
    return cut


def test_fence_repair2():
    for (n, l, result) in [
        (3, [8, 5, 8], 34),
    ]:
        assert fence_repair2(n, l) == result
