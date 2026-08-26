"""Exact-shape sanity checks for the M3 pure-extension counterexample."""

import numpy as np


def matrix_unit(j: int, k: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[j, k] = 1
    return out


I = np.eye(3, dtype=complex)
E11 = matrix_unit(0, 0)
E22 = matrix_unit(1, 1)
E33 = matrix_unit(2, 2)
E13 = matrix_unit(0, 2)
E31 = matrix_unit(2, 0)
E23 = matrix_unit(1, 2)
E32 = matrix_unit(2, 1)

H = E11 + E22
X = E13 + E31
Y = E23 + E32
A = H + 1j * X
B = H + 1j * Y

assert np.allclose(H, H.conj().T)
assert np.allclose(X, X.conj().T)
assert np.allclose(Y, Y.conj().T)
assert np.allclose(E33, I - H)

e1 = np.array([1, 0, 0], dtype=complex)
e2 = np.array([0, 1, 0], dtype=complex)


def omega(vector: np.ndarray, matrix: np.ndarray) -> complex:
    return np.vdot(vector, matrix @ vector)


for generator in (I, A, B):
    assert np.allclose(omega(e1, generator), omega(e2, generator))

units = [
    E11,
    E22,
    E33,
    X @ E33,
    E33 @ X,
    Y @ E33,
    E33 @ Y,
    (X @ E33) @ (E33 @ Y),
    (Y @ E33) @ (E33 @ X),
]
span_matrix = np.stack([u.reshape(-1) for u in units], axis=1)
assert np.linalg.matrix_rank(span_matrix) == 9

print("verified: restrictions agree and C*(M) spans all of M3")

