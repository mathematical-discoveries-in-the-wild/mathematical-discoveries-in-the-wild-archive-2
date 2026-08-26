"""Numerical checks for the arXiv:1203.6812 counterexample and resolvent formula.

The proof in the packet is analytic.  This script exhausts all labelled simple
graphs on two, three, and four vertices to catch cofactor-sign or indexing
errors in the finite incidence-minor formula.
"""

from __future__ import annotations

import itertools
import numpy as np


def incidence(n: int, edges: list[tuple[int, int]]) -> np.ndarray:
    matrix = np.zeros((n, len(edges)))
    for column, (u, v) in enumerate(edges):
        matrix[u, column] = 1.0
        matrix[v, column] = 1.0
    return matrix


def subset_formula(
    n: int,
    edges: list[tuple[int, int]],
    alpha: float,
    ell: float,
    t: float,
) -> tuple[float, np.ndarray]:
    b_matrix = incidence(n, edges)
    columns = [np.eye(n)[:, i] for i in range(n)]
    columns += [np.ones(n)]
    columns += [b_matrix[:, k] for k in range(len(edges))]
    weights = [alpha] * n + [ell] + [t] * len(edges)

    denominator = 0.0
    for subset in itertools.combinations(range(len(columns)), n):
        a_sub = np.column_stack([columns[k] for k in subset])
        weight = np.prod([weights[k] for k in subset])
        denominator += weight * np.linalg.det(a_sub) ** 2

    numerator = np.zeros((n, n))
    for subset in itertools.combinations(range(len(columns)), n - 1):
        a_sub = np.column_stack([columns[k] for k in subset])
        weight = np.prod([weights[k] for k in subset])
        deltas = np.array(
            [np.linalg.det(np.column_stack([np.eye(n)[:, i], a_sub])) for i in range(n)]
        )
        numerator += weight * np.outer(deltas, deltas)

    return denominator, numerator


# Exact displayed counterexample to the literal Conjecture 8.1.
s_matrix = np.eye(3) + np.ones((3, 3))
j_matrix = 1.5 * np.eye(3) + 0.5 * np.ones((3, 3))
assert np.all(j_matrix > 0) and np.all(j_matrix <= s_matrix)
assert np.all(np.diag(j_matrix) >= np.sum(j_matrix, axis=1) - np.diag(j_matrix))
np.testing.assert_allclose(np.linalg.inv(s_matrix), np.eye(3) - 0.25 * np.ones((3, 3)))
np.testing.assert_allclose(
    np.linalg.inv(j_matrix), (2.0 / 3.0) * np.eye(3) - (1.0 / 9.0) * np.ones((3, 3))
)
np.testing.assert_allclose(np.linalg.norm(np.linalg.inv(s_matrix), np.inf), 5.0 / 4.0)
np.testing.assert_allclose(np.linalg.norm(np.linalg.inv(j_matrix), np.inf), 7.0 / 9.0)


graph_count = 0
comparison_count = 0
for n_vertices in range(2, 5):
    possible_edges = list(itertools.combinations(range(n_vertices), 2))
    for mask in range(1 << len(possible_edges)):
        graph_edges = [
            edge for bit, edge in enumerate(possible_edges) if mask & (1 << bit)
        ]
        b_matrix = incidence(n_vertices, graph_edges)
        p_matrix = b_matrix @ b_matrix.T
        graph_count += 1
        for t_value in (0.13, 1.2, 3.7):
            alpha_value, ell_value = 2.3, 0.7
            matrix = (
                alpha_value * np.eye(n_vertices)
                + ell_value * np.ones((n_vertices, n_vertices))
                + t_value * p_matrix
            )
            denominator, numerator = subset_formula(
                n_vertices, graph_edges, alpha_value, ell_value, t_value
            )
            np.testing.assert_allclose(
                denominator, np.linalg.det(matrix), rtol=2e-10, atol=2e-10
            )
            np.testing.assert_allclose(
                numerator / denominator,
                np.linalg.inv(matrix),
                rtol=2e-10,
                atol=2e-10,
            )
            comparison_count += 1

assert graph_count == 74
assert comparison_count == 222
print(
    "PASS: literal counterexample and incidence-minor resolvent identity; "
    f"{graph_count} labelled graphs, {comparison_count} parameterized comparisons"
)
