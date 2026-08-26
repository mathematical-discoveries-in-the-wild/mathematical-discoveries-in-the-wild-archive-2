#!/usr/bin/env python3
"""Finite sanity checks for the forest-support operator-norm packet.

This is not part of the proof.  It checks the rooted edge decomposition and
the resulting spectral/endpoint inequalities on reproducible random examples.
"""

from __future__ import annotations

import numpy as np


def random_bipartite_forest(rng: np.random.Generator, m: int, n: int, density: float):
    parent = list(range(m + n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    edges = []
    candidates = [(i, j) for i in range(m) for j in range(n)]
    rng.shuffle(candidates)
    for i, j in candidates:
        if rng.random() > density:
            continue
        u, v = i, m + j
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        parent[ru] = rv
        edges.append((i, j))
    return edges


def rooted_split(m: int, n: int, edges: list[tuple[int, int]]):
    adjacency = [[] for _ in range(m + n)]
    for i, j in edges:
        u, v = i, m + j
        adjacency[u].append(v)
        adjacency[v].append(u)

    row_child, col_child = [], []
    seen = [False] * (m + n)
    for root in range(m + n):
        if seen[root] or not adjacency[root]:
            continue
        seen[root] = True
        stack = [(root, -1)]
        while stack:
            u, par = stack.pop()
            for v in adjacency[u]:
                if v == par:
                    continue
                assert not seen[v], "the supplied support is not a forest"
                seen[v] = True
                edge = (v, u) if v < m else (u, v)
                i, w = edge
                j = w - m
                (row_child if v < m else col_child).append((i, j))
                stack.append((v, u))
    assert sorted(row_child + col_child) == sorted(edges)
    assert max(np.bincount([i for i, _ in row_child], minlength=m), default=0) <= 1
    assert max(np.bincount([j for _, j in col_child], minlength=n), default=0) <= 1
    return row_child, col_child


def masked_matrix(a: np.ndarray, edges: list[tuple[int, int]]) -> np.ndarray:
    b = np.zeros_like(a)
    for i, j in edges:
        b[i, j] = a[i, j]
    return b


def main() -> None:
    rng = np.random.default_rng(250202186)
    trials = 500
    sign_trials = 20
    checked_signings = 0

    for _ in range(trials):
        m = int(rng.integers(1, 9))
        n = int(rng.integers(1, 9))
        edges = random_bipartite_forest(rng, m, n, density=0.65)
        row_child, col_child = rooted_split(m, n, edges)
        a = masked_matrix(rng.normal(size=(m, n)), edges)
        ar = masked_matrix(a, row_child)
        ac = masked_matrix(a, col_child)

        assert np.allclose(a, ar + ac)
        row2 = np.max(np.linalg.norm(a, axis=1), initial=0.0)
        col2 = np.max(np.linalg.norm(a, axis=0), initial=0.0)
        spectral = np.linalg.svd(a, compute_uv=False)[0] if a.size else 0.0
        assert spectral <= row2 + col2 + 1e-11

        # The two rooted pieces have the exact degree-one endpoint formulas.
        assert np.isclose(
            np.linalg.svd(ar, compute_uv=False)[0] if ar.size else 0.0,
            np.max(np.linalg.norm(ar, axis=0), initial=0.0),
        )
        assert np.isclose(
            np.linalg.svd(ac, compute_uv=False)[0] if ac.size else 0.0,
            np.max(np.linalg.norm(ac, axis=1), initial=0.0),
        )

        for _ in range(sign_trials):
            signs = masked_matrix(rng.choice([-1.0, 1.0], size=(m, n)), edges)
            signed = a * signs
            signed_spectral = np.linalg.svd(signed, compute_uv=False)[0]
            assert max(row2, col2) <= signed_spectral + 1e-11
            assert signed_spectral <= row2 + col2 + 1e-11
            checked_signings += 1

    print(
        f"PASS: {trials} random forest matrices, {checked_signings} Bernoulli "
        "signings; rooted decompositions and spectral/endpoint bounds verified."
    )


if __name__ == "__main__":
    main()
