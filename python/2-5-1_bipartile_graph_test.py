#!/usr/local/bin/python3


# 2部グラフ判定
# DFS
def bipartile_graph(n, g):
    colors = [-1 for _ in range(n)]
    for i in range(n):
        edges = g[i]
        edges_color = [colors[edge] for edge in edges]

        if 1 not in edges_color:
            colors[i] = 1
        elif 2 not in edges_color:
            colors[i] = 2
        else:
            return False
    return True


def test_bipartile_graph():
    for (n, g, result) in [
        (3, {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1],
        }, False),
        (4, {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2],
        }, True),
    ]:
        assert bipartile_graph(n, g) is result
