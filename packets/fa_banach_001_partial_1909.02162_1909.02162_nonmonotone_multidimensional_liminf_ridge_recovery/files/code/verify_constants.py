#!/usr/bin/env python3
"""Numerically compare the transverse Riesz marginal with gamma_{d,p}/2."""

from __future__ import annotations

import math

import scipy.integrate as integrate
import scipy.special as special


def closed_form(d: int, p: float) -> float:
    return math.pi ** ((d - 1) / 2) * special.gamma((p + 1) / 2) / special.gamma((d + p) / 2)


def radial_marginal(d: int, p: float) -> float:
    if d == 1:
        return 1.0
    sphere_dm2 = 2 * math.pi ** ((d - 1) / 2) / special.gamma((d - 1) / 2)
    value, error = integrate.quad(
        lambda r: r ** (d - 2) * (1 + r * r) ** (-(d + p) / 2),
        0,
        math.inf,
        epsabs=1e-11,
        epsrel=1e-11,
    )
    assert error < 1e-8
    return sphere_dm2 * value


def half_sphere_constant(d: int, p: float) -> float:
    sphere_dm2 = 2 * math.pi ** ((d - 1) / 2) / special.gamma((d - 1) / 2)
    value, error = integrate.quad(
        lambda theta: math.sin(theta) ** (d - 2) * abs(math.cos(theta)) ** p,
        0,
        math.pi,
        epsabs=1e-11,
        epsrel=1e-11,
    )
    assert error < 1e-8
    return 0.5 * sphere_dm2 * value


def main() -> None:
    for d, p in [(2, 1), (2, 2), (3, 1), (3, 3), (5, 2.5)]:
        expected = closed_form(d, p)
        marginal = radial_marginal(d, p)
        half_gamma = half_sphere_constant(d, p)
        assert math.isclose(marginal, expected, rel_tol=1e-9, abs_tol=1e-9)
        assert math.isclose(half_gamma, expected, rel_tol=1e-9, abs_tol=1e-9)
        print(f"d={d}, p={p}: c={expected:.12g}")


if __name__ == "__main__":
    main()
