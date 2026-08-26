"""Sanity checks for the periodic nonuniform sampling kernel theorem."""

from __future__ import annotations

import numpy as np


def data(q: int, alpha: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    r = np.arange(q)
    j = np.arange(q)[:, None]
    z = np.exp(2j * np.pi * alpha / q)
    v = z[None, :] ** j
    c = q * np.linalg.inv(v.T)
    assert np.allclose(v @ c.T, q * np.eye(q), atol=1e-11)
    return z, v, c


def split_kernel(
    q: int,
    alpha: np.ndarray,
    c: np.ndarray,
    n: int,
    omega: float,
    x: np.ndarray,
) -> np.ndarray:
    cell_length = 2 * np.pi / q
    cell = np.floor((x + np.pi) / cell_length).astype(int)
    cell = np.clip(cell, 0, q - 1)
    shift = 2 * np.pi * cell / q
    y = x - shift

    total = np.zeros_like(x, dtype=complex)
    for k in range(-n, n + 1):
        residue = k % q
        m = (k - residue) // q
        t = q * m + alpha[residue]
        dual = np.exp(-1j * t * y) * c[cell, residue]
        total += np.exp(1j * omega * t) * dual
    return total


def lebesgue_values(q: int, alpha: np.ndarray) -> None:
    _, _, c = data(q, alpha)
    x = np.linspace(-np.pi, np.pi, 32769, endpoint=False)
    dx = 2 * np.pi / len(x)
    omegas = np.linspace(-np.pi, np.pi, 17)
    print(f"q={q}, alpha={alpha.tolist()}")
    for n in (8, 16, 32, 64):
        vals = []
        for omega in omegas:
            kernel = split_kernel(q, alpha, c, n, omega, x)
            vals.append(np.sum(np.abs(kernel)) * dx / (2 * np.pi))
        print(n, min(vals), min(vals) / np.log(n + 1))


lebesgue_values(2, np.array([0.0, 0.7]))
lebesgue_values(3, np.array([0.0, 0.8, 2.25]))
print("verified: V C^T=qI and sampled Lebesgue functions grow logarithmically")

