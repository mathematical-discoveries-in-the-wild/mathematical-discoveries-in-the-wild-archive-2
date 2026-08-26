#!/usr/bin/env python3
"""Independent finite-dimensional checks for the projection formulas.

The symbolic checks use ``fractions.Fraction``.  The optimization checks use
linear programming and do not impose the closed-form candidate projection.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import random

import numpy as np
from scipy.optimize import linprog


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def max_row_sum(a):
    return max(sum(abs(x) for x in row) for row in a)


def cycle_formula(weights):
    weights = [Fraction(x) for x in weights]
    perimeter = sum(weights)
    assert 2 * max(weights) <= perimeter
    for k, a in enumerate(weights):
        if 2 * a == perimeter:
            t = [Fraction(0) for _ in weights]
            t[k] = Fraction(1)
            return Fraction(1), t
    capacities = [a / (perimeter - 2 * a) for a in weights]
    capacity_sum = sum(capacities)
    t = [c / capacity_sum for c in capacities]
    return 1 + 1 / capacity_sum, t


def cycle_projection(weights):
    weights = [Fraction(x) for x in weights]
    lam, t = cycle_formula(weights)
    u = [t_i / a_i for t_i, a_i in zip(t, weights)]
    n = len(weights)
    p = [
        [Fraction(i == j) - u[i] * weights[j] for j in range(n)]
        for i in range(n)
    ]
    return lam, p


def solve_cycle_lp(weights):
    """Minimize ||I-u phi||_infinity subject to phi(u)=1."""
    a = np.asarray(weights, dtype=float)
    n = len(a)
    u0 = 0
    z0 = n
    ell = n + n * n
    size = ell + 1
    c = np.zeros(size)
    c[ell] = 1.0
    aub, bub = [], []
    for i in range(n):
        for j in range(n):
            z = z0 + i * n + j
            delta = float(i == j)
            row = np.zeros(size)
            row[u0 + i] = -a[j]
            row[z] = -1.0
            aub.append(row)
            bub.append(-delta)
            row = np.zeros(size)
            row[u0 + i] = a[j]
            row[z] = -1.0
            aub.append(row)
            bub.append(delta)
        row = np.zeros(size)
        row[z0 + i * n : z0 + (i + 1) * n] = 1.0
        row[ell] = -1.0
        aub.append(row)
        bub.append(0.0)
    aeq = np.zeros((1, size))
    aeq[0, :n] = a
    bounds = [(None, None)] * n + [(0.0, None)] * (n * n + 1)
    ans = linprog(
        c,
        A_ub=np.asarray(aub),
        b_ub=np.asarray(bub),
        A_eq=aeq,
        b_eq=np.asarray([1.0]),
        bounds=bounds,
        method="highs",
    )
    assert ans.success, ans.message
    return ans.fun


def gradient_matrix_complete(n):
    """Gradient matrix for K_n, with x_{n-1}=0 and edge i<j equal x_j-x_i."""
    edges = list(combinations(range(n), 2))
    b = np.zeros((len(edges), n - 1))
    for e, (i, j) in enumerate(edges):
        if i < n - 1:
            b[e, i] -= 1.0
        if j < n - 1:
            b[e, j] += 1.0
    return edges, b


def canonical_complete_projection(n):
    edges, _ = gradient_matrix_complete(n)
    m = len(edges)
    p = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for out, (i, j) in enumerate(edges):
        # (Pf)_{ij}=(d_i-d_j)/n with f_{pq} stored for p<q.
        for inp, (q, r) in enumerate(edges):
            def coeff(vertex):
                if vertex == q:
                    return Fraction(1)
                if vertex == r:
                    return Fraction(-1)
                return Fraction(0)
            p[out][inp] = (coeff(i) - coeff(j)) / n
    return p


def additive_matrix_bipartite(p, q):
    """A basis for matrices x_ij=y_j-x_i, fixing x_{p-1}=0."""
    b = np.zeros((p * q, p - 1 + q))
    for i in range(p):
        for j in range(q):
            edge = i * q + j
            if i < p - 1:
                b[edge, i] = -1.0
            b[edge, p - 1 + j] = 1.0
    return b


def canonical_bipartite_projection(p, q):
    """Two-way additive projection: row mean + column mean - grand mean."""
    m = p * q
    out = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for i in range(p):
        for j in range(q):
            target = i * q + j
            for k in range(p):
                for ell_col in range(q):
                    source = k * q + ell_col
                    out[target][source] = (
                        Fraction(i == k, q)
                        + Fraction(j == ell_col, p)
                        - Fraction(1, p * q)
                    )
    return out


def solve_range_projection_lp(b):
    """Minimize ||B R||_infinity over left inverses R B=I."""
    m, d = b.shape
    r0 = 0
    z0 = d * m
    ell = z0 + m * m
    size = ell + 1
    c = np.zeros(size)
    c[ell] = 1.0

    def ridx(k, j):
        return r0 + k * m + j

    def zidx(i, j):
        return z0 + i * m + j

    aub, bub = [], []
    for i in range(m):
        for j in range(m):
            # p_ij = sum_k b_ik r_kj; impose |p_ij| <= z_ij.
            row = np.zeros(size)
            for k in range(d):
                row[ridx(k, j)] = b[i, k]
            row[zidx(i, j)] = -1.0
            aub.append(row)
            bub.append(0.0)
            aub.append(-row.copy())
            # Correct the sign of z after negating: -p-z <= 0.
            aub[-1][zidx(i, j)] = -1.0
            bub.append(0.0)
        row = np.zeros(size)
        row[z0 + i * m : z0 + (i + 1) * m] = 1.0
        row[ell] = -1.0
        aub.append(row)
        bub.append(0.0)

    aeq, beq = [], []
    for k in range(d):
        for ell_col in range(d):
            row = np.zeros(size)
            for j in range(m):
                row[ridx(k, j)] = b[j, ell_col]
            aeq.append(row)
            beq.append(float(k == ell_col))

    bounds = [(None, None)] * (d * m) + [(0.0, None)] * (m * m + 1)
    ans = linprog(
        c,
        A_ub=np.asarray(aub),
        b_ub=np.asarray(bub),
        A_eq=np.asarray(aeq),
        b_eq=np.asarray(beq),
        bounds=bounds,
        method="highs",
    )
    assert ans.success, ans.message
    return ans.fun


def block_diagonal(blocks):
    total = sum(len(b) for b in blocks)
    out = [[Fraction(0) for _ in range(total)] for _ in range(total)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = value
        offset += len(block)
    return out


def main():
    exact_assertions = 0
    lp_assertions = 0

    # Deterministic cycle cases, including the geodesic equality endpoint.
    cases = [
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 2],
        [2, 3, 4, 5],
        [1, 2, 3],
        [3, 3, 3, 3, 3],
    ]
    rng = random.Random(230909313)
    while len(cases) < 36:
        w = [rng.randint(1, 9) for _ in range(rng.randint(3, 8))]
        if 2 * max(w) <= sum(w):
            cases.append(w)

    for weights in cases:
        lam, p = cycle_projection(weights)
        n = len(weights)
        ident = [[Fraction(i == j) for j in range(n)] for i in range(n)]
        assert matmul(p, p) == p
        exact_assertions += 1
        assert [sum(Fraction(weights[i]) * p[i][j] for i in range(n)) for j in range(n)] == [Fraction(0)] * n
        exact_assertions += 1
        assert max_row_sum(p) == lam
        exact_assertions += 1
        # P is the identity on ker(phi): equivalently I-P has all rows
        # proportional to phi, already encoded by construction.
        assert all(
            (ident[i][j] - p[i][j]) * Fraction(weights[0])
            == (ident[i][0] - p[i][0]) * Fraction(weights[j])
            for i in range(n)
            for j in range(n)
        )
        exact_assertions += 1
        lp_value = solve_cycle_lp(weights)
        assert abs(lp_value - float(lam)) < 2e-8, (weights, lp_value, lam)
        lp_assertions += 1

    # The unweighted specialization is 2-2/r.
    for r in range(3, 13):
        lam, _ = cycle_projection([1] * r)
        assert lam == Fraction(2 * r - 2, r)
        exact_assertions += 1

    # Complete graphs: exact idempotence/norm and independent range LP.
    complete_blocks = []
    for n in range(2, 9):
        p = canonical_complete_projection(n)
        assert matmul(p, p) == p
        exact_assertions += 1
        assert max_row_sum(p) == Fraction(2 * n - 2, n)
        exact_assertions += 1
        complete_blocks.append(p)
        if n <= 5:
            _, b = gradient_matrix_complete(n)
            lp_value = solve_range_projection_lp(b)
            assert abs(lp_value - (2.0 - 2.0 / n)) < 2e-8, (n, lp_value)
            lp_assertions += 1

    # Complete bipartite graphs: exact ANOVA projection and independent LP.
    bipartite_blocks = []
    bipartite_cases = [(1, 5), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 5)]
    for p_size, q_size in bipartite_cases:
        pmat = canonical_bipartite_projection(p_size, q_size)
        expected = (
            Fraction(3)
            - Fraction(2, p_size)
            - Fraction(2, q_size)
            + Fraction(2, p_size * q_size)
        )
        assert matmul(pmat, pmat) == pmat
        exact_assertions += 1
        assert max_row_sum(pmat) == expected
        exact_assertions += 1
        bipartite_blocks.append(pmat)
        if p_size * q_size <= 12:
            b = additive_matrix_bipartite(p_size, q_size)
            lp_value = solve_range_projection_lp(b)
            assert abs(lp_value - float(expected)) < 2e-8, ((p_size, q_size), lp_value)
            lp_assertions += 1

    # Block-diagonal gluing has norm equal to the maximum block norm.
    cycle_blocks = [cycle_projection(w)[1] for w in ([1, 1, 1], [1, 2, 2], [2, 3, 4, 5])]
    for blocks in [
        cycle_blocks,
        complete_blocks[1:4],
        bipartite_blocks[1:4],
        cycle_blocks + complete_blocks[2:4] + bipartite_blocks[2:4],
    ]:
        glued = block_diagonal(blocks)
        assert max_row_sum(glued) == max(max_row_sum(block) for block in blocks)
        assert matmul(glued, glued) == glued
        exact_assertions += 2

    print("verification passed")
    print(f"exact rational assertions: {exact_assertions}")
    print(f"independent LP optimum assertions: {lp_assertions}")
    print(f"weighted-cycle instances: {len(cases)}")
    print("complete-graph exact instances: 7 (n=2,...,8)")
    print("complete-graph independent LP instances: 4 (n=2,...,5)")
    print(f"complete-bipartite exact instances: {len(bipartite_cases)}")
    print("complete-bipartite independent LP instances: 6")


if __name__ == "__main__":
    main()
