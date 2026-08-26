#!/usr/bin/env python3
"""Numerical checks for the 2006.04901 condition-number packet.

These tests are sanity checks only; the packet contains exact proofs.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def gram(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=complex)
    weights = np.sqrt(1.0 - np.abs(z) ** 2)
    return weights[:, None] * weights[None, :] / (
        1.0 - np.conjugate(z[:, None]) * z[None, :]
    )


def optimized_eta(g: np.ndarray) -> tuple[float, np.ndarray]:
    n = len(g)

    def objective(x: np.ndarray) -> float:
        logs = np.r_[x, -x.sum()]
        d = np.exp(logs)
        eigenvalues = np.linalg.eigvalsh(d[:, None] * g * d[None, :])
        return float(np.log(eigenvalues[-1] / eigenvalues[0]))

    result = minimize(objective, np.zeros(n - 1), method="BFGS", tol=1e-12)
    logs = np.r_[result.x, -result.x.sum()]
    return float(np.exp(result.fun / 2.0)), logs


def check_regular_polygons() -> None:
    for n in range(2, 9):
        omega = np.exp(2j * np.pi * np.arange(n) / n)
        for radius in (0.2, 0.5, 0.8):
            g = gram(radius * omega)
            eta, logs = optimized_eta(g)
            expected = radius ** (-(n - 1))
            relative_error = abs(eta / expected - 1.0)
            tolerance = 3e-6 if expected > 1e4 else 1e-8
            assert relative_error < tolerance, (n, radius, eta, expected)
            assert np.linalg.norm(logs) < 2e-3, (n, radius, logs)


def check_two_point_formula() -> None:
    rng = np.random.default_rng(20260812)
    for _ in range(100):
        radii = np.sqrt(rng.uniform(0.01, 0.95, 2))
        z = radii * np.exp(2j * np.pi * rng.random(2))
        rho = abs((z[0] - z[1]) / (1.0 - np.conjugate(z[0]) * z[1]))
        c = np.sqrt(1.0 - rho**2)
        expected = (1.0 + c) / rho
        eta, _ = optimized_eta(gram(z))
        assert abs(eta / expected - 1.0) < 1e-9


def check_automorphism_invariance() -> None:
    rng = np.random.default_rng(314159)
    for n in range(2, 8):
        z = np.sqrt(rng.uniform(0.02, 0.9, n)) * np.exp(
            2j * np.pi * rng.random(n)
        )
        a = np.sqrt(rng.uniform(0.02, 0.8)) * np.exp(2j * np.pi * rng.random())
        transformed = (z - a) / (1.0 - np.conjugate(a) * z)
        eta_before, _ = optimized_eta(gram(z))
        eta_after, _ = optimized_eta(gram(transformed))
        assert abs(eta_before / eta_after - 1.0) < 2e-7


def check_generic_scaling_is_nontrivial() -> None:
    z = np.array(
        [
            0.73 * np.exp(0.2j),
            0.31 * np.exp(2.1j),
            0.88 * np.exp(3.7j),
            0.52 * np.exp(5.4j),
            0.18 * np.exp(4.6j),
        ]
    )
    g = gram(z)
    raw = np.sqrt(np.linalg.cond(g))
    optimized, logs = optimized_eta(g)
    assert optimized < raw - 1e-4
    assert np.linalg.norm(logs) > 1e-3


if __name__ == "__main__":
    check_regular_polygons()
    check_two_point_formula()
    check_automorphism_invariance()
    check_generic_scaling_is_nontrivial()
    print("all condition-number checks passed")
