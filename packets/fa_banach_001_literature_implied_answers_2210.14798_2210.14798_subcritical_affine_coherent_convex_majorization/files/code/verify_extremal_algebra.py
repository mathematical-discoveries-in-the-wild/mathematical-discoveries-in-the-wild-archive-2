#!/usr/bin/env python3
"""Symbolic checks for the subcritical hinge-majorization calculation."""

import sympy as sp


a, tau, T = sp.symbols("a tau T", positive=True)
A = tau ** (a - 1)

baseline = a * T * (A - T ** (a - 1)) / (1 - a) - T**a + tau**a
ratio = (A * T ** (1 - a) - 1) / (1 - a)
q_raw = baseline + ratio * (1 - T**a)
q_closed = A * (T ** (1 - a) / (1 - a) - T) - 1 / (1 - a) + tau**a

assert sp.simplify(q_raw - q_closed) == 0
assert sp.simplify(sp.diff(q_closed, T) - A * (T ** (-a) - 1)) == 0

coherent_direct = a * (tau ** (a - 1) - 1) / (1 - a) - (1 - tau**a)
assert sp.simplify(q_closed.subs(T, 1) - coherent_direct) == 0

# The kernel-to-cost ratio is increasing in the jump location y.
y = sp.symbols("y", positive=True)
kernel_ratio = ((tau / y) ** (a - 1) - 1) / (1 - a)
assert sp.simplify(sp.diff(kernel_ratio, y) - tau ** (a - 1) * y ** (-a)) == 0

print("symbolic hinge-majorization identities: PASS")

