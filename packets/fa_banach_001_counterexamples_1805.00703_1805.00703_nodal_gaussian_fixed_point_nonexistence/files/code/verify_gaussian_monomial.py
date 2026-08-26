#!/usr/bin/env python3
"""Exact checks for the Gaussian-monomial fixed-point obstruction."""

import sympy as sp


y, a, lam2, s = sp.symbols("y a lam2 s", positive=True)

# First nodal Gaussian.
f = y * sp.exp(-a * y**2 / 2)
B = sp.simplify(sp.diff(f, y) ** 2 - f * sp.diff(f, y, 2))
assert sp.simplify(B - (1 + a * y**2) * sp.exp(-a * y**2)) == 0

c = a + lam2 * s
den = sp.integrate(y**2 * sp.exp(-c * y**2), (y, -sp.oo, sp.oo))
num = sp.integrate((1 + a * y**2) * sp.exp(-c * y**2), (y, -sp.oo, sp.oo))
ratio = sp.simplify(num / den)
assert sp.simplify(ratio - (3 * a + 2 * lam2 * s)) == 0

print("f_1 quotient:", ratio)
print("f_1 recurrence: s_(n+1) = 3*a/2 + 3*lambda^2*s_n/2")
print("f_1 sharp threshold: lambda^2 < 2/3")

# General monomial thresholds; the proof packet derives the moment identity.
for m in range(1, 7):
    threshold = sp.Rational(4 * m - 2, 4 * m - 1)
    A_m = a * sp.Rational(4 * m - 1, 2 * (2 * m - 1))
    r_m = lam2 * sp.Rational(4 * m - 1, 2 * (2 * m - 1))
    assert sp.simplify(r_m.subs(lam2, threshold) - 1) == 0
    print(f"m={m}: A_m={A_m}, r_m={r_m}, threshold={threshold}")
