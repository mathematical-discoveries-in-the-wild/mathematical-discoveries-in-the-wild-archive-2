#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the random-semigroup proof.

The script is numerical evidence only.  It samples a noncommuting discrete
matrix distribution, compares exact and Euler products with exp(t E A), and
checks the first three ordered-product coefficients.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.linalg import expm


RNG = np.random.default_rng(241007417)
X = np.array([1.0, -0.35, 0.6])
T_GRID = np.linspace(0.0, 1.25, 16)


def distribution() -> tuple[np.ndarray, np.ndarray]:
    mats = np.array(
        [
            [[0.20, 0.45, 0.00], [-0.10, -0.15, 0.30], [0.05, 0.00, 0.10]],
            [[-0.25, 0.00, 0.35], [0.40, 0.05, 0.00], [0.00, -0.20, 0.15]],
            [[0.10, -0.30, 0.10], [0.00, 0.25, -0.15], [0.30, 0.10, -0.20]],
        ],
        dtype=float,
    )
    probs = np.array([0.25, 0.45, 0.30])
    return mats, probs


def ordered_coefficients(sample: np.ndarray, max_k: int) -> list[np.ndarray]:
    """Coefficients of prod_i (I + z A_i), in the displayed factor order."""
    dim = sample.shape[1]
    coeff = [np.eye(dim)] + [np.zeros((dim, dim)) for _ in range(max_k)]
    for a in sample:
        for k in range(max_k, 0, -1):
            coeff[k] = coeff[k] + coeff[k - 1] @ a
    return coeff


def product_errors(n: int, trials: int = 180) -> tuple[float, float, list[float]]:
    mats, probs = distribution()
    mean_a = np.tensordot(probs, mats, axes=(0, 0))
    exp_cache = np.array(
        [[[expm(t * a / n) for a in mats] for t in T_GRID]], dtype=float
    )[0]
    euler_cache = np.array(
        [[[np.eye(3) + t * a / n for a in mats] for t in T_GRID]], dtype=float
    )[0]
    target = np.array([expm(t * mean_a) @ X for t in T_GRID])

    exact_sup = []
    replacement_sup = []
    coeff_errors = [[] for _ in range(3)]
    target_coeff = []
    power = np.eye(3)
    for k in range(1, 4):
        power = power @ mean_a
        target_coeff.append((power @ X) / math.factorial(k))

    for _ in range(trials):
        labels = RNG.choice(len(mats), size=n, p=probs)
        exact_vals = []
        euler_vals = []
        for ti in range(len(T_GRID)):
            p_exact = np.eye(3)
            p_euler = np.eye(3)
            for label in labels:
                p_exact = p_exact @ exp_cache[ti, label]
                p_euler = p_euler @ euler_cache[ti, label]
            exact_vals.append(p_exact @ X)
            euler_vals.append(p_euler @ X)
        exact_vals = np.asarray(exact_vals)
        euler_vals = np.asarray(euler_vals)
        exact_sup.append(np.max(np.linalg.norm(exact_vals - target, axis=1)))
        replacement_sup.append(
            np.max(np.linalg.norm(exact_vals - euler_vals, axis=1))
        )

        sample = mats[labels]
        coeff = ordered_coefficients(sample, 3)
        for k in range(1, 4):
            value = (coeff[k] @ X) / (n**k)
            coeff_errors[k - 1].append(np.linalg.norm(value - target_coeff[k - 1]))

    return (
        float(np.mean(exact_sup)),
        float(np.mean(replacement_sup)),
        [float(np.mean(values)) for values in coeff_errors],
    )


def main() -> None:
    mats, _ = distribution()
    rho = max(np.linalg.norm(a, 2) for a in mats)
    print(f"distribution spectral-norm bound rho={rho:.6f}")
    print("n  mean_sup_exact  mean_sup_exact_minus_euler  coeff_L1(k=1,2,3)")
    for n in (4, 8, 16, 32, 64, 128):
        exact, replacement, coeff = product_errors(n)
        coeff_text = " ".join(f"{value:.6e}" for value in coeff)
        print(f"{n:3d}  {exact:.6e}  {replacement:.6e}  {coeff_text}")


if __name__ == "__main__":
    main()
