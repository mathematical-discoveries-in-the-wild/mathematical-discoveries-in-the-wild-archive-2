"""Small finite sanity check for the endpoint min-cut scaling.

This is not part of the proof.  It builds the retained level cells, uses
face or face-plus-corner adjacency, and computes representative annular cuts.
"""

from __future__ import annotations

import networkx as nx


def cells(n: int) -> list[tuple[int, int]]:
    kept: list[tuple[int, int]] = []
    for x in range(3**n):
        for y in range(3**n):
            if all(
                ((x // 3**j) % 3, (y // 3**j) % 3) != (1, 1)
                for j in range(n)
            ):
                kept.append((x, y))
    return kept


def graph(n: int, corners: bool) -> nx.Graph:
    vertices = set(cells(n))
    result = nx.Graph()
    result.add_nodes_from(vertices)
    steps = [(1, 0), (0, 1)]
    if corners:
        steps += [(1, 1), (1, -1)]
    for x, y in vertices:
        for dx, dy in steps:
            other = (x + dx, y + dy)
            if other in vertices:
                result.add_edge((x, y), other)
    return result


def annular_cut(m: int, n: int, coarse_cell: tuple[int, int], corners: bool) -> int:
    coarse = graph(m, corners)
    near = set(nx.single_source_shortest_path_length(coarse, coarse_cell, cutoff=2))
    fine = graph(m + n, corners)
    scale = 3**n
    inner = {v for v in fine if (v[0] // scale, v[1] // scale) == coarse_cell}
    outer = {v for v in fine if (v[0] // scale, v[1] // scale) not in near}
    flow = nx.DiGraph()
    for u, v in fine.edges:
        flow.add_edge(u, v, capacity=1)
        flow.add_edge(v, u, capacity=1)
    source, sink, infinity = ("source",), ("sink",), 10**9
    for v in inner:
        flow.add_edge(source, v, capacity=infinity)
    for v in outer:
        flow.add_edge(v, sink, capacity=infinity)
    value, _ = nx.minimum_cut(flow, source, sink)
    return int(value)


if __name__ == "__main__":
    # A representative cell for which the annulus is nonempty.
    w = (0, 2)
    for corners in (False, True):
        values = [annular_cut(2, n, w, corners) for n in (1, 2)]
        print({"corner_adjacency": corners, "cuts_n_1_2": values})
        assert values[1] == 2 * values[0]
