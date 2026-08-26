#!/usr/bin/env python3
"""Exact and numerical checks for the square-boundary Riesz basis packet."""

from __future__ import annotations

import numpy as np
import sympy as sp


def exact_matrix_check() -> None:
    m = sp.Matrix(
        [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 0, -1, 1],
        ]
    )
    x = sp.symbols("x")
    gram = m.conjugate().T * m
    expected = (x**2 - 4 * x + 2) ** 2
    actual = gram.charpoly(x).as_expr()
    assert m.det() == -2
    assert sp.expand(actual - expected) == 0
    assert m.inv() == sp.Rational(1, 2) * sp.Matrix(
        [
            [1, -1, 1, 1],
            [-1, 1, 1, -1],
            [1, 1, -1, -1],
            [1, 1, -1, 1],
        ]
    )
    print("exact determinant: -2")
    print("exact Gram characteristic polynomial: (x^2 - 4*x + 2)^2")
    print("exact squared Riesz bounds after the sqrt(2) factor: 4 +/- 2*sqrt(2)")


def direct_synthesis_check(seed: int = 230914625, trials: int = 40) -> None:
    rng = np.random.default_rng(seed)
    nvals = np.arange(-7, 8)
    # A dense grid makes this an independent numerical check of the original
    # four edge restrictions, not a replacement for the exact proof.
    t = (np.arange(32768) + 0.5) / 32768
    lower = 4 - 2 * np.sqrt(2)
    upper = 4 + 2 * np.sqrt(2)
    observed = []

    families = (
        lambda n: (n, n + 0.5),
        lambda n: (n, n + 1.0),
        lambda n: (n - 0.5, -n + 0.5),
        lambda n: (n - 0.5, -n),
    )

    for _ in range(trials):
        coeff = rng.normal(size=(4, len(nvals))) + 1j * rng.normal(
            size=(4, len(nvals))
        )
        edges = np.zeros((4, len(t)), dtype=complex)
        for j, family in enumerate(families):
            for k, n in enumerate(nvals):
                p, q = family(float(n))
                c = coeff[j, k]
                edges[0] += c * np.exp(2j * np.pi * p * t)
                edges[1] += c * np.exp(2j * np.pi * (p * t + q))
                edges[2] += c * np.exp(2j * np.pi * q * t)
                edges[3] += c * np.exp(2j * np.pi * (p + q * t))
        norm_sq = float(np.mean(np.sum(np.abs(edges) ** 2, axis=0)))
        coeff_sq = float(np.sum(np.abs(coeff) ** 2))
        ratio = norm_sq / coeff_sq
        assert lower - 2e-5 <= ratio <= upper + 2e-5
        observed.append(ratio)

    print(f"random direct-synthesis trials: {trials}")
    print(f"observed norm ratios: [{min(observed):.9f}, {max(observed):.9f}]")
    print(f"proved interval: [{lower:.9f}, {upper:.9f}]")


if __name__ == "__main__":
    exact_matrix_check()
    direct_synthesis_check()

