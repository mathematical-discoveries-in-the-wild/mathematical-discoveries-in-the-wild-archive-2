"""Numerical sanity checks for the complex endpoint norm packet.

This script is not part of the proof.  It checks two explicit lower-bound
families against the claimed constant for several complex orders.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad
from scipy.special import gamma


def claimed_square_endpoint_norm(xi: complex) -> float:
    return 1.0 / (xi.real * abs(gamma(xi)))


def l1_concentrating_ratio(xi: complex, eps: float) -> float:
    """L1 norm of V_xi(eps^{-1} 1_[0,eps])."""

    denom = eps * gamma(xi + 1.0)

    def value(x: float) -> complex:
        if x <= eps:
            return x**xi / denom
        return (x**xi - (x - eps) ** xi) / denom

    left = quad(lambda x: abs(value(x)), 0.0, eps, epsabs=2e-11, limit=400)[0]
    right = quad(lambda x: abs(value(x)), eps, 1.0, epsabs=2e-11, limit=400)[0]
    return left + right


def triangular_cutoff(u: float, delta: float) -> float:
    """Continuous cutoff: zero at endpoints, one on [2d,1-2d]."""

    if u <= delta or u >= 1.0 - delta:
        return 0.0
    if u < 2.0 * delta:
        return (u - delta) / delta
    if u > 1.0 - 2.0 * delta:
        return (1.0 - delta - u) / delta
    return 1.0


def c0_phase_cutoff_value(xi: complex, delta: float) -> float:
    """Value at x=1 after phase alignment with a continuous cutoff."""

    tau = xi.real
    integral = quad(
        lambda u: (1.0 - u) ** (tau - 1.0) * triangular_cutoff(u, delta),
        delta,
        1.0 - delta,
        epsabs=2e-11,
        limit=400,
    )[0]
    return integral / abs(gamma(xi))


def lp_to_c0_formula(xi: complex, p: float) -> float:
    tau = xi.real
    if np.isinf(p):
        p_conj = 1.0
    else:
        p_conj = p / (p - 1.0)
    return 1.0 / (
        abs(gamma(xi)) * (((tau - 1.0) * p_conj + 1.0) ** (1.0 / p_conj))
    )


def main() -> None:
    orders = [0.35 + 1.2j, 1.0 + 2.5j, 2.2 - 0.7j]
    epsilons = [0.20, 0.08, 0.03, 0.01]

    for xi in orders:
        target = claimed_square_endpoint_norm(xi)
        l1_values = [l1_concentrating_ratio(xi, eps) for eps in epsilons]
        c0_values = [c0_phase_cutoff_value(xi, eps) for eps in epsilons]
        print(f"xi={xi}, target={target:.10f}")
        print("  L1 concentration:", [f"{v:.10f}" for v in l1_values])
        print("  C0 phase cutoffs:", [f"{v:.10f}" for v in c0_values])
        assert l1_values[-1] <= target * (1.0 + 2e-7)
        assert c0_values[-1] <= target * (1.0 + 2e-7)
        assert l1_values[-1] > 0.70 * target
        assert c0_values[-1] > 0.70 * target

    xi = 0.8 + 0.9j
    p = 2.0
    numeric_row_norm = quad(
        lambda u: abs((1.0 - u) ** (xi - 1.0) / gamma(xi)) ** 2,
        0.0,
        1.0,
        epsabs=2e-11,
        limit=400,
    )[0] ** 0.5
    formula = lp_to_c0_formula(xi, p)
    print(f"Lp->C0 row check: numeric={numeric_row_norm:.10f}, formula={formula:.10f}")
    assert abs(numeric_row_norm - formula) < 2e-9


if __name__ == "__main__":
    main()
