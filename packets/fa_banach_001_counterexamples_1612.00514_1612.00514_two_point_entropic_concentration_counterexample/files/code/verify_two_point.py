#!/usr/bin/env python3
"""Numerical regression for the analytic two-point counterexample.

This script is not part of the proof. It independently evaluates the exact
one-dimensional entropic-transport integral and the pointwise curvature
formula for representative p.
"""

import math

import numpy as np
from scipy.integrate import quad


def logit_difference(m: float, p: float) -> float:
    q = 1.0 - p
    return math.log(m * q / (p * (1.0 - m)))


def metric_integrand(m: float, p: float) -> float:
    if abs(m - p) <= 1e-10 * max(p, 1.0 - p):
        return 1.0 / math.sqrt(p * (1.0 - p))
    return math.sqrt(logit_difference(m, p) / (m - p))


def diameter(p: float) -> float:
    value, error = quad(
        lambda m: metric_integrand(m, p),
        0.0,
        1.0,
        points=[p],
        epsabs=2e-11,
        epsrel=2e-11,
        limit=800,
    )
    assert error < 2e-7
    return value


def curvature(m: float, p: float) -> float:
    if abs(m - p) <= 1e-9 * max(p, 1.0 - p):
        # K(p)=p(1-p), so the limiting formula is 1.
        return 1.0
    ell = logit_difference(m, p)
    K = (m - p) / ell
    return 0.5 * (1.0 + K / (m * (1.0 - m)))


def main() -> None:
    probabilities = [0.25, 0.1, 0.01, 1e-4, 1e-6, 1e-8]
    previous_rho2 = -1.0
    for p in probabilities:
        D = diameter(p)
        L = math.log(1.0 / p)
        rho2 = (L / D) ** 2
        ratio = D * D / L
        grid = np.concatenate(
            [
                np.geomspace(max(p * 1e-7, 1e-15), p * 0.999, 400),
                np.linspace(p * 1.001, 1.0 - 1e-8, 1200),
            ]
        )
        kmin = min(curvature(float(m), p) for m in grid if 0.0 < m < 1.0)
        assert ratio < 49.0
        assert kmin >= 0.5 - 1e-11
        assert rho2 > previous_rho2
        previous_rho2 = rho2
        print(
            f"p={p:.0e} D={D:.10f} D^2/log(1/p)={ratio:.10f} "
            f"rho^2={rho2:.10f} min_curvature={kmin:.10f}"
        )

    # Literal-exponent scaling audit for p=1/4: lambda_s rho_s^2 -> 0.
    p = 0.25
    D = diameter(p)
    L = math.log(1.0 / p)
    values = []
    for s in [1.0, 1e-2, 1e-4, 1e-6]:
        lambda_s = s
        rho_s = math.sqrt(s) * L / D
        values.append(lambda_s * rho_s * rho_s)
    assert all(values[i + 1] < values[i] for i in range(len(values) - 1))
    print("literal scaling lambda_s*rho_s^2:", values)
    print("PASS")


if __name__ == "__main__":
    main()
