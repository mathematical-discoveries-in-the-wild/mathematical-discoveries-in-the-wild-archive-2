#!/usr/bin/env python3
"""Numerical sanity checks for the proved pinching-refinement subcases.

This script is not part of the proof.  It computes the normalized word
average as a coefficient of Tr(A+tB)^(n+m) and constructs E_A(B) from the
spectral projections of A.
"""

from __future__ import annotations

import math
import numpy as np


def word_average(a: np.ndarray, b: np.ndarray, n: int, m: int) -> float:
    """Return A_{n,m}(A,B) using a matrix-polynomial recurrence."""
    degree = n + m
    coeff = [np.eye(a.shape[0], dtype=complex)]
    for step in range(degree):
        nxt = [np.zeros_like(a, dtype=complex) for _ in range(step + 2)]
        for k, matrix in enumerate(coeff):
            nxt[k] += matrix @ a
            nxt[k + 1] += matrix @ b
        coeff = nxt
    value = np.trace(coeff[m]) / math.comb(degree, m)
    if abs(value.imag) > 2e-8 * (1.0 + abs(value.real)):
        raise AssertionError(f"unexpected imaginary residue: {value}")
    return float(value.real)


def pinching(a: np.ndarray, b: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    """Pinch B by the spectral subspaces of Hermitian A."""
    values, vectors = np.linalg.eigh(a)
    result = np.zeros_like(b, dtype=complex)
    start = 0
    while start < len(values):
        stop = start + 1
        scale = max(1.0, abs(values[start]))
        while stop < len(values) and abs(values[stop] - values[start]) <= tol * scale:
            stop += 1
        block = vectors[:, start:stop]
        projector = block @ block.conj().T
        result += projector @ b @ projector
        start = stop
    return (result + result.conj().T) / 2.0


def random_psd(rng: np.random.Generator, dim: int, rank: int | None = None) -> np.ndarray:
    if rank is None:
        rank = dim
    x = rng.normal(size=(dim, rank)) + 1j * rng.normal(size=(dim, rank))
    matrix = x @ x.conj().T / (2.0 * rank)
    return matrix / max(1.0, np.linalg.norm(matrix, 2))


def check_gap(a: np.ndarray, b: np.ndarray, n: int, m: int, label: str) -> float:
    lhs = word_average(a, b, n, m)
    rhs = word_average(a, pinching(a, b), n, m)
    gap = lhs - rhs
    tolerance = 2e-8 * (1.0 + abs(lhs) + abs(rhs))
    if gap < -tolerance:
        raise AssertionError(
            f"{label}: negative gap {gap:.6e} at (n,m)=({n},{m}); "
            f"lhs={lhs:.6e}, rhs={rhs:.6e}"
        )
    return gap


def main() -> None:
    rng = np.random.default_rng(260517782)
    minima: dict[str, float] = {}

    # Corollary: all 2x2 pairs and all exponents (finite random audit).
    gaps = []
    for _ in range(50):
        a, b = random_psd(rng, 2), random_psd(rng, 2)
        for n in range(0, 8):
            for m in range(0, 8):
                gaps.append(check_gap(a, b, n, m, "2x2"))
    minima["2x2, 0<=n,m<=7"] = min(gaps)

    # Theorem: arbitrary dimension for n=0 or n=1.
    gaps = []
    for _ in range(35):
        a, b = random_psd(rng, 5), random_psd(rng, 5)
        for n in (0, 1):
            for m in range(0, 9):
                gaps.append(check_gap(a, b, n, m, "n<=1"))
    minima["dimension 5, n<=1, m<=8"] = min(gaps)

    # Theorem: rank-one A in arbitrary dimension.
    gaps = []
    for _ in range(35):
        vector = rng.normal(size=5) + 1j * rng.normal(size=5)
        vector /= np.linalg.norm(vector)
        a = np.outer(vector, vector.conj())
        b = random_psd(rng, 5)
        for n in range(1, 7):
            for m in range(0, 7):
                gaps.append(check_gap(a, b, n, m, "rank-one A"))
    minima["dimension 5, rank-one A, n<=6, m<=6"] = min(gaps)

    # Theorem: phase-balanced pairs.  Start with entrywise-nonnegative PSD B,
    # then obscure the property by a random diagonal phase gauge.
    gaps = []
    for _ in range(35):
        x = rng.uniform(0.0, 1.0, size=(4, 4))
        b0 = x @ x.T
        b0 /= max(1.0, np.linalg.norm(b0, 2))
        phases = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=4))
        d = np.diag(phases)
        b = d @ b0 @ d.conj().T
        # Include a repeated eigenspace in half the trials.
        spectrum = np.array([0.1, 0.3, 0.3 if len(gaps) % 2 == 0 else 0.6, 1.0])
        a = np.diag(spectrum)
        for n in range(0, 7):
            for m in range(0, 7):
                gaps.append(check_gap(a, b, n, m, "phase-balanced"))
    minima["phase-balanced dimension 4, n,m<=6"] = min(gaps)

    # New theorem: the first higher-cycle corner (n,m)=(2,3).
    gaps = []
    for _ in range(100):
        dim = int(rng.integers(3, 8))
        rank_a = int(rng.integers(1, dim + 1))
        rank_b = int(rng.integers(1, dim + 1))
        a, b = random_psd(rng, dim, rank_a), random_psd(rng, dim, rank_b)
        gaps.append(check_gap(a, b, 2, 3, "all-dimensional (2,3)"))
    minima["dimensions 3--7, (n,m)=(2,3)"] = min(gaps)

    # Source-paper benchmark: m=2 for arbitrary PSD pairs.
    gaps = []
    for _ in range(50):
        a, b = random_psd(rng, 5), random_psd(rng, 5)
        for n in range(0, 10):
            gaps.append(check_gap(a, b, n, 2, "source m=2"))
    minima["source theorem, dimension 5, m=2, n<=9"] = min(gaps)

    print("All pinching-subcase checks passed.")
    for label, gap in minima.items():
        print(f"  minimum gap [{label}]: {gap:.6e}")


if __name__ == "__main__":
    main()
