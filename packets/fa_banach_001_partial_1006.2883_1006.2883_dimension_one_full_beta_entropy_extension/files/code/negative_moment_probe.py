"""Numerically probe normalized negative-moment log-concavity.

For a positive convex function on R^n, sublevel volumes have the form
V(t)=v(t)^n with v concave.  The source's missing beta range would follow if
prod_{j=1}^n(p-j) * int phi^{-p} were log-concave for all p>n.

This script samples nonnegative concave piecewise-linear v and estimates the
second derivative of the logarithm in the strip n<p<n+1.  It is only a
counterexample search, not a proof.
"""

from __future__ import annotations

import math
import random

import numpy as np


def make_concave_profile(rng: random.Random, pieces: int = 5):
    knots = [1.0]
    for _ in range(pieces):
        knots.append(knots[-1] + rng.uniform(0.15, 3.0))
    slopes = sorted(
        (10 ** rng.uniform(-2.0, 1.0) for _ in range(pieces + 1)), reverse=True
    )
    base = 10 ** rng.uniform(-3.0, 0.8)
    values = [base]
    for j in range(pieces):
        values.append(values[-1] + slopes[j] * (knots[j + 1] - knots[j]))

    def v(t: float) -> float:
        if t <= knots[0]:
            return base
        for j in range(pieces):
            if t <= knots[j + 1]:
                return values[j] + slopes[j] * (t - knots[j])
        return values[-1] + slopes[-1] * (t - knots[-1])

    return v, (knots, slopes, base)


def normalized_moment(n: int, p: float, params) -> float:
    # Exact piecewise-polynomial evaluation of
    # int phi^{-p} = p int_1^infty v(t)^n t^{-p-1} dt.
    knots, slopes, base = params
    value = base
    integral = 0.0
    for j, (left, right) in enumerate(zip(knots[:-1], knots[1:])):
        slope = slopes[j]
        intercept = value - slope * left
        for k in range(n + 1):
            coefficient = math.comb(n, k) * slope**k * intercept ** (n - k)
            integral += (
                p
                * coefficient
                * (right ** (k - p) - left ** (k - p))
                / (k - p)
            )
        value += slope * (right - left)
    # Integrate the final affine ray exactly; p>n ensures convergence.
    left = knots[-1]
    slope = slopes[-1]
    intercept = value - slope * left
    for k in range(n + 1):
        coefficient = math.comb(n, k) * slope**k * intercept ** (n - k)
        integral += p * coefficient * left ** (k - p) / (p - k)
    factor = math.prod(p - j for j in range(1, n + 1))
    return factor * integral


def main() -> None:
    rng = random.Random(1807)
    worst = (-math.inf, None)
    for n in (2, 3, 4):
        for trial in range(600):
            _, params = make_concave_profile(rng)
            for p in np.linspace(n + 0.035, n + 0.965, 25):
                h = 2e-3
                vals = [
                    math.log(normalized_moment(n, p + d, params))
                    for d in (-h, 0.0, h)
                ]
                second = (vals[0] - 2.0 * vals[1] + vals[2]) / h**2
                if second > worst[0]:
                    worst = (second, (n, trial, p, params))
                if second > 2e-4:
                    print("candidate failure", second, n, trial, p, params)
                    return
    print("no failure; largest estimated log-second-derivative", worst)


if __name__ == "__main__":
    main()
