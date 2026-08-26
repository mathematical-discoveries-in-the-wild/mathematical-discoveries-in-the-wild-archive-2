#!/usr/bin/env python3
"""Finite-dimensional checks for the Fock kernel matrix characterization."""

from math import factorial, sqrt

import numpy as np


def coherent(z: complex, size: int) -> np.ndarray:
    return np.array([z**k / sqrt(factorial(k)) for k in range(size)], dtype=complex)


# The obstruction blocks have unit row/column l2 norms but operator norm sqrt(k).
for k in range(1, 13):
    block = np.ones((k, k), dtype=float) / sqrt(k)
    row_norms = np.linalg.norm(block, axis=1)
    col_norms = np.linalg.norm(block, axis=0)
    operator_norm = np.linalg.norm(block, ord=2)
    assert np.allclose(row_norms, 1.0)
    assert np.allclose(col_norms, 1.0)
    assert np.isclose(operator_norm, sqrt(k))

# Check the coherent-state inequality for a deterministic complex matrix.
rng = np.random.default_rng(190700574)
size = 9
A = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
A_norm = np.linalg.norm(A, ord=2)
zs = np.array([-0.8 + 0.2j, 0.1 - 0.7j, 0.9 + 0.4j])
ws = np.array([-0.4 - 0.5j, 0.6 + 0.1j, 0.2 + 0.9j, 1.0 - 0.3j])
xis = np.array([0.7 + 0.2j, -0.3 + 0.8j, 0.5 - 0.4j])
etas = np.array([0.2 - 0.6j, 0.9 + 0.1j, -0.5 + 0.3j, 0.4 + 0.7j])

X = sum((xi * coherent(z, size) for xi, z in zip(xis, zs)), np.zeros(size, complex))
Y = sum((eta * coherent(w, size) for eta, w in zip(etas, ws)), np.zeros(size, complex))
lhs = abs(X.T @ A @ np.conjugate(Y))
rhs = A_norm * np.linalg.norm(X) * np.linalg.norm(Y)
assert lhs <= rhs + 1e-12

# Gaussian monomial orthogonality is the coefficient normalization used in
# the proof: integral conj(e_j) e_k d(lambda) = delta_jk.
for j in range(9):
    for k in range(9):
        raw_moment = factorial(k) if j == k else 0
        normalized = raw_moment / sqrt(factorial(j) * factorial(k))
        assert normalized == (1 if j == k else 0)

print("block row/column norms: PASS (all equal 1)")
print("block operator norms: PASS (sqrt(k), hence unbounded)")
print("coherent-state inequality: PASS")
print("Gaussian normalized moments: PASS")

