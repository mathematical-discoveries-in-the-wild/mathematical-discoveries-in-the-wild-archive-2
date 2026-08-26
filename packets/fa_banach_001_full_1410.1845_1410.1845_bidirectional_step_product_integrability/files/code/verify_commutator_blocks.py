#!/usr/bin/env python3
"""Exact checks for the commutator blocks in the 1410.1845 packet."""

import sympy as sp


def e(i: int, j: int, n: int) -> sp.Matrix:
    out = sp.zeros(n)
    out[i - 1, j - 1] = 1
    return out


t = sp.symbols("t", positive=True)

# Exact 3 x 3, step-two nilpotent construction.
U = e(1, 2, 3)
V = e(2, 3, 3)
W = e(1, 3, 3)
I3 = sp.eye(3)
assert U * V == W
assert V * U == sp.zeros(3)
assert W * W == sp.zeros(3)

C3 = (I3 - t * V) * (I3 - t * U) * (I3 + t * V) * (I3 + t * U)
assert sp.simplify(C3 - (I3 - t**2 * W)) == sp.zeros(3)
assert sp.simplify((I3 + t**2 * W) * C3 - I3) == sp.zeros(3)
assert t * U + t * V - t * U - t * V + t**2 * W == t**2 * W

N = sp.symbols("N", integer=True, positive=True)
h = sp.symbols("h")
assert sp.simplify((I3 - h * W) * (I3 - t**2 * W) - (I3 - (h + t**2) * W)) == sp.zeros(3)

# Exact algebra behind the 2 x 2 refinement.
A = e(1, 2, 2)
B = e(2, 1, 2)
I2 = sp.eye(2)
C2 = (I2 - t * B) * (I2 - t * A) * (I2 + t * B) * (I2 + t * A)
C2_expected = sp.Matrix([[1 - t**2, -t**3], [t**3, 1 + t**2 + t**4]])
assert sp.simplify(C2 - C2_expected) == sp.zeros(2)
assert sp.expand(C2.det()) == 1
assert sp.expand(sp.trace(C2)) == 2 + t**4

cosh_s = 1 + t**4 / 2
D = sp.simplify(C2 - cosh_s * I2)
sinh_s_sq = sp.expand(cosh_s**2 - 1)
assert sp.simplify(D * D - sinh_s_sq * I2) == sp.zeros(2)
assert sp.simplify((C2.inv() - (cosh_s * I2 - D))) == sp.zeros(2)

# The diagonal functional of -log(C2) is positive and asymptotic to t^2.
# With s = arcosh(cosh_s), log(C2) = (s/sinh(s)) D.
ell_minus_D = sp.simplify((-D[0, 0] + D[1, 1]) / 2)
assert ell_minus_D == t**2 + t**4 / 2

print("3x3 commutator identity: verified")
print("3x3 correction identity: verified")
print("3x3 additive block sums: verified")
print("2x2 commutator matrix, determinant, trace, and log direction: verified")

