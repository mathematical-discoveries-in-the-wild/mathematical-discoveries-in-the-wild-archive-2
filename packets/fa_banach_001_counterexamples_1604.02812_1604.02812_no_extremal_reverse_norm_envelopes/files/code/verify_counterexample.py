#!/usr/bin/env python3
"""Verify the finite matrices and exact witnesses in the M_3 counterexample."""

import numpy as np


def trace_norm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False).sum())


def numerical_radius(a: np.ndarray, samples: int = 20000) -> float:
    # w(A) = max_theta lambda_max(Re(e^{-i theta} A)).
    best = 0.0
    for theta in np.linspace(0.0, 2.0 * np.pi, samples, endpoint=False):
        rotated = np.exp(-1j * theta) * a
        hermitian = (rotated + rotated.conj().T) / 2.0
        best = max(best, float(np.linalg.eigvalsh(hermitian)[-1]))
    return best


e = np.zeros((3, 3), dtype=complex)
e[0, 0] = 1.0
j = np.zeros((3, 3), dtype=complex)
j[1, 2] = 1.0
x = e + j
y = e + 2.0 * j
p = e.copy()
q = np.eye(3) - p

assert np.allclose(p.conj().T @ p + q.conj().T @ q, np.eye(3))
assert np.allclose(p @ x @ p, e)
assert np.allclose(q @ x @ q, j)
assert np.isclose(trace_norm(e), 1.0)
assert np.isclose(trace_norm(j), 1.0)
assert np.isclose(trace_norm(x), 2.0)
assert np.isclose(numerical_radius(j), 0.5, atol=2e-7)
assert np.isclose(numerical_radius(y), 1.0, atol=2e-7)
assert np.isclose(np.trace(e.conj().T @ e).real, 1.0)
assert np.isclose(np.trace(j.conj().T @ (2.0 * j)).real, 2.0)
assert np.isclose(np.trace(x.conj().T @ y).real, 3.0)

# These omega_* values are certified by the witnesses above and the matching
# analytic upper bounds in main.tex.
omega_star = {"E": 1.0, "J": 2.0, "X": 3.0}
p_values = {
    "E": max(trace_norm(e), 0.75 * omega_star["E"]),
    "J": max(trace_norm(j), 0.75 * omega_star["J"]),
    "X": max(trace_norm(x), 0.75 * omega_star["X"]),
}
assert p_values == {"E": 1.0, "J": 1.5, "X": 2.25}
assert p_values["E"] + p_values["J"] > p_values["X"]
for c in np.linspace(0.5001, 0.9999, 1000):
    assert 1.0 + 2.0 * c > max(2.0, 3.0 * c)

print("projection constraint and compressions: PASS")
print("trace norms (E,J,X) = (1,1,2): PASS")
print("numerical-radius witness values w(J)=1/2, w(E+2J)=1: PASS")
print("dual pairings certify omega_*(E,J,X) >= (1,2,3): PASS")
print("analytic upper bounds certify omega_*(E,J,X) <= (1,2,3): documented")
print("p(E)+p(J)=5/2 > p(X)=9/4: PASS")
print("robust family c in (1/2,1), sampled at 1000 values: PASS")
