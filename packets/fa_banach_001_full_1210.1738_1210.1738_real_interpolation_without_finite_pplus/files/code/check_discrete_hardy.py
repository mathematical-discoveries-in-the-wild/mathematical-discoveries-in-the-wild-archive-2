#!/usr/bin/env python3
"""Finite sanity checks for the discrete Hardy identities in the packet.

This is not a proof.  It checks the algebraic formulas and records empirical
operator-norm ratios for random positive finite sequences.
"""

from __future__ import annotations

import argparse
import math
import random


def ell_norm(values: list[float], exponent: float) -> float:
    if math.isinf(exponent):
        return max(values, default=0.0)
    return sum(value**exponent for value in values) ** (1.0 / exponent)


def finite_r_transform(c: list[float], theta: float, r: float) -> list[float]:
    s = r / (1.0 - theta)
    decay = r * theta / (1.0 - theta)
    return [
        sum(2.0 ** (-j * decay) * c[m + j] ** s for j in range(len(c) - m))
        ** (1.0 / s)
        for m in range(len(c))
    ]


def infinity_r_transform(c: list[float], theta: float) -> list[float]:
    return [
        max(2.0 ** (-j * theta) * c[m + j] for j in range(len(c) - m))
        for m in range(len(c))
    ]


def direct_tail_identity(
    h: list[float], theta: float, r: float
) -> tuple[list[float], list[float]]:
    """Return the two sides of 2^m D_m^(1-theta)=T(c)_m."""
    c = [2.0**m * h[m] ** (1.0 - theta) for m in range(len(h))]
    left: list[float] = []
    if math.isinf(r):
        for m in range(len(h)):
            a_m = max(2.0**n * h[n] for n in range(m, len(h)))
            d_m = 2.0 ** (-m) * a_m
            left.append(2.0**m * d_m ** (1.0 - theta))
        right = infinity_r_transform(c, theta)
    else:
        for m in range(len(h)):
            a_m = sum((2.0**n * h[n]) ** r for n in range(m, len(h))) ** (1.0 / r)
            d_m = 2.0 ** (-m) * a_m
            left.append(2.0**m * d_m ** (1.0 - theta))
        right = finite_r_transform(c, theta, r)
    return left, right


def run(trials: int, length: int, seed: int) -> None:
    rng = random.Random(seed)
    worst_identity_error = 0.0
    worst_ratio = 0.0
    for _ in range(trials):
        # Keep powers inside ordinary double precision; the identities are
        # algebraic, so extreme overflow regimes add no useful check here.
        theta = rng.uniform(0.10, 0.75)
        q = 10 ** rng.uniform(-0.5, 0.7)
        # Log sampling exercises both the quasi-Banach range r<1 and the
        # locally convex range r>=1.
        r = math.inf if rng.random() < 0.25 else 10 ** rng.uniform(-0.8, 0.6)
        h = [10 ** rng.uniform(-2.0, 2.0) for _ in range(length)]
        left, right = direct_tail_identity(h, theta, r)
        for x, y in zip(left, right):
            worst_identity_error = max(
                worst_identity_error, abs(x - y) / max(1.0, abs(x), abs(y))
            )
        c = [2.0**m * h[m] ** (1.0 - theta) for m in range(length)]
        transformed = (
            infinity_r_transform(c, theta)
            if math.isinf(r)
            else finite_r_transform(c, theta, r)
        )
        denominator = ell_norm(c, q)
        if denominator:
            worst_ratio = max(worst_ratio, ell_norm(transformed, q) / denominator)

    print(f"trials={trials} length={length} seed={seed}")
    print(f"worst_relative_identity_error={worst_identity_error:.3e}")
    print(f"largest_observed_operator_ratio={worst_ratio:.6f}")
    if worst_identity_error > 1e-10:
        raise SystemExit("tail identity check failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=2000)
    parser.add_argument("--length", type=int, default=24)
    parser.add_argument("--seed", type=int, default=12101738)
    args = parser.parse_args()
    run(args.trials, args.length, args.seed)
