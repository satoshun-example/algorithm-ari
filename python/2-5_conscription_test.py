#!/usr/local/bin/python3


def conscription(n, m, r, x):
    xxx = []
    for xx in x:
        xxx += [(xx[0], xx[1] + n, xx[2])]

    def calculate(vv):
        added = []
        v = 0
        for s in vv:
            sss = 0
            for xx in xxx:
                if xx[0] in added and xx[1] == s:
                    if sss < xx[2]:
                        sss = xx[2]
                if xx[1] in added and xx[0] == s:
                    if sss < xx[2]:
                        sss = xx[2]
            added += [s]
            v += 10000 - sss
        return v

    v = [i for i in range(n + m)]
    for i in range(n + m):
        for j in range(n + m):
            before = calculate(v)
            v[i], v[j] = v[j], v[i]
            after = calculate(v)
            if before > after:
                pass
            else:
                v[i], v[j] = v[j], v[i]
    return calculate(v)


def test_conscription():
    assert conscription(
        5,
        5,
        8,
        (
            (4, 3, 6831),
            (1, 3, 4583),
            (0, 0, 6592),
            (0, 1, 3063),
            (3, 3, 4975),
            (1, 3, 2049),
            (4, 2, 2104),
            (2, 2, 781),
        ),
    ) == 71071
