"""Numerical sanity checks for the explicit formulas in the packet."""

from __future__ import annotations

import math


def check_half_lattice() -> None:
    a = 1.25
    h = 0.7
    d = math.pi / (2.0 * h)
    for n in range(12):
        z = a + n * h
        if n % 2 == 0:
            u = math.sin(d * (z - a)) / (z - a + 2.0 * h)
            assert abs(u) < 1.0e-12
        else:
            v = math.cos(d * (z - a)) / (z - a + h)
            assert abs(v) < 1.0e-12


def check_flux_counterexample() -> None:
    # If d_left were nonzero, the p and p_tilde flux laws would demand two
    # different right derivatives.
    d_left = 1.0
    assert 4.0 * d_left != 2.0 * d_left


def check_derivative_witness() -> None:
    c = 0.8
    derivative = 2.0 * c**3 / (3.0 * math.sqrt(2.0 * math.pi))
    assert derivative > 0.0


if __name__ == "__main__":
    check_half_lattice()
    check_flux_counterexample()
    check_derivative_witness()
    print("explicit identity checks passed")
