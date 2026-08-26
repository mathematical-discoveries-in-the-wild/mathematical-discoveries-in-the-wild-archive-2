#!/usr/bin/env python3
"""Independent numerical checks for the sparse n=4 equality case.

The packet proof is exact and does not depend on this script.  The numerical
checks exercise the matrix convention, the cube-root equality witness, and a
large random sample of the phase torus.
"""

from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import differential_evolution


SIGNS = np.asarray(list(itertools.product((1.0, -1.0), repeat=2)))
A = np.column_stack((np.ones(4), SIGNS, np.zeros(4))).astype(complex)


def values(theta: np.ndarray) -> np.ndarray:
    x = np.array([1.0, np.exp(1j * theta[0]), np.exp(1j * theta[1]), 1.0])
    return np.abs(A @ x)


omega = np.exp(2j * np.pi / 3)
witness = np.array([1.0, omega, omega**2, 1.0])
witness_values = np.abs(A @ witness)
assert np.allclose(np.sort(witness_values), [0.0, 2.0, 2.0, 2.0], atol=1e-12)

rng = np.random.default_rng(260212868)
theta = rng.uniform(0.0, 2.0 * np.pi, size=(1_000_000, 2))
z = np.exp(1j * theta[:, 0])
w = np.exp(1j * theta[:, 1])
sample_values = np.max(
    np.abs(1.0 + SIGNS[:, 0, None] * z + SIGNS[:, 1, None] * w), axis=0
)
assert np.min(sample_values) >= 2.0 - 1e-12

de = differential_evolution(
    lambda th: float(np.max(values(th))),
    [(0.0, 2.0 * np.pi)] * 2,
    seed=260212868,
    popsize=30,
    maxiter=1000,
    tol=1e-12,
    polish=True,
)
assert abs(de.fun - 2.0) < 1e-10

print("matrix=")
print(A.real.astype(int))
print("cube_root_witness_values=", witness_values)
print("random_sample_minimum=", float(np.min(sample_values)))
print("global_optimizer_value=", float(de.fun))
print("global_optimizer_angles=", de.x)
