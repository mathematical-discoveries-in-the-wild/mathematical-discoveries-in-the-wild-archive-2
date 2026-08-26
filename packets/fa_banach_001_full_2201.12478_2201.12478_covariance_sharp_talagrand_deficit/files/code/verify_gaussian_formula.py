#!/usr/bin/env python3
"""Sanity-check the Gaussian equality formula and scalar monotonicity."""

from math import isclose, log, sqrt
from random import Random


def gaussian_kl(eigenvalues: list[float], mean_sq: float) -> float:
    n = len(eigenvalues)
    return 0.5 * (
        sum(eigenvalues) + mean_sq - n - sum(log(x) for x in eigenvalues)
    )


def gaussian_w2_sq(eigenvalues: list[float], mean_sq: float) -> float:
    return mean_sq + sum(1 + x - 2 * sqrt(x) for x in eigenvalues)


def matrix_bound(eigenvalues: list[float]) -> float:
    n = len(eigenvalues)
    return 0.5 * sum(log(x) for x in eigenvalues) - sum(
        sqrt(x) for x in eigenvalues
    ) + n


def scalar_bound(n: int, beta: float) -> float:
    return n * (1 + 0.5 * log(beta) - sqrt(beta))


rng = Random(220112478)
tested = 10_000

for _ in range(tested):
    n = rng.randint(1, 12)
    beta = 10 ** rng.uniform(-4, -0.0001)
    eigenvalues = [10 ** rng.uniform(-5, log(beta, 10)) for _ in range(n)]
    mean_sq = 10 ** rng.uniform(-5, 3)

    deficit = 0.5 * gaussian_w2_sq(eigenvalues, mean_sq) - gaussian_kl(
        eigenvalues, mean_sq
    )
    anisotropic = matrix_bound(eigenvalues)
    isotropic = scalar_bound(n, beta)

    assert isclose(deficit, anisotropic, rel_tol=2e-12, abs_tol=2e-12)
    assert anisotropic <= isotropic + 2e-12

print(f"checked {tested} random Gaussian covariance/translation cases")
print("Gaussian deficit equals the anisotropic bound and obeys the scalar bound")
