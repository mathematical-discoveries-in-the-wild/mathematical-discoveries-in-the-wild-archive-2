#!/usr/bin/env python3
"""Independent checks for the four-dimensional harmonic-Fock L1 counterexample."""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad
from scipy.special import factorial


def kernel_closed(s: float, theta: float) -> float:
    """H_1(x,y) in R^4, where s=|x||y| and theta is their angle."""
    a = s * math.cos(theta)
    b = s * math.sin(theta)
    sinc = 1.0 if abs(b) < 1e-14 else math.sin(b) / b
    return math.exp(a) * (a * sinc + math.cos(b))


def kernel_series(s: float, theta: float, terms: int = 80) -> float:
    """Sum C_k^1(cos theta) s^k/k! using C_k^1=sin((k+1)theta)/sin(theta)."""
    if abs(math.sin(theta)) < 1e-12:
        coefficients = np.arange(1, terms + 1, dtype=float)
    else:
        k = np.arange(terms, dtype=float)
        coefficients = np.sin((k + 1.0) * theta) / math.sin(theta)
    k = np.arange(terms, dtype=float)
    return float(np.sum(coefficients * np.power(s, k) / factorial(k)))


def column_mass(r_value: float) -> float:
    """Numerically integrate the exact absolute dmu_2-column mass at R e_1."""

    def radial_integral(u: float) -> float:
        def integrand(rho: float) -> float:
            if rho == 0.0:
                oscillatory = r_value * (r_value + u) + 1.0
            else:
                oscillatory = (
                    (r_value + u) * math.sin(r_value * rho) / rho
                    + math.cos(r_value * rho)
                )
            return math.exp(-rho * rho / 2.0) * rho * rho * abs(oscillatory)

        # Break at the zeros of sin/cos only to make the absolute-value
        # quadrature stable.  The tail beyond rho=8 is negligible here.
        points = sorted(
            {
                0.0,
                8.0,
                *[
                    j * math.pi / (2.0 * r_value)
                    for j in range(1, int(16.0 * r_value / math.pi) + 1)
                    if j * math.pi / (2.0 * r_value) < 8.0
                ],
            }
        )
        total = 0.0
        for left, right in zip(points[:-1], points[1:]):
            total += quad(integrand, left, right, epsabs=2e-9, epsrel=2e-9)[0]
        return math.exp(-u * u / 2.0) * total

    # dv contributes 4 pi rho^2 drho and the column prefactor is pi^{-2}.
    return (4.0 / math.pi) * quad(
        radial_integral, -7.0, 7.0, epsabs=2e-7, epsrel=2e-7, limit=250
    )[0]


def analytic_lower_bound(r_value: float) -> float:
    """The explicit restricted-region lower bound used in the proof."""
    cu = quad(lambda u: math.exp(-u * u / 2.0), -1.0, 1.0)[0]
    c_rho = quad(lambda rho: math.exp(-rho * rho / 2.0) * rho * rho, 1.0, 2.0)[0]
    sine_floor = 2.0 / math.pi - 2.0 / r_value
    weighted_sine_floor = math.exp(-2.0) * max(sine_floor, 0.0)
    return (4.0 / math.pi) * cu * (
        0.5 * (r_value - 1.0) * weighted_sine_floor - c_rho
    )


def main() -> None:
    print("closed kernel versus zonal series")
    for s, theta in [(0.3, 0.8), (1.7, 1.1), (4.0, 0.37)]:
        closed = kernel_closed(s, theta)
        series = kernel_series(s, theta)
        err = abs(closed - series)
        print(f"  s={s:3.1f}, theta={theta:4.2f}: error={err:.3e}")
        assert err < 2e-11

    print("\nGaussian exponent cancellation")
    for r_value, u, rho in [(3.0, -0.4, 1.2), (10.0, 0.7, 2.1)]:
        a = r_value * (r_value + u)
        exponent = -r_value**2 / 2.0 - ((r_value + u) ** 2 + rho**2) / 2.0 + a
        target = -(u**2 + rho**2) / 2.0
        print(f"  R={r_value:4.1f}: error={abs(exponent-target):.3e}")
        assert abs(exponent - target) < 2e-14

    print("\nabsolute column masses")
    values = []
    for r_value in [8.0, 16.0, 32.0, 64.0]:
        mass = column_mass(r_value)
        lower = analytic_lower_bound(r_value)
        values.append(mass)
        print(f"  R={r_value:4.0f}: J(R)={mass:10.5f}, proof lower bound={lower:10.5f}")
        assert mass >= lower - 2e-4
    assert values[-1] > 5.0 * values[0]
    print("\nPASS: the exact absolute columns exhibit unbounded linear growth.")


if __name__ == "__main__":
    main()

