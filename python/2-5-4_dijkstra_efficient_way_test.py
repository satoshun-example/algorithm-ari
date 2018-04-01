#!/usr/local/bin/python3
from queue import PriorityQueue

MAX = 10000


# 単一始点
# ダイクストラ
# プライオリティqueueを使う
def dijkstra(edges, s, g, c):
    queue = list()
    d = [0 if i == s else MAX for i in range(c)]

    def fill(ni):
        for c in edges:
            if c[0] == ni:
                if d[c[1]] > d[c[0]] + c[2]:
                    d[c[1]] = d[c[0]] + c[2]
                    queue.append((d[c[1]], c[1]))
            if c[1] == ni:
                if d[c[0]] > d[c[1]] + c[2]:
                    d[c[0]] = d[c[1]] + c[2]
                    queue.append((d[c[0]], c[0]))

    for i in range(c):
        if i == s:
            queue.append((0, i))
        else:
            queue.append((MAX, i))
    queue = sorted(queue)
    while queue:
        v = queue.pop(0)
        if v[0] == MAX:
            break
        fill(v[1])
        queue = sorted(queue)
    return d[g]


def test_dijkstra():
    for (n, s, g, c, result) in [
        ([
            (0, 1, 2),
            (0, 2, 5),
            (1, 2, 4),
            (1, 3, 6),
            (1, 4, 10),
            (2, 3, 2),
            (3, 5, 1),
            (4, 5, 3),
            (4, 6, 5),
            (5, 6, 9),
        ], 0, 6, 7, 16),
    ]:
        assert dijkstra(n, s, g, c) is result
