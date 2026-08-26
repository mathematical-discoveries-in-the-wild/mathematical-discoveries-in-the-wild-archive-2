#!/usr/bin/env python3
"""Sanity checks for the dyadic-cone lower bound (not proof evidence)."""

from __future__ import annotations

import math


def kernel_2d(m1: int, m2: int) -> float:
    if m1 == 0 and m2 == 0:
        return 0.0
    return (m1 * m1) / (math.pi * (m1 * m1 + m2 * m2) ** 2)


def shell_sum(q: int) -> float:
    r = 2**q
    return sum(kernel_2d(m1, m2) for m1 in range(r, 2 * r) for m2 in range(r))


def cube_mass(radius: int) -> float:
    return sum(
        kernel_2d(m1, m2)
        for m1 in range(-radius, radius + 1)
        for m2 in range(-radius, radius + 1)
    )


def main() -> None:
    alpha_2 = 1.0 / (25.0 * math.pi)
    print(f"proved per-shell bound alpha_2 = {alpha_2:.12f}")
    for q in range(8):
        value = shell_sum(q)
        assert value >= alpha_2
        print(f"q={q:2d} r={2**q:4d} shell_sum={value:.12f}")

    previous = 0.0
    for radius in (4, 8, 16, 32, 64, 128):
        value = cube_mass(radius)
        assert value > previous
        previous = value
        print(f"radius={radius:3d} cube_mass={value:.12f}")

    for ell in (2, 4, 8, 12):
        n = 2 ** (ell + 1)
        ratio_bound = alpha_2 * ell * (2 * n + 1) / (4 * n + 1)
        print(f"L={ell:2d} N={n:5d} ell2_ratio_lower_bound={ratio_bound:.12f}")


if __name__ == "__main__":
    main()
