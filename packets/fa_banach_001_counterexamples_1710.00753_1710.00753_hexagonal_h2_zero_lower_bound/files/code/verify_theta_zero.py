#!/usr/bin/env python3
"""Audit the torsion-point lattice sum and the final modular algebra."""

import mpmath as mp
import sympy as sp


def truncated_sum(radius: int) -> mp.mpf:
    value = mp.mpf("0")
    u = 2 * mp.pi / mp.sqrt(3)
    for k in range(-radius, radius + 1):
        for ell in range(-radius, radius + 1):
            qform = k * k + k * ell + ell * ell
            coefficient = mp.exp(-u * qform) * (
                1 - 4 * u * qform + 2 * u * u * qform * qform
            )
            value += coefficient * mp.cos(2 * mp.pi * (k - ell) / 3)
    return value


def symbolic_audit() -> None:
    e, f = sp.symbols("e f")
    pi = sp.pi
    root3 = sp.sqrt(3)
    u = 2 * pi / root3
    e3 = -e / 3 + 2 * root3 / pi
    f3 = f / 9
    logarithmic = (e - e3) / 8
    delta_logarithmic = ((e * e - f) - 3 * (e3 * e3 - f3)) / 96
    ratio = sp.factor(
        1 - 4 * u * logarithmic
        + 2 * u * u * (logarithmic * logarithmic + delta_logarithmic)
    )
    level_three = (3 * e3 - e) / 2
    expected = sp.pi**2 * (5 * level_three**2 - f) / 54
    assert sp.simplify(ratio - expected) == 0
    assert sp.simplify(expected.subs(f, 5 * level_three**2)) == 0
    print("symbolic modular reduction: exact zero")


def main() -> None:
    mp.mp.dps = 100
    for radius in [2, 3, 4, 5, 6, 8, 10]:
        print(f"radius={radius:2d}  sum={mp.nstr(truncated_sum(radius), 50)}")
    symbolic_audit()


if __name__ == "__main__":
    main()
