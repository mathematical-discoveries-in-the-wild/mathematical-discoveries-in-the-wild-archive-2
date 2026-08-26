#!/usr/bin/env python3
"""Finite-grid check of the OU truncation formulas; not part of the proof."""

from __future__ import annotations

import math

import numpy as np
from scipy.special import ndtr


def phi(z: np.ndarray | float) -> np.ndarray | float:
    return np.exp(-0.5 * np.asarray(z) ** 2) / math.sqrt(2.0 * math.pi)


def clipped_moments(mean: np.ndarray, sigma: float, radius: float):
    """Return E[clip(Y)] and E[clip(Y)^2] for Y~N(mean,sigma^2)."""
    zlo = (-radius - mean) / sigma
    zhi = (radius - mean) / sigma
    prob = ndtr(zhi) - ndtr(zlo)
    first_mid = mean * prob + sigma * (phi(zlo) - phi(zhi))
    second_mid = (
        mean**2 * prob
        + 2.0 * mean * sigma * (phi(zlo) - phi(zhi))
        + sigma**2 * (prob + zlo * phi(zlo) - zhi * phi(zhi))
    )
    lower = ndtr(zlo)
    upper = 1.0 - ndtr(zhi)
    first = first_mid + radius * (upper - lower)
    second = second_mid + radius**2 * (upper + lower)
    return first, second


def ou_moments(t: float, x: np.ndarray, radius: float):
    mean = math.exp(-t) * x
    sigma = math.sqrt(1.0 - math.exp(-2.0 * t))
    return clipped_moments(mean, sigma, radius)


def main() -> None:
    radii = [2.0, 4.0, 8.0, 16.0, 32.0]
    times = np.geomspace(1.0e-4, 8.0, 240)
    fixed_t = math.log(2.0)
    print("R   sampled_sup_bmo   |(T_t-T_2t)f_R(R)|   quotient_by_R")
    for radius in radii:
        xs = np.linspace(-1.5 * radius, 1.5 * radius, 601)
        max_variance = 0.0
        for t in times:
            first, second = ou_moments(t, xs, radius)
            max_variance = max(max_variance, float(np.max(second - first**2)))
        t1, _ = ou_moments(fixed_t, np.asarray([radius]), radius)
        t2, _ = ou_moments(2.0 * fixed_t, np.asarray([radius]), radius)
        drift = float(abs(t1[0] - t2[0]))
        assert max_variance <= 1.0 + 2.0e-10
        print(f"{radius:2.0f}  {math.sqrt(max_variance):16.10f}"
              f"  {drift:22.10f}  {drift/radius:13.10f}")


if __name__ == "__main__":
    main()
