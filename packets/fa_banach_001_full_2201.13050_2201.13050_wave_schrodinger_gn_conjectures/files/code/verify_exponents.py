#!/usr/bin/env python3
"""Sanity checks for the curvature substitutions and ell2 summation."""

from __future__ import annotations

import numpy as np


def check_formulas() -> None:
    for d in range(3, 15):
        for kappa in np.linspace(0.05, 0.95, 19):
            alpha = 1.0 - kappa

            wave_k = d - 2
            assert np.isclose(2 * alpha / (wave_k + 2), 2 * (1 - kappa) / d)
            assert np.isclose(
                (wave_k + 2 * alpha) / (2 * (wave_k + 1)),
                (d - 2 * kappa) / (2 * (d - 1)),
            )

            sch_k = d - 1
            assert np.isclose(2 * alpha / (sch_k + 2), 2 * (1 - kappa) / (d + 1))
            assert np.isclose(
                (sch_k + 2 * alpha) / (2 * (sch_k + 1)),
                (d + 1 - 2 * kappa) / (2 * d),
            )


def check_sequence_inequality() -> None:
    rng = np.random.default_rng(220113050)
    worst_ratio = 0.0
    for _ in range(1000):
        kappa = rng.uniform(0.001, 0.999)
        a = rng.lognormal(size=100)
        b = rng.lognormal(size=100)
        lhs = np.sqrt(np.sum(a ** (2 * (1 - kappa)) * b ** (2 * kappa)))
        rhs = np.linalg.norm(a) ** (1 - kappa) * np.linalg.norm(b) ** kappa
        worst_ratio = max(worst_ratio, float(lhs / rhs))
        assert lhs <= rhs * (1 + 1e-12)
    print(f"worst sequence-Holder ratio: {worst_ratio:.12f}")


def check_finite_two_concavity() -> None:
    rng = np.random.default_rng(17)
    worst_ratio = 0.0
    # Counting measure supplies a finite exact model of L^r.
    for r in np.linspace(1.0, 2.0, 11):
        f = rng.lognormal(size=(80, 60))
        individual = np.sum(f**r, axis=1) ** (1 / r)
        lhs = np.linalg.norm(individual)
        square = np.sqrt(np.sum(f**2, axis=0))
        rhs = np.sum(square**r) ** (1 / r)
        worst_ratio = max(worst_ratio, float(lhs / rhs))
        assert lhs <= rhs * (1 + 1e-12)
    print(f"worst 2-concavity ratio: {worst_ratio:.12f}")


if __name__ == "__main__":
    check_formulas()
    print("curvature and scaling formulas: PASS")
    check_sequence_inequality()
    check_finite_two_concavity()
    print("PASS")
