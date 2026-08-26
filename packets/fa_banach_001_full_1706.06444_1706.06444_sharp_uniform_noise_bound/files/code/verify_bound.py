#!/usr/bin/env python3
"""Finite-dimensional checks for the sharp Q_lambda noise bound."""

from __future__ import annotations

import numpy as np


def positive_half_power(matrix: np.ndarray, exponent: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.power(values, exponent)) @ vectors.T


def sigma_inverse_half(gram: np.ndarray, lam: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(gram)
    if lam == 0.0:
        cutoff = 1.0e-10 * max(1.0, float(values.max()))
        weights = np.zeros_like(values)
        positive = values > cutoff
        weights[positive] = values[positive] ** -0.5
    else:
        weights = (lam + (1.0 - lam) * values) ** -0.5
    return (vectors * weights) @ vectors.T


def reconstruction(
    analysis: np.ndarray, t_basis: np.ndarray, lam: float
) -> np.ndarray:
    gram = analysis @ analysis.T
    weight = sigma_inverse_half(gram, lam)
    weighted_cross = weight @ analysis @ t_basis
    return t_basis @ np.linalg.pinv(weighted_cross) @ weight


def random_checks() -> int:
    rng = np.random.default_rng(170606444)
    checks = 0
    lambdas = (0.0, 1.0e-6, 0.01, 0.2, 0.5, 1.0)

    for _ in range(400):
        r = int(rng.integers(2, 7))
        ambient = r + int(rng.integers(1, 4))
        data_dim = r + int(rng.integers(0, 4))
        t_dim = int(rng.integers(1, r + 1))

        eigs = np.exp(rng.uniform(-3.0, 3.0, size=r))
        eigenvectors, _ = np.linalg.qr(rng.normal(size=(r, r)))
        frame_operator = (
            eigenvectors @ np.diag(eigs) @ eigenvectors.T
        )
        frame_half = positive_half_power(frame_operator, 0.5)

        data_isometry, _ = np.linalg.qr(rng.normal(size=(data_dim, r)))
        projection_u = np.zeros((r, ambient))
        projection_u[:, :r] = np.eye(r)
        analysis = data_isometry @ frame_half @ projection_u

        while True:
            t_basis, _ = np.linalg.qr(rng.normal(size=(ambient, t_dim)))
            angle_cosine = float(
                np.linalg.svd(projection_u @ t_basis, compute_uv=False)[-1]
            )
            if angle_cosine > 0.04:
                break

        lower_bound = float(eigs.min())
        theorem_bound = 1.0 / (np.sqrt(lower_bound) * angle_cosine)

        for lam in lambdas:
            q_lam = reconstruction(analysis, t_basis, lam)
            q_norm = float(np.linalg.norm(q_lam, 2))
            left_inverse_error = float(
                np.linalg.norm(q_lam @ analysis @ t_basis - t_basis, 2)
            )
            assert left_inverse_error < 2.0e-7
            assert q_norm <= theorem_bound * (1.0 + 2.0e-7)
            checks += 1
    return checks


def sharpness_checks() -> int:
    checks = 0
    for lower, upper, cosine in (
        (0.2, 4.0, 0.17),
        (1.0, 1.0, 1.0),
        (2.5, 11.0, 0.73),
    ):
        analysis = np.array(
            [[np.sqrt(lower), 0.0, 0.0], [0.0, np.sqrt(upper), 0.0]]
        )
        t = np.array(
            [[cosine], [0.0], [np.sqrt(max(0.0, 1.0 - cosine**2))]]
        )
        expected = 1.0 / (np.sqrt(lower) * cosine)
        for lam in (0.0, 1.0e-8, 0.03, 0.4, 1.0):
            q_lam = reconstruction(analysis, t, lam)
            assert abs(float(np.linalg.norm(q_lam, 2)) - expected) < 2.0e-9
            checks += 1
    return checks


def main() -> None:
    random_count = random_checks()
    sharp_count = sharpness_checks()
    print(f"verified {random_count} random inequalities")
    print(f"verified {sharp_count} exact sharpness instances")


if __name__ == "__main__":
    main()
