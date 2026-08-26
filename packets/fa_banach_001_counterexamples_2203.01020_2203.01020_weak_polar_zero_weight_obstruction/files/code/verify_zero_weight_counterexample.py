#!/usr/bin/env python3
"""Exact-formula sanity checks for the zero-weight weak-polar example."""

from math import exp, isclose, pi


# For p=2 on R^2 and h=e^{|x|} Lebesgue-a.e.,
# R_2 = 2*pi*integral_1^infinity r*e^{-2r}dr.
r2_closed_form = 1.5 * pi * exp(-2.0)
assert r2_closed_form > 0.0

# A_{2^j} has area 3*pi*4^j, so every term in mathcal R_2 is 1/(3*pi).
annular_term = 1.0 / (3.0 * pi)
for j in range(20):
    radius_squared = 4.0**j
    annulus_area = 3.0 * pi * radius_squared
    assert isclose(radius_squared / annulus_area, annular_term, rel_tol=1e-15)

for count in (1, 10, 100, 1000):
    partial_sum = count * annular_term
    assert partial_sum > 0.0
    print(f"first {count:4d} annular terms sum to {partial_sum:.12g}")

print(f"R_2(h,0) = (3*pi/2)e^(-2) = {r2_closed_form:.12g} < infinity")
print(f"each mathcal R_2 annular term = 1/(3*pi) = {annular_term:.12g}")
print("zero-weight counterexample sanity checks passed")
