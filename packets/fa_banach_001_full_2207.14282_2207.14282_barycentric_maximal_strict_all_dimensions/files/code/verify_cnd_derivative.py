#!/usr/bin/env python3
"""Checks for the dimension-free barycentric/maximal strict inequality.

The proof is analytic.  This script checks the scalar kernel identities,
finite Schoenberg embeddings, the double-commutator trace identity, and the
strict derivative sign on random positive matrices.
"""

from __future__ import annotations

import math

import numpy as np


def lambda_kernel(alpha: float, differences: np.ndarray) -> np.ndarray:
    beta = 1.0 - alpha
    out = np.ones_like(differences, dtype=float)
    mask = np.abs(differences) > 1e-7
    x = differences[mask]
    out[mask] = (
        alpha
        * beta
        * x
        * np.sinh(x / 2.0)
        / (2.0 * np.sinh(alpha * x / 2.0) * np.sinh(beta * x / 2.0))
    )
    return out


def h_minus_one(x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(x, dtype=float)
    mask = np.abs(x) > 1e-7
    y = x[mask]
    out[mask] = (y / 2.0) / np.tanh(y / 2.0) - 1.0
    return out


def schoenberg_coordinates(psi: np.ndarray) -> np.ndarray:
    d = psi.shape[0]
    j = np.eye(d) - np.ones((d, d)) / d
    gram = -(j @ psi @ j) / 2.0
    vals, vecs = np.linalg.eigh((gram + gram.T) / 2.0)
    assert vals.min() > -2e-8
    positive = vals > 1e-10
    return vecs[:, positive] * np.sqrt(vals[positive])


def check_scalar_identities() -> None:
    grid = np.linspace(-15.0, 15.0, 3001)
    for alpha in (0.03, 0.1, 0.25, 0.5, 0.8, 0.97):
        beta = 1.0 - alpha
        psi = lambda_kernel(alpha, grid) - 1.0
        decomposition = beta * h_minus_one(alpha * grid) + alpha * h_minus_one(beta * grid)
        assert np.max(np.abs(psi - decomposition)) < 2e-10

    # Partial fractions for h(x)-1; the tail is O(x^2/N).
    test = np.linspace(-12.0, 12.0, 241)
    n = np.arange(1, 20001, dtype=float)
    series = np.array(
        [2.0 * np.sum(x * x / (x * x + 4.0 * math.pi**2 * n * n)) for x in test]
    )
    assert np.max(np.abs(series - h_minus_one(test))) < 4e-4


def check_random_derivatives() -> None:
    rng = np.random.default_rng(20260817)
    checked = 0
    for d in range(2, 13):
        for alpha in (0.04, 0.15, 0.37, 0.5, 0.79, 0.96):
            for _ in range(80):
                z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
                s = z @ z.conj().T + 0.3 * np.eye(d)
                x = np.sort(rng.normal(size=d) * 3.0)
                differences = x[:, None] - x[None, :]
                lam = lambda_kernel(alpha, differences)
                psi = lam - 1.0

                inv_s = np.linalg.inv(s)
                source_derivative = -1.0 + np.sum(s * inv_s.T * lam).real / d

                coords = schoenberg_coordinates(psi)
                reconstructed = np.sum((coords[:, None, :] - coords[None, :, :]) ** 2, axis=2)
                assert np.max(np.abs(reconstructed - psi)) < 2e-7

                double_commutator_sum = 0.0
                for column in range(coords.shape[1]):
                    v = np.diag(coords[:, column])
                    comm2 = v @ (v @ s - s @ v) - (v @ s - s @ v) @ v
                    double_commutator_sum += np.trace(inv_s @ comm2).real

                assert abs(d * source_derivative - double_commutator_sum) < 2e-6
                assert source_derivative < -1e-10
                checked += 1

    # If S is diagonal in the lambda basis, the pair commutes and the
    # derivative is exactly zero (up to floating-point error).
    for d in range(2, 20):
        s = np.diag(np.linspace(1.0, 2.0, d))
        x = np.linspace(-2.0, 2.0, d)
        lam = lambda_kernel(0.37, x[:, None] - x[None, :])
        derivative = -1.0 + np.sum(s * np.linalg.inv(s).T * lam).real / d
        assert abs(derivative) < 2e-14

    print(f"random strict derivative checks passed: {checked}")


if __name__ == "__main__":
    check_scalar_identities()
    check_random_derivatives()
    print("hyperbolic decomposition and partial-fraction checks passed")
    print("Schoenberg distance and double-commutator identities passed")

