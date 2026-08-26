#!/usr/bin/env python3
"""Numerical check for the Chebyshev symmetrization used in the proof.

This script is evidence only; the solution packet's counting argument is exact.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial import Chebyshev, Polynomial


def level_value(d: int, m: int, n: int) -> float:
    """Return the level-m homogeneous part at 1 for T_d(mean epsilon)."""
    polynomial = Chebyshev.basis(d).convert(kind=Polynomial)
    value = 0.0
    for r in range(m + 1):
        for s in range(n - m + 1):
            probability = math.comb(m, r) * math.comb(n - m, s) / (2**n)
            character = (-1) ** r
            mean = (n - 2 * (r + s)) / n
            value += math.comb(n, m) * probability * character * polynomial(mean)
    return value


def main() -> None:
    for d, m in ((6, 2), (7, 3), (10, 6)):
        polynomial = Chebyshev.basis(d).convert(kind=Polynomial)
        target = float(polynomial.coef[m])
        print(f"d={d}, m={m}, target={target:g}")
        for n in (20, 50, 100, 200):
            print(f"  n={n:3d}: {level_value(d, m, n):.12g}")


if __name__ == "__main__":
    main()
