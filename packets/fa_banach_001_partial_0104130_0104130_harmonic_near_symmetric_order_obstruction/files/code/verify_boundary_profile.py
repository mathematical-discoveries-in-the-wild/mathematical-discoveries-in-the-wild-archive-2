#!/usr/bin/env python3
"""Numerical consistency checks for the critical boundary profile."""

from __future__ import annotations

import math


def simpson_integral(u: float, panels: int = 20000) -> float:
    """Return integral_0^1 sin(u t)/t dt by composite Simpson quadrature."""
    if panels % 2:
        raise ValueError("panels must be even")

    def integrand(t: float) -> float:
        return u if t == 0.0 else math.sin(u * t) / t

    step = 1.0 / panels
    total = integrand(0.0) + integrand(1.0)
    total += 4.0 * sum(integrand(j * step) for j in range(1, panels, 2))
    total += 2.0 * sum(integrand(j * step) for j in range(2, panels, 2))
    return step * total / 3.0


def profile(u: float) -> float:
    return math.pi - 2.0 * simpson_integral(u)


def finite_error(n_terms: int, u: float) -> float:
    fourier_sum = 2.0 * sum(
        math.sin(n * u / n_terms) / n for n in range(1, n_terms + 1)
    )
    return math.pi - u / n_terms - fourier_sum


def main() -> None:
    grid = [0.1 + 1.15 * j / 80.0 for j in range(81)]
    errors = {}
    for n_terms in (64, 128, 256):
        errors[n_terms] = max(
            abs(finite_error(n_terms, u) - profile(u)) for u in grid
        )
        print(f"N={n_terms:3d} max_profile_error={errors[n_terms]:.8e}")

    # R is strictly decreasing on (0, pi).  The closest values on these
    # intervals occur at u=1/4 and v=1.
    separation = profile(0.25) - profile(1.0)
    print(f"profile_separation_U_[.125,.25]_V_[1,1.25]={separation:.8e}")

    assert errors[256] < errors[128] < errors[64]
    assert errors[256] < 0.01
    assert separation > 0.5
    print("PASS: finite boundary layers converge and the profile is separated")


if __name__ == "__main__":
    main()
