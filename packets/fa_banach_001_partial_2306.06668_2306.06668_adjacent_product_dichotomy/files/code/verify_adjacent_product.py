#!/usr/bin/env python3
"""Deterministic sanity checks for the adjacent-product packet.

The proof is analytic.  This script checks the finite-q inequalities on
Schwartz test functions, the arbitrary-gap q=1 identity, and the growth
mechanism in the phase-plane endpoint construction.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.special import eval_hermitenorm


def gaussian_derivative(x: np.ndarray, center: float, scale: float, n: int) -> np.ndarray:
    z = scale * (x - center)
    return ((-1) ** n) * scale**n * eval_hermitenorm(n, z) * np.exp(-0.5 * z * z)


def test_derivative(x: np.ndarray, n: int) -> np.ndarray:
    terms = [
        (1.0, -1.1, 0.8),
        (-0.65, 0.35, 1.25),
        (0.4, 1.55, 0.95),
    ]
    return sum(weight * gaussian_derivative(x, center, scale, n) for weight, center, scale in terms)


def lp_norm(values: np.ndarray, x: np.ndarray, p: float) -> float:
    return float(np.trapz(np.abs(values) ** p, x) ** (1.0 / p))


def finite_q_checks() -> None:
    x = np.linspace(-14.0, 14.0, 240_001)
    cases = [
        (1, 1, 0, 1.0),
        (1, 1, 3, 2.0),
        (2, 1, 2, 1.5),
        (3, 2, 1, 2.25),
        (4, 2, 4, 3.0),
    ]
    print("finite-q adjacent checks")
    for j, a, b, q in cases:
        kappa = 2 * a + b
        p = q * kappa
        low = test_derivative(x, j - 1)
        mid = test_derivative(x, j)
        high = test_derivative(x, j + 1)
        product = low**a * mid**b * high**a
        lhs = lp_norm(mid, x, p)
        rhs = (p - 1.0) ** (a / kappa) * lp_norm(product, x, q) ** (1.0 / kappa)
        ratio = lhs / rhs
        print(f"  j={j} a={a} b={b} q={q:g}: lhs/rhs={ratio:.8f}")
        assert ratio <= 1.0001


def symmetric_gap_checks() -> None:
    x = np.linspace(-14.0, 14.0, 240_001)
    print("q=1 symmetric-gap checks")
    for j, d in [(1, 1), (2, 1), (2, 2), (4, 3), (5, 5)]:
        mid = test_derivative(x, j)
        low = test_derivative(x, j - d)
        high = test_derivative(x, j + d)
        lhs_sq = float(np.trapz(mid * mid, x))
        signed = ((-1) ** d) * float(np.trapz(low * high, x))
        rel = abs(lhs_sq - signed) / max(1.0, abs(lhs_sq))
        holder_rhs = float(np.trapz(np.abs(low * high), x))
        print(f"  j={j} d={d}: identity rel.err={rel:.3e}, lhs/rhs={lhs_sq/holder_rhs:.8f}")
        assert rel < 2e-8
        assert lhs_sq <= holder_rhs * (1.0 + 2e-8)


def smooth_step_with_derivatives(s: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """C-infinity step rho and its first two derivatives."""
    rho = np.zeros_like(s)
    rho1 = np.zeros_like(s)
    rho2 = np.zeros_like(s)
    rho[s >= 1.0] = 1.0
    mask = (s > 0.0) & (s < 1.0)
    t = s[mask]
    left = np.exp(-1.0 / t)
    right = np.exp(-1.0 / (1.0 - t))
    left1 = left / t**2
    right1 = -right / (1.0 - t) ** 2
    left2 = left * (t ** -4 - 2.0 * t ** -3)
    right2 = right * ((1.0 - t) ** -4 - 2.0 * (1.0 - t) ** -3)
    den = left + right
    den1 = left1 + right1
    den2 = left2 + right2
    rho[mask] = left / den
    rho1[mask] = left1 / den - left * den1 / den**2
    rho2[mask] = (
        left2 / den
        - 2.0 * left1 * den1 / den**2
        - left * den2 / den**2
        + 2.0 * left * den1**2 / den**3
    )
    return rho, rho1, rho2


def endpoint_phase_plane_checks() -> None:
    print("q=infinity phase-plane growth checks")
    ratios = []
    for log_inv_eps in [4.0, 8.0, 12.0, 16.0]:
        eps = math.exp(-log_inv_eps)
        log_y = np.linspace(math.log(eps), log_inv_eps + 4.0, 600_001)
        transition, _, _ = smooth_step_with_derivatives(log_y)
        acceleration = 1.0 - 2.0 * transition
        energy = 2.0 * cumulative_trapezoid(acceleration, log_y, initial=0.0)
        positive = np.flatnonzero(energy > 0.0)
        last = positive[-1]
        log_y = log_y[: last + 1]
        energy = np.maximum(energy[: last + 1], 0.0)
        acceleration = acceleration[: last + 1]
        y = np.exp(log_y)

        s = (y - eps) / eps
        rho, rho1, rho2 = smooth_step_with_derivatives(s)
        chi = y * rho
        chi1 = rho + y * rho1 / eps
        chi2 = 2.0 * rho1 / eps + y * rho2 / eps**2
        slope = chi1 * np.sqrt(energy)
        second = chi2 * energy + chi1 * acceleration / y
        product_bound = float(np.max(np.abs(chi * second)))
        slope_sq = float(np.max(np.abs(slope)) ** 2)
        ratio = slope_sq / product_bound
        ratios.append(ratio)
        print(
            f"  log(1/eps)={log_inv_eps:4.1f}: "
            f"sup(f')^2/sup|f f''|={ratio:.6f}"
        )
    assert all(a < b for a, b in zip(ratios, ratios[1:]))
    assert ratios[-1] > 2.0 * ratios[0]


def main() -> None:
    finite_q_checks()
    symmetric_gap_checks()
    endpoint_phase_plane_checks()
    print("all deterministic checks passed")


if __name__ == "__main__":
    main()
