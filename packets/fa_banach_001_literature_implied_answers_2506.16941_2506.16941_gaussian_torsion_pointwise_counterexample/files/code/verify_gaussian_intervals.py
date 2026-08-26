#!/usr/bin/env python3
"""High-precision check of the centered Gaussian interval counterexample."""

import mpmath as mp


mp.mp.dps = 60


def mass_primitive(r):
    return mp.quad(lambda s: mp.exp(-s * s / 2), [0, r])


def slope(r):
    return mp.exp(r * r / 2) * mass_primitive(r)


def center_torsion(r):
    return mp.quad(slope, [0, r])


values = [mp.sqrt(center_torsion(r)) for r in (1, 2, 3)]
deficit = (values[0] + values[2]) / 2 - values[1]

print("sqrt(u_1(0)) =", mp.nstr(values[0], 30))
print("sqrt(u_2(0)) =", mp.nstr(values[1], 30))
print("sqrt(u_3(0)) =", mp.nstr(values[2], 30))
print("midpoint concavity deficit =", mp.nstr(deficit, 30))
assert deficit > 1
print("strict midpoint violation verified")

