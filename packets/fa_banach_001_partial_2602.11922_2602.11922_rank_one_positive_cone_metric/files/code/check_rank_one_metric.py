#!/usr/bin/env python3
"""Numerical sanity checks for the rank-one cone theorem.

This script is not a proof.  It checks the closed trace formula against direct
functional calculus and samples triangle inequalities on the rank-one cone.
"""

from __future__ import annotations

import numpy as np


def positive_power(a: np.ndarray, exponent: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(a)
    # The test matrices are exactly rank one.  Remove roundoff eigenvalues
    # before taking fractional powers, which would otherwise amplify them.
    scale = max(float(np.max(np.abs(values))), 1.0)
    values[np.abs(values) < 1e-12 * scale] = 0.0
    values = np.clip(values, 0.0, None) ** exponent
    return (vectors * values) @ vectors.conj().T


def kappa(a: np.ndarray, b: np.ndarray, p: float) -> np.ndarray:
    left = positive_power(a, p / 4.0)
    middle = positive_power(b, p / 2.0)
    return positive_power(left @ middle @ left, 1.0 / p)


def distance(a: np.ndarray, b: np.ndarray, p: float) -> float:
    value = np.trace((a + b) / 2.0 - kappa(a, b, p)).real
    return float(np.sqrt(max(value, 0.0)))


def random_unit(rng: np.random.Generator, n: int) -> np.ndarray:
    u = rng.normal(size=n) + 1j * rng.normal(size=n)
    return u / np.linalg.norm(u)


def rank_one(radius_squared: float, u: np.ndarray) -> np.ndarray:
    return radius_squared * np.outer(u, u.conj())


def main() -> None:
    rng = np.random.default_rng(260211922)
    n = 4
    ps = (0.5, 1.0, 1.5, 1.9, 2.0)
    formula_error = 0.0
    maximum_triangle_defect = -np.inf
    trials = 2_000

    for p in ps:
        for _ in range(trials):
            units = [random_unit(rng, n) for _ in range(3)]
            scalars = rng.lognormal(mean=0.0, sigma=1.2, size=3)
            matrices = [rank_one(a, u) for a, u in zip(scalars, units)]

            a, b = scalars[0], scalars[1]
            direct_trace = np.trace(kappa(matrices[0], matrices[1], p)).real
            closed_trace = np.sqrt(a * b) * abs(np.vdot(units[0], units[1])) ** (2.0 / p)
            formula_error = max(formula_error, abs(direct_trace - closed_trace))

            dab = distance(matrices[0], matrices[1], p)
            dbc = distance(matrices[1], matrices[2], p)
            dac = distance(matrices[0], matrices[2], p)
            maximum_triangle_defect = max(maximum_triangle_defect, dac - dab - dbc)

    print(f"parameter values: {ps}")
    print(f"random triples per parameter: {trials}")
    print(f"maximum trace-formula absolute error: {formula_error:.3e}")
    print(f"maximum triangle defect d(A,C)-d(A,B)-d(B,C): {maximum_triangle_defect:.3e}")

    if formula_error > 5e-7:
        raise SystemExit("trace-formula check failed")
    if maximum_triangle_defect > 5e-8:
        raise SystemExit("triangle check failed")


if __name__ == "__main__":
    main()
