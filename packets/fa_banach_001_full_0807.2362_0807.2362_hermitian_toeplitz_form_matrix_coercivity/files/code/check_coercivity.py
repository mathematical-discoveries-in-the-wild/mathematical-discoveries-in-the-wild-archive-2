#!/usr/bin/env python3
"""Finite checks for the 0807.2362 coercivity packet.

The computations are diagnostics, not ingredients of the proof.
"""

from __future__ import annotations

import numpy as np


def hermitian_part(a: np.ndarray) -> np.ndarray:
    return (a + a.conj().T) / 2


def check_schur(seed: int = 20260809) -> None:
    rng = np.random.default_rng(seed)
    for _ in range(100):
        x = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        p = x.conj().T @ x + np.eye(3)
        b = rng.normal(size=(2, 3)) + 1j * rng.normal(size=(2, 3))
        y = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        s = y.conj().T @ y + 0.4 * np.eye(2)
        q = s + b @ np.linalg.solve(p, b.conj().T)
        a = np.block([[p, b.conj().T], [b, q]])
        recovered = q - b @ np.linalg.solve(p, b.conj().T)
        assert np.linalg.norm(recovered - s) < 1e-10
        assert np.linalg.eigvalsh(a)[0] > 0
        assert np.linalg.eigvalsh(recovered)[0] > 0


def symbol(coeffs: dict[int, np.ndarray], theta: float) -> np.ndarray:
    return sum(b * np.exp(1j * k * theta) for k, b in coeffs.items())


def block_toeplitz(coeffs: dict[int, np.ndarray], n: int) -> np.ndarray:
    d = next(iter(coeffs.values())).shape[0]
    t = np.zeros((n * d, n * d), dtype=complex)
    for m in range(n):
        for j in range(n):
            t[m * d : (m + 1) * d, j * d : (j + 1) * d] = coeffs.get(
                m - j, np.zeros((d, d), dtype=complex)
            )
    return t


def check_toeplitz() -> None:
    coeffs = {
        -2: np.array([[0.03j, 0.02], [-0.01j, 0.04]]),
        -1: np.array([[0.10, -0.05], [0.10j, 0.20]]),
        0: np.array([[3.0 + 0.2j, 0.15], [-0.05j, 4.0 - 0.1j]]),
        1: np.array([[0.40, 0.10j], [0.20, -0.30]]),
        2: np.array([[-0.02, 0.03j], [0.01, 0.02]]),
    }
    grid = np.linspace(0.0, 2 * np.pi, 32768, endpoint=False)
    g_grid = min(
        np.linalg.eigvalsh(hermitian_part(symbol(coeffs, th)))[0]
        for th in grid
    )
    t = block_toeplitz(coeffs, 384)
    finite_edge = np.linalg.eigvalsh(hermitian_part(t))[0]
    # Every compression is bounded below by the symbol edge. Large sections
    # approach it from above.
    assert finite_edge >= g_grid - 2e-7
    assert finite_edge <= g_grid + 2e-3
    print(f"sampled symbol edge: {g_grid:.9f}")
    print(f"384-block Toeplitz edge: {finite_edge:.9f}")


def check_source_proposition_counterexample() -> None:
    # a(z,z)=|z_1|^2+|z_2|^2 has coercivity constant 1.
    a = np.eye(2)
    assert np.linalg.eigvalsh(a)[0] == 1.0
    # Source condition (1.22), with z_1=1,z_2=0, becomes 0 >= alpha.
    for alpha in (1.0, 0.1, 1e-8):
        lhs = 0.0
        rhs = alpha
        assert lhs < rhs


if __name__ == "__main__":
    check_schur()
    check_toeplitz()
    check_source_proposition_counterexample()
    print("all finite checks passed")
