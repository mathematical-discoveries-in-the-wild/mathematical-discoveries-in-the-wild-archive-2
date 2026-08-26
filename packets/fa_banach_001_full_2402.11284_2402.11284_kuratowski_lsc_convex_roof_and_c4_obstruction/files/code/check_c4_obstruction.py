#!/usr/bin/env python3
"""Exact check of the four-cycle Kuratowski chord obstruction."""

from fractions import Fraction


def cycle_distance(i: int, j: int) -> int:
    gap = abs(i - j)
    return min(gap, 4 - gap)


rows = [[cycle_distance(i, j) for j in range(4)] for i in range(4)]
base = rows[0]
kuratowski = [[entry - base[j] for j, entry in enumerate(row)] for row in rows]

midpoint_02 = [Fraction(kuratowski[0][j] + kuratowski[2][j], 2) for j in range(4)]
midpoint_13 = [Fraction(kuratowski[1][j] + kuratowski[3][j], 2) for j in range(4)]
rho = [0, 1, 0, 1]
cost_02 = Fraction(rho[0] + rho[2], 2)
cost_13 = Fraction(rho[1] + rho[3], 2)

assert midpoint_02 == midpoint_13
assert cost_02 == 0
assert cost_13 == 1

print("distance rows:", rows)
print("base-pointed Kuratowski rows:", kuratowski)
print("common midpoint:", midpoint_02)
print("forced affine values:", cost_02, "and", cost_13)
print("PASS: one semihull point receives incompatible affine values")
