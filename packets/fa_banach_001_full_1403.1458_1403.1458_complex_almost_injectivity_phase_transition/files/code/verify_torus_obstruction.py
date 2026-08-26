#!/usr/bin/env python3
"""Deterministic numerical stress test for the plane--torus proof.

This script is not used as evidence for the topological theorem.  It checks
the linear-algebra reductions and numerically exhibits the second phase zero
for random critical Parseval frames.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import root


RNG = np.random.default_rng(14031458)


def parseval_frame(d: int) -> np.ndarray:
    n = 2 * d - 1
    a = RNG.normal(size=(n, d)) + 1j * RNG.normal(size=(n, d))
    eigval, eigvec = np.linalg.eigh(a.conj().T @ a)
    invsqrt = eigvec @ np.diag(eigval ** -0.5) @ eigvec.conj().T
    v = a @ invsqrt
    assert np.linalg.norm(v.conj().T @ v - np.eye(d)) < 1e-11
    return v


def realification(v: np.ndarray) -> np.ndarray:
    return np.block([[v.real, -v.imag], [v.imag, v.real]])


def phase_jacobian(k: np.ndarray, z: np.ndarray) -> np.ndarray:
    n = len(z)
    e = np.zeros((n, n - 1))
    e[1:, :] = np.eye(n - 1)
    complex_jac = k.conj().T @ (1j * np.diag(z) @ e)
    return np.vstack([complex_jac.real, complex_jac.imag])


def projective_jacobian(v: np.ndarray, z: np.ndarray) -> np.ndarray:
    n, d = v.shape
    vr = realification(v)
    zr = np.r_[z.real, z.imag]
    izr = np.r_[-z.imag, z.real]
    horizontal = null_space(np.vstack([zr @ vr, izr @ vr]))
    assert horizontal.shape == (2 * d, 2 * d - 2)

    dmag = np.zeros((n, 2 * n))
    for j in range(n):
        dmag[j, j] = 2 * z[j].real
        dmag[j, n + j] = 2 * z[j].imag
    # The rows sum to zero on the unit-sphere tangent, so delete one row to
    # use affine coordinates on the probability simplex.
    return (dmag @ vr @ horizontal)[1:, :]


def phase_zeros(v: np.ndarray, z: np.ndarray, starts: int = 400) -> list[np.ndarray]:
    n, d = v.shape
    k = null_space(v.conj().T)

    def equations(theta: np.ndarray) -> np.ndarray:
        phases = np.r_[1.0 + 0.0j, np.exp(1j * theta)]
        value = k.conj().T @ (phases * z)
        return np.r_[value.real, value.imag]

    seeds = [np.zeros(n - 1), *RNG.uniform(-np.pi, np.pi, size=(starts, n - 1))]
    solutions: list[np.ndarray] = []
    for seed in seeds:
        answer = root(equations, seed)
        if not answer.success or np.linalg.norm(equations(answer.x)) >= 1e-8:
            continue
        wrapped = (answer.x + np.pi) % (2 * np.pi) - np.pi
        if all(np.linalg.norm(np.angle(np.exp(1j * (wrapped - old)))) >= 1e-5 for old in solutions):
            solutions.append(wrapped)
    return solutions


def run_case(d: int) -> None:
    v = parseval_frame(d)
    x = RNG.normal(size=d) + 1j * RNG.normal(size=d)
    x /= np.linalg.norm(x)
    z = v @ x
    assert np.min(np.abs(z)) > 1e-8

    k = null_space(v.conj().T)
    j_phase = phase_jacobian(k, z)
    j_proj = projective_jacobian(v, z)
    expected = 2 * d - 2
    rank_phase = np.linalg.matrix_rank(j_phase, tol=1e-9)
    rank_proj = np.linalg.matrix_rank(j_proj, tol=1e-9)
    assert rank_phase == rank_proj == expected

    zeros = phase_zeros(v, z)
    assert len(zeros) >= 2
    nontrivial = [u for u in zeros if np.linalg.norm(np.angle(np.exp(1j * u))) > 1e-5]
    assert nontrivial
    print(
        f"d={d}, N={2*d-1}: ranks={rank_phase}/{rank_proj}, "
        f"phase zeros found={len(zeros)}, "
        f"|det D(Psi)_identity|={abs(np.linalg.det(j_phase)):.6e}"
    )


def main() -> None:
    for d in (2, 3, 4):
        run_case(d)
    print("all deterministic stress tests passed")


if __name__ == "__main__":
    main()

