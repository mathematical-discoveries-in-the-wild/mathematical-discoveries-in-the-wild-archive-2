#!/usr/bin/env python3
"""Numerical checks for the tangential-double-arc Lipschitz derivative example."""

from __future__ import annotations

import argparse
import numpy as np


def branch_slope(alpha: float, t: np.ndarray) -> np.ndarray:
    return alpha * t ** (alpha - 1) / np.sqrt(
        1 + alpha**2 * t ** (2 * alpha - 2)
    )


def radial_ratio(alpha: float, t: np.ndarray) -> np.ndarray:
    return t**alpha / np.sqrt(t**2 + t ** (2 * alpha))


def verify(alpha: float) -> None:
    assert alpha > 1
    t = 10.0 ** (-np.arange(1, 10, dtype=float))
    slopes = branch_slope(alpha, t)
    radial = radial_ratio(alpha, t)

    # Opposite points (t,+t^alpha), (t,-t^alpha): both differences are 2t^alpha.
    cross_ratio = (2 * t**alpha) / (2 * t**alpha)

    # Every path in the double arc joining opposite points passes through the origin.
    # Its length is at least 2t, whereas the ambient chord has length 2t^alpha.
    path_distortion_lower = t ** (1 - alpha)

    # Independent centered finite-difference check on the upper branch.
    sample_t = np.array([0.2, 0.08, 0.03], dtype=float)
    h = 1e-7
    dy = (sample_t + h) ** alpha - (sample_t - h) ** alpha
    dx = np.sqrt((2 * h) ** 2 + dy**2)
    finite_difference_slope = np.abs(dy) / dx
    closed_slope = branch_slope(alpha, sample_t)

    assert np.allclose(cross_ratio, 1.0, atol=1e-14)
    assert radial[-1] < radial[0]
    assert slopes[-1] < slopes[0]
    assert radial[-1] < 1e-4
    assert slopes[-1] < 1e-3
    assert path_distortion_lower[-1] > path_distortion_lower[0]
    assert np.allclose(finite_difference_slope, closed_slope, rtol=2e-7, atol=2e-10)

    print(f"PASS alpha={alpha:g}")
    print(f"  radial ratio at t=1e-9: {radial[-1]:.6e}")
    print(f"  branch slope at t=1e-9: {slopes[-1]:.6e}")
    print(f"  cross-branch quotient: {cross_ratio[-1]:.12g}")
    print(f"  path/chord lower bound at t=1e-9: {path_distortion_lower[-1]:.6e}")
    print(f"  max finite-difference slope error: {np.max(abs(finite_difference_slope-closed_slope)):.3e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=float)
    parser.add_argument("--suite", action="store_true")
    args = parser.parse_args()
    values = (1.5, 2.0, 3.0) if args.suite or args.alpha is None else (args.alpha,)
    for value in values:
        verify(value)
    print("VERDICT: PASS")
