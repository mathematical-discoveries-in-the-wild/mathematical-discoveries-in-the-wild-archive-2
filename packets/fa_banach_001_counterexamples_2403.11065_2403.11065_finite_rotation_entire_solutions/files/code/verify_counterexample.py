#!/usr/bin/env python3
"""Exact symbolic verification of the q=3, a=1/2 counterexample."""

import sympy as sp


z = sp.symbols("z")
I = sp.I
a = sp.Rational(1, 2)
omega = (-1 + I * sp.sqrt(3)) / 2


def h(w):
    return sp.cancel((w + a) / (1 + a * w))


def h_inv(w):
    return sp.cancel((w - a) / (1 - a * w))


def gamma(j, w):
    return sp.cancel(h(omega**j * h_inv(w)))


def gamma_inv(j, w):
    return sp.cancel(h(omega ** (-j) * h_inv(w)))


def value_at_infinity(expr):
    num, den = sp.fraction(sp.cancel(expr))
    return sp.simplify(sp.LC(sp.Poly(num, z)) / sp.LC(sp.Poly(den, z)))


f = 1 / (2 - z)
lhs = 0
rhs = 0

for j in (1, 2):
    inv = gamma_inv(j, z)
    lhs += sp.Rational(1, 2) * f.subs(z, inv) * sp.diff(inv, z)
    pole = value_at_infinity(gamma(j, z))
    rhs += sp.Rational(1, 2) / (z - pole)
    assert sp.simplify(gamma(j, 0)) != 0
    assert sp.simplify(gamma(j, gamma_inv(j, z)) - z) == 0

lhs -= f
assert sp.simplify(lhs - rhs) == 0
assert sp.simplify(omega**2 + omega + 1) == 0
assert len({sp.simplify(gamma(j, z)) for j in (1, 2)}) == 2

print("PASS: exact holomorphic stationarity equation verified")
print("f(z) =", f)
print("radius of convergence about 0 = 2")
print("support size = 2; both support maps move 0")

