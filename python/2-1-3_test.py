#!/usr/local/bin/python3

## Lake Counting
def lake_counting(n, m, l):
    c = 0
    for y in range(m):
        for x in range(n):
            if l[x][y] == 'W':
                fill(l, x, y, n, m)
                c += 1
    return c

def fill(l, x, y, n, m):
    l[x][y] = '.'
    for i in range(-1, 2):
        for j in range(-1, 2):
            xx = x + i
            yy = y + j
            if xx >= n or yy >= m:
                continue
            if xx < 0 or yy < 0:
                continue
            if l[xx][yy] == 'W':
                fill(l, xx, yy, n, m)


def test_lake_counting():
    for (n, a, lake, result) in [
        (10, 12,
            [
                ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
                ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
                ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
                ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
                ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
                ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
                ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
                ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'],
            ],
        3),
    ]:
        assert lake_counting(n, a, lake) is result
