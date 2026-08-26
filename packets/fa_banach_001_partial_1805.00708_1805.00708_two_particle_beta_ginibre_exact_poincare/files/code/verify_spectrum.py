#!/usr/bin/env python3
"""Exact symbolic checks for the two-particle beta-Ginibre spectrum."""

import sympy as sp


r, a, beta = sp.symbols("r a beta", positive=True)
rho = sp.symbols("rho", positive=True)


def alpha(m: int):
    return (sp.sqrt(beta**2 + 4 * m**2) - beta) / 2


def radial_residual(m: int, k: int):
    al = alpha(m)
    q = al + beta / 2
    R = r**al * sp.assoc_laguerre(k, q, a * r**2)
    LmR = (
        sp.diff(R, r, 2)
        + ((beta + 1) / r - 2 * a * r) * sp.diff(R, r)
        - m**2 / r**2 * R
    )
    eigenvalue = 4 * a * k + 2 * a * al
    return sp.simplify(LmR + eigenvalue * R)


for m in range(4):
    for k in range(3):
        assert radial_residual(m, k) == 0, (m, k, radial_residual(m, k))

gap = sp.simplify(2 * a * alpha(1))
assert sp.simplify(gap - a * (sp.sqrt(beta**2 + 4) - beta)) == 0
constant = (sp.sqrt(beta**2 + 4) + beta) / (4 * a)
assert sp.simplify(constant * gap - 1) == 0

# Independent Rayleigh-quotient check for r^alpha cos(theta).
al = alpha(1)
rayleigh_constant = sp.simplify((al + beta / 2) / (a * (al**2 + 1)))
assert sp.simplify(rayleigh_constant - constant) == 0
assert sp.simplify(gap.subs(beta, 0) - 2 * a) == 0
assert sp.simplify(gap.subs({beta: 2, a: 2}) - 4 * (sp.sqrt(2) - 1)) == 0
assert sp.simplify(constant.subs({beta: 2, a: 2}) - (1 + sp.sqrt(2)) / 4) == 0

print("checked Laguerre eigen-equation for m=0..3 and k=0..2")
print("gap =", gap)
print("optimal Poincare constant =", constant)
print("source n=2, beta=2 gap =", gap.subs({beta: 2, a: 2}))
print("source n=2, beta=2 constant =", constant.subs({beta: 2, a: 2}))
