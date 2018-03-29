#!/usr/local/bin/python3

MAX = 10000


# 単一始点
# ベルマンフォード
# d[i]: 始点sから頂点iへの最短距離
# d[i] = min(d[j] + jからiへのedgeコスト) | e=(j,i)
def shortest_way(edges, s, g, c):
    d = [0 if i == s else MAX for i in range(c)]
    while True:
        updated = False
        for edge in edges:
            if d[edge[1]] > d[edge[0]] + edge[2]:
                d[edge[1]] = d[edge[0]] + edge[2]
                updated = True
                continue
            if d[edge[0]] > d[edge[1]] + edge[2]:
                d[edge[0]] = d[edge[1]] + edge[2]
                updated = True
                continue
        if not updated:
            break
    return d[g]


def test_shortest_way():
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
        assert shortest_way(n, s, g, c) is result
