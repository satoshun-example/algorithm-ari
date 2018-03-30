#!/usr/local/bin/python3

MAX = 10000


# 単一始点
# ダイクストラ
# 最も距離が短い頂点の隣接頂点を更新していく
def dijkstra(edges, s, g, c):
    d = [0 if i == s else MAX for i in range(c)]
    dd = [False for _ in range(c)]

    def find_next_edge():
        ii = -1
        ddd = MAX
        for (i, f) in zip(range(c), dd):
            if f:
                continue
            if ddd > d[i]:
                ii = i
                ddd = d[i]
        return ii

    def update_edge(edge):
        for ss in edges:
            if ss[0] == edge:
                c = ss[2] + d[edge]
                if c < d[ss[1]]:
                    d[ss[1]] = c
            if ss[1] == edge:
                c = ss[2] + d[edge]
                if c < d[ss[0]]:
                    d[ss[0]] = c
        dd[edge] = True

    while True:
        if False not in dd:
            break
        edge = find_next_edge()
        update_edge(edge)
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
