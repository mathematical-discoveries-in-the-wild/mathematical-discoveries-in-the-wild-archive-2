#!/usr/bin/env python3
"""Symbolic checks for the degree-two finite/free comparison packet."""

import sympy as sp


m, n = sp.symbols("m n", real=True)
alpha, beta = sp.symbols("alpha beta", nonnegative=True)
v, t = sp.symbols("v t", positive=True)

# For p=(x-m)^2-alpha^2 and q=(x-n)^2-beta^2, the elementary
# coefficients are p=x^2-a1*x+a2 and q=x^2-b1*x+b2.
a1, a2 = 2 * m, m**2 - alpha**2
b1, b2 = 2 * n, n**2 - beta**2
c1 = sp.expand(a1 + b1)
c2 = sp.expand(a2 + b2 + sp.Rational(1, 2) * a1 * b1)

assert sp.simplify(c1 - 2 * (m + n)) == 0
assert sp.simplify(c2 - ((m + n) ** 2 - alpha**2 - beta**2)) == 0

# On v>t^2 the truncated-square-root kernel is (sqrt(v)-t)^3.
g = (sp.sqrt(v) - t) ** 3
g_second = sp.simplify(sp.diff(g, v, 2))
expected = 3 * (v - t**2) / (4 * v ** sp.Rational(3, 2))
assert sp.simplify(g_second - expected) == 0

print("finite coefficient identity: PASS")
print("g''(v) =", g_second)
print("convex for v >= t^2: PASS")

