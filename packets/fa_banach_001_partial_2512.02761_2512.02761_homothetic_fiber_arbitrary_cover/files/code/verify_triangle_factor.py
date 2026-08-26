#!/usr/bin/env python3
"""Exact check for the first non-1-reducible cover."""

import sympy as sp


q = sp.symbols("q", integer=True, nonnegative=True)

# For psi(t)=(1-t)_+^q, mu_d = E[R^d] = d! q!/(d+q)!.
mu2 = sp.factor(2 / ((q + 1) * (q + 2)))
mu3 = sp.factor(6 / ((q + 1) * (q + 2) * (q + 3)))
ratio = sp.factor(mu3**2 / mu2**3)
excess = sp.factor(ratio - 1)

assert sp.simplify(
    ratio - sp.Rational(9, 2) * (q + 1) * (q + 2) / (q + 3) ** 2
) == 0
assert sp.simplify(excess - q * (7 * q + 15) / (2 * (q + 3) ** 2)) == 0
assert sp.simplify(ratio.subs(q, 1) - sp.Rational(27, 16)) == 0

# {12,13,23} is a 2-cover of [3], but no two of its edges are disjoint,
# so it cannot split into two 1-covers.
edges = ({0, 1}, {0, 2}, {1, 2})
assert all(sum(i in edge for edge in edges) == 2 for i in range(3))
assert not any(edges[i].isdisjoint(edges[j]) for i in range(3) for j in range(i))

print("triangle cover: 2-cover and not 1-reducible")
print("mu_3^2/mu_2^3 =", ratio)
print("excess over 1 =", excess)
print("q=1 factor =", ratio.subs(q, 1))
