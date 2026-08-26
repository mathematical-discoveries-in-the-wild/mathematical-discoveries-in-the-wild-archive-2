#!/usr/bin/env python3
"""Numerical checks for the weighted-Welch solution of arXiv:2002.03974.

The random checks validate the successive inequalities used in the proof.
The explicit harmonic constructions validate sharpness.  The optional global
search is only a finite-dimensional sanity check and is not proof.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def harmonic_untf(d: int, n_vectors: int) -> np.ndarray:
    """Return N unit vectors in R^d forming a UNTF, as an N-by-d array."""
    if not 1 <= d <= n_vectors:
        raise ValueError("need 1 <= d <= N")
    if d == n_vectors:
        return np.eye(d)

    grid = np.arange(n_vectors, dtype=float)
    rows: list[np.ndarray] = []
    if d % 2:
        rows.append(np.ones(n_vectors) / math.sqrt(n_vectors))
        pair_count = (d - 1) // 2
    else:
        pair_count = d // 2

    for frequency in range(1, pair_count + 1):
        phase = 2.0 * math.pi * frequency * grid / n_vectors
        rows.append(math.sqrt(2.0 / n_vectors) * np.cos(phase))
        rows.append(math.sqrt(2.0 / n_vectors) * np.sin(phase))

    synthesis_rows = np.stack(rows, axis=0)
    unit_vectors = math.sqrt(n_vectors / d) * synthesis_rows.T
    np.testing.assert_allclose(
        np.linalg.norm(unit_vectors, axis=1), 1.0, atol=2e-12
    )
    np.testing.assert_allclose(
        unit_vectors.T @ unit_vectors,
        (n_vectors / d) * np.eye(d),
        atol=2e-12,
    )
    return unit_vectors


def clipped_optimal_norm_squared(
    d: int, n_vectors: int, c1: float, c2: float, sigma: float
) -> float:
    if n_vectors == d:
        return c2
    alpha = (n_vectors - d) / d
    return float(np.clip(sigma / math.sqrt(alpha), c1, c2))


def reciprocal_sinrs(
    unit_vectors: np.ndarray, norm_squares: np.ndarray, sigma: float
) -> np.ndarray:
    gram_cosine_squared = (unit_vectors @ unit_vectors.T) ** 2
    return sigma**2 / norm_squares + gram_cosine_squared @ norm_squares - norm_squares


def check_random_chain(seed: int = 200203974, trials_per_case: int = 20_000) -> int:
    rng = np.random.default_rng(seed)
    cases = [(2, 3), (2, 7), (3, 3), (3, 5), (4, 9), (7, 11)]
    checked = 0

    for d, n_vectors in cases:
        alpha = (n_vectors - d) / d
        for _ in range(trials_per_case):
            c1 = float(np.exp(rng.uniform(-1.5, 0.5)))
            c2 = float(c1 * np.exp(rng.uniform(0.01, 2.0)))
            sigma = float(np.exp(rng.uniform(-3.0, 3.0)))
            if rng.random() < 0.03:
                sigma = 0.0

            norm_squares = rng.uniform(c1, c2, size=n_vectors)
            unit_vectors = rng.normal(size=(n_vectors, d))
            unit_vectors /= np.linalg.norm(unit_vectors, axis=1, keepdims=True)
            values = reciprocal_sinrs(unit_vectors, norm_squares, sigma)
            x = 1.0 / norm_squares
            x_bar = float(np.mean(x))

            maximum = float(np.max(values))
            weighted_average = float(np.dot(x, values) / np.sum(x))
            welch_stage = float(
                (sigma**2 * np.dot(x, x) + n_vectors * alpha) / np.sum(x)
            )
            cauchy_stage = float(
                sigma**2 * x_bar + (alpha / x_bar if alpha else 0.0)
            )
            c_star = clipped_optimal_norm_squared(d, n_vectors, c1, c2, sigma)
            optimum = float(sigma**2 / c_star + alpha * c_star)

            scale = 1.0 + abs(maximum) + abs(optimum)
            tolerance = 2e-11 * scale
            assert maximum + tolerance >= weighted_average
            assert weighted_average + tolerance >= welch_stage
            assert welch_stage + tolerance >= cauchy_stage
            assert cauchy_stage + tolerance >= optimum
            checked += 1
    return checked


def check_sharpness() -> int:
    checked = 0
    for d, n_vectors in [
        (2, 3),
        (2, 8),
        (3, 4),
        (3, 9),
        (4, 7),
        (5, 8),
        (6, 10),
        (7, 13),
    ]:
        unit_vectors = harmonic_untf(d, n_vectors)
        alpha = (n_vectors - d) / d
        c1, c2 = 0.7, 5.3
        threshold_low = c1 * math.sqrt(alpha)
        threshold_high = c2 * math.sqrt(alpha)
        for sigma in [0.0, 0.4 * threshold_low, threshold_low, 0.7 * threshold_high,
                      threshold_high, 2.0 * threshold_high]:
            c_star = clipped_optimal_norm_squared(d, n_vectors, c1, c2, sigma)
            norm_squares = np.full(n_vectors, c_star)
            maximum = float(
                np.max(reciprocal_sinrs(unit_vectors, norm_squares, sigma))
            )
            optimum = sigma**2 / c_star + alpha * c_star
            np.testing.assert_allclose(maximum, optimum, rtol=2e-12, atol=2e-12)
            checked += 1
    return checked


def run_global_search() -> None:
    from scipy.optimize import differential_evolution

    c1, c2 = 1.0, 4.0
    for n_vectors in (3, 4, 5):
        d = 2
        alpha = (n_vectors - d) / d
        for sigma_squared in (0.1, 1.0, 4.0, 16.0):
            sigma = math.sqrt(sigma_squared)

            def target(parameters: np.ndarray) -> float:
                norm_squares = parameters[:n_vectors]
                angles = parameters[n_vectors:]
                unit_vectors = np.column_stack((np.cos(angles), np.sin(angles)))
                return float(
                    np.max(reciprocal_sinrs(unit_vectors, norm_squares, sigma))
                )

            result = differential_evolution(
                target,
                [(c1, c2)] * n_vectors + [(0.0, math.pi)] * n_vectors,
                seed=10_000 + 100 * n_vectors + int(10 * sigma_squared),
                popsize=12,
                maxiter=700,
                tol=1e-8,
                polish=True,
            )
            c_star = clipped_optimal_norm_squared(d, n_vectors, c1, c2, sigma)
            optimum = sigma_squared / c_star + alpha * c_star
            # Differential evolution gives an upper approximation to the minimum.
            assert result.fun >= optimum - 2e-6
            assert result.fun <= optimum + 6e-3
            print(
                f"global d={d} N={n_vectors} sigma^2={sigma_squared:g}: "
                f"numerical={result.fun:.9f}, theorem={optimum:.9f}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-search", action="store_true")
    args = parser.parse_args()

    random_count = check_random_chain()
    sharp_count = check_sharpness()
    print(f"random inequality chains checked: {random_count}")
    print(f"sharp UNTF parameter cases checked: {sharp_count}")
    if args.global_search:
        run_global_search()
    print("all checks passed")


if __name__ == "__main__":
    main()

