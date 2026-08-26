#!/usr/bin/env python3
"""Numerical checks for the recurrent-spike packet.

The proof of recurrence is exact (Kronecker's theorem); this script checks
the finite peak estimate around the identity recurrence and the block-budget
scaling used in the construction.
"""

from __future__ import annotations

import cmath
import math


def harmonic(n: int) -> float:
    return sum(1.0 / j for j in range(1, n + 1))


def boundary_value(n: int, t: float) -> complex:
    h_n = harmonic(n)
    return sum(cmath.exp(-1j * t * math.log(j)) / j for j in range(1, n + 1)) / math.sqrt(h_n)


def check_peaks() -> None:
    for n in (32, 128, 512, 2048):
        h_n = harmonic(n)
        delta = 1.0 / (16.0 * math.log(n))
        grid = [(-delta + 2.0 * delta * j / 400) for j in range(401)]
        observed = min(abs(boundary_value(n, t)) ** 2 for t in grid)
        rigorous_floor = (7.0 / 8.0) ** 2 * h_n
        assert observed + 1e-12 >= rigorous_floor
        print(
            f"N={n:4d} H_N={h_n:.8f} delta={delta:.3e} "
            f"min_peak={observed:.8f} proof_floor={rigorous_floor:.8f}"
        )


def check_block_scaling() -> None:
    mass_budget = 0.0
    lower_values = []
    for k in range(1, 31):
        # The proof only needs log N_k at least this large.
        log_n = (2.0**k) * (k**2)
        height = 1.0 / k
        count = k**2
        delta = 1.0 / (16.0 * log_n)
        mass_budget += 2.0 * height * count * delta
        lower_values.append((49.0 / 1024.0) * height * count)
    assert mass_budget < 0.2
    assert all(b > a for a, b in zip(lower_values, lower_values[1:]))
    print(f"30-block support-mass upper budget (unit bump integral bound): {mass_budget:.8f}")
    print(f"test lower bound grows from {lower_values[0]:.8f} to {lower_values[-1]:.8f}")


if __name__ == "__main__":
    check_peaks()
    check_block_scaling()
    print("all recurrent-spike checks passed")
