"""Numerical regression for the Bernoulli subgaussian-diameter formulas.

This script is not used as proof. It maximizes the exact moment-generating
function quotient for several Bernoulli masses.
"""

from __future__ import annotations

import math

from scipy.optimize import minimize_scalar


def mgf(p: float, s: float) -> float:
    q = 2.0 * p * (1.0 - p)
    return 1.0 + q * (math.cosh(s) - 1.0)


def quotient(p: float, s: float) -> float:
    return 2.0 * math.log(mgf(p, s)) / (s * s)


def delta_squared(p: float) -> tuple[float, float]:
    upper = max(12.0, 4.0 * math.log(1.0 / p))
    result = minimize_scalar(
        lambda s: -quotient(p, s),
        bounds=(1.0e-7, upper),
        method="bounded",
        options={"xatol": 1.0e-13},
    )
    return -result.fun, result.x


def main() -> None:
    explicit_rhs = 2.0 * math.exp(-0.81)
    print(f"uniform exact delta^2 = 0.5; RHS at t=0.45 = {explicit_rhs:.12f}")
    assert explicit_rhs < 1.0

    for p in (1.0e-1, 1.0e-2, 1.0e-4, 1.0e-8):
        delta2, maximizer = delta_squared(p)
        scaled = math.log(1.0 / p) * delta2
        print(
            f"p={p:.0e}  maximizer={maximizer:.10f}  "
            f"delta^2={delta2:.12f}  log(1/p)*delta^2={scaled:.12f}"
        )


if __name__ == "__main__":
    main()
