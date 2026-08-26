#!/usr/bin/env python3
"""High-precision regression for the Laplace counterexample.

This script is not part of the proof.  The packet proves the strict
inequality using rational estimates separated at 1/5.
"""

from fractions import Fraction

import mpmath as mp


mp.mp.dps = 80
R = mp.mpf(5)
t = (1 - mp.e ** (-R)) / 2
g = -1 + R / (mp.e**R - 1)
lhs = (mp.e**g - mp.e ** (-R)) / 2
z = mp.sqrt(2) * mp.erfinv(2 * t - 1)
phi_z = mp.e ** (-(z**2) / 2) / mp.sqrt(2 * mp.pi)
rhs = mp.mpf("0.5") * mp.erfc((phi_z / t) / mp.sqrt(2))

a = Fraction(101, 125)
poly_integral = a - a**3 / 6 + a**5 / 40

print(f"t   = {mp.nstr(t, 50)}")
print(f"g   = {mp.nstr(g, 50)}")
print(f"lhs = {mp.nstr(lhs, 50)}")
print(f"rhs = {mp.nstr(rhs, 50)}")
print(f"gap = {mp.nstr(rhs - lhs, 50)}")
print(f"A(101/125) = {poly_integral} = {float(poly_integral):.15f}")

assert lhs < mp.mpf(1) / 5 < rhs
assert poly_integral < Fraction(3, 4)

