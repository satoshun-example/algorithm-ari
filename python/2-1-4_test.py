#!/usr/local/bin/python3

## 迷路
def puzzles(n, m, l):
    x, y = _find_start(m, m, l)
    return _puzzles(x, y, l)

def _find_start(n, m, l):
    for y in range(n):
        for x in range(m):
            if l[x][y] == 'S':
                return x, y

def _puzzles(sx, sy, l):
    mx = len(l)
    my = len(l[0])
    c = 0
    n = [(sx, sy)]
    while True:
        c += 1
        nn = n.copy()
        n = []
        for (x, y) in nn:
            for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx = x + xd
                yy = y + yd
                if xx < 0 or xx >= mx:
                    continue
                if yy < 0 or yy >= my:
                    continue
                if l[xx][yy] == 'G':
                    return c
                if l[xx][yy] == '.':
                    l[xx][yy] = '#'
                    n.append((xx, yy))
    return c

def test_puzzle():
    for (n, m, puzzle, result) in [
        (10, 10,
            [
                ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
                ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
                ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
                ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
                ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
                ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
            ],
        22),
    ]:
        assert puzzles(n, m, puzzle) is result


## 迷路 with queue
def puzzles2(n, m, l):
    sx, sy = _find_start(m, m, l)
    l[sx][sy] = 0
    mx = len(l)
    my = len(l[0])
    q = [(sx, sy)]
    for (x, y) in q:
        for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x + xd
            yy = y + yd
            if xx < 0 or xx >= mx:
                continue
            if yy < 0 or yy >= my:
                continue
            if l[xx][yy] == 'G':
                return l[x][y] + 1
            if l[xx][yy] == '.':
                l[xx][yy] = l[x][y] + 1
                q.append((xx, yy))
    return False

def test_puzzle2():
    for (n, m, puzzle, result) in [
        (10, 10,
            [
                ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
                ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
                ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
                ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
                ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
                ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
                ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
            ],
        22),
    ]:
        assert puzzles2(n, m, puzzle) is result
