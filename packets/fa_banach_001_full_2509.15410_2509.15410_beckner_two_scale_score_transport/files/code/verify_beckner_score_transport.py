"""Finite sanity checks for the two-scale Beckner packet.

The checks are not part of the proof.  They test:

1. the sharp power-Pinsker inequality on binary laws;
2. the bounded-score transport inequality on random finite laws;
3. the closed form for the optimized joint constant;
4. growth in the variance-only obstruction.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize_scalar


RNG = np.random.default_rng(250915410)


def power_divergence(prob: np.ndarray, density: np.ndarray, p: float) -> float:
    return float((np.dot(prob, density**p) - 1.0) / (p - 1.0))


def check_power_pinsker() -> int:
    checked = 0
    for p in (1.01, 1.1, 1.25, 1.5, 1.75, 1.99, 2.0):
        for base in np.linspace(0.002, 0.998, 251):
            prob = np.array([base, 1.0 - base])
            for tilted in np.linspace(0.002, 0.998, 251):
                density = np.array([tilted / base, (1.0 - tilted) / (1.0 - base)])
                divergence = power_divergence(prob, density, p)
                l1 = float(np.dot(prob, np.abs(density - 1.0)))
                assert divergence + 2e-12 >= 0.5 * p * l1 * l1
                checked += 1
    return checked


def check_bounded_score_transport() -> int:
    checked = 0
    for p in (1.03, 1.2, 1.5, 1.8, 2.0):
        for _ in range(5000):
            size = int(RNG.integers(2, 12))
            prob = RNG.dirichlet(np.ones(size))
            density = RNG.dirichlet(np.ones(size)) / prob
            density /= np.dot(prob, density)
            raw_score = RNG.normal(size=(size, 3))
            score = raw_score - np.dot(prob, raw_score)
            bound = float(np.max(np.linalg.norm(score, axis=1)))
            direction = RNG.normal(size=3)
            direction /= np.linalg.norm(direction)
            covariance = float(np.dot(prob, density * (score @ direction)))
            divergence = power_divergence(prob, density, p)
            rhs = (2.0 * bound * bound / p) * divergence
            assert covariance * covariance <= rhs + 2e-11 * max(1.0, rhs)
            checked += 1
    return checked


def zeta_closed(alpha: float, beta: float, ell: float) -> float:
    radicand = (
        4.0 * alpha * alpha * beta * ell * ell
        + (beta - alpha + alpha * beta * ell * ell) ** 2
    )
    return 0.5 * (
        alpha + beta + alpha * beta * ell * ell + math.sqrt(radicand)
    )


def zeta_objective(log_c: float, alpha: float, beta: float, ell: float) -> float:
    c = math.exp(log_c)
    x_energy = beta + alpha * (1.0 + 1.0 / c) * beta * ell * ell
    y_energy = alpha * (1.0 + c)
    return max(x_energy, y_energy)


def check_zeta_formula() -> int:
    checked = 0
    for _ in range(5000):
        alpha, beta, ell = np.exp(RNG.uniform(-5.0, 5.0, size=3))
        numerical = minimize_scalar(
            zeta_objective,
            args=(float(alpha), float(beta), float(ell)),
            bounds=(-30.0, 30.0),
            method="bounded",
            options={"xatol": 1e-12},
        ).fun
        closed = zeta_closed(float(alpha), float(beta), float(ell))
        assert abs(numerical - closed) <= 2e-7 * max(1.0, closed)
        checked += 1
    return checked


def obstruction_ratios(p: float = 1.5) -> list[float]:
    ratios = []
    for n in range(2, 13):
        epsilon = 2.0 ** (-n * n / (2.0 - p))
        amplitude = math.sqrt(n) * epsilon ** (-(p - 1.0) / 2.0)
        divergence = (epsilon ** (1.0 - p) - 1.0) / (p - 1.0)
        ratios.append(amplitude * amplitude / divergence)
    assert all(b > a for a, b in zip(ratios, ratios[1:]))
    return ratios


if __name__ == "__main__":
    pinsker_cases = check_power_pinsker()
    score_cases = check_bounded_score_transport()
    zeta_cases = check_zeta_formula()
    ratios = obstruction_ratios()
    print(f"power-Pinsker binary cases: {pinsker_cases}")
    print(f"bounded-score random cases: {score_cases}")
    print(f"zeta formula cases: {zeta_cases}")
    print("variance-obstruction ratios:", " ".join(f"{x:.6g}" for x in ratios))
    print("all finite sanity checks passed")

