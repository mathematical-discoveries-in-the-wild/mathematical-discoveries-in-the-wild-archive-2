#!/usr/bin/env python3
"""Exact checks for the counterexample packet for arXiv:2511.17343."""

from sympy import Matrix, Rational, cos, pi, simplify, sqrt


def cycle_adjacency(n: int) -> Matrix:
    return Matrix(
        n,
        n,
        lambda i, j: 1 if (i - j) % n in (1, n - 1) else 0,
    )


omega = 1 - 1 / sqrt(2)
expander_gap = Rational(2, 5)
assert simplify(expander_gap - omega) > 0

A8 = cycle_adjacency(8)
L8 = Matrix.eye(8) - A8 / 2
eigenvalues = L8.eigenvals()
assert eigenvalues[Rational(0)] == 1
assert eigenvalues[omega] == 2
assert sum(mult for ev, mult in eigenvalues.items() if ev <= omega) == 3

# For phi=1 on X\{x} and 0 at x in a d-regular graph:
d = Rational(10)
laplacian_norm_sq = 1 + d * (1 / d) ** 2
assert laplacian_norm_sq == Rational(11, 10)

for n_vertices in (20, 200, 2000):
    phi_norm_sq = n_vertices - 1
    ratio_sq = Rational(phi_norm_sq) / laplacian_norm_sq
    expected = Rational(10 * (n_vertices - 1), 11)
    assert ratio_sq == expected

# The chosen subsequence N_n >= n^4 makes sum N_n/n^2 divergent.
for n in range(1, 20):
    assert Rational(n**4, n**2) == n**2

print("omega =", omega)
print("2/5 - omega =", simplify(expander_gap - omega))
print("C8 normalized-Laplacian eigenvalues =", eigenvalues)
print("dim E_[0,omega](C8) = 3")
print("||L phi_n||^2 =", laplacian_norm_sq)
print("all exact checks passed")

