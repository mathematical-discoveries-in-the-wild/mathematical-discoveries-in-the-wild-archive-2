#!/usr/bin/env python3
"""Check every exponent and the concrete n=3 normalization in the packet."""

from fractions import Fraction
from math import pi


def check_dimension(n: int) -> None:
    gamma = Fraction(n + 2, 4)
    assert gamma > 1
    assert 2 * gamma < n  # g(x)=|x|^-gamma belongs to L^2 locally.
    assert 2 * gamma - 1 == Fraction(n, 2)
    assert gamma - 1 == Fraction(n - 2, 4)


for dimension in range(3, 101):
    check_dimension(dimension)

# Concrete R^3 formulas: gamma=5/4, c_r=7/(16*pi) r^(-7/4).
for radius in (1e-1, 1e-2, 1e-4):
    c_r = 7 / (16 * pi) * radius ** (-7 / 4)
    data_fit = c_r * 4 * pi * radius ** (7 / 4) / (7 / 4)
    weighted_l2 = c_r**2 * 4 * pi * radius**5 / 5
    total_variation = c_r * 4 * pi * radius**2
    assert abs(data_fit - 1) < 1e-12
    assert abs(weighted_l2 - 49 / (320 * pi) * radius ** (3 / 2)) < 1e-12
    assert abs(total_variation - Fraction(7, 4) * radius ** Fraction(1, 4)) < 1e-12

print("PASS: dimensions 3..100 and the normalized n=3 formulas agree.")
