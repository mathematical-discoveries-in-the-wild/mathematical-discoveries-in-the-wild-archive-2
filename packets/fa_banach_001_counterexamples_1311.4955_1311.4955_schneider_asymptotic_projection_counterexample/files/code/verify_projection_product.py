#!/usr/bin/env python3
"""Exact audits for the octahedral Schneider-product counterexample."""

from fractions import Fraction
from itertools import combinations


VECTORS = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def det3(cols):
    a, b, c = cols
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )


raw_dets = [abs(det3(cols)) for cols in combinations(VECTORS, 3)]
assert raw_dets == [4, 4, 4, 4], raw_dets

# Each generator is v_j/2.  A symmetric 3-zonotope sum_j[-g_j,g_j]
# has volume 2^3 times the sum of all absolute 3-by-3 determinants.
generator_det_sum = sum(Fraction(d, 2**3) for d in raw_dets)
projection_volume = 2**3 * generator_det_sum
octahedron_volume = Fraction(4, 3)
p_octahedron = projection_volume / octahedron_volume**2

assert projection_volume == 16
assert p_octahedron == 9
assert Fraction(p_octahedron, 2**3) == Fraction(9, 8)

print("raw determinant moduli:", raw_dets)
print("|Pi B_1^3| =", projection_volume)
print("|B_1^3| =", octahedron_volume)
print("P_3(B_1^3) =", p_octahedron)
print("P_3(B_1^3)/P_3(C_3) =", Fraction(9, 8))
print("asymptotic lower bound = (9/8)^(1/3) =", float(Fraction(9, 8)) ** (1 / 3))

# Finite product sanity checks: P(O^m)/2^(3m)=(9/8)^m.
for m in range(1, 9):
    ratio = Fraction(9, 8) ** m
    assert ratio == Fraction(9**m, 8**m)
    print(f"m={m}: normalized ratio={ratio}")

