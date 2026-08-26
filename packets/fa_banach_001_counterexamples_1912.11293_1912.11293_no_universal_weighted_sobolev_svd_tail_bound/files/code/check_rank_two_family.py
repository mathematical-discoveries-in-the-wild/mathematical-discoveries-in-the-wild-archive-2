#!/usr/bin/env python3
"""Exact checks for the rank-two Sobolev-SVD counterexample family.

The proof is elementary and does not depend on this script.
"""

import sympy as sp


n = sp.symbols("n", positive=True, integer=True)
t = n**2 / 2
g = sp.Matrix([[1 + t, t], [t, 1 + t]])
d = sp.diag(2, 1)
a = sp.simplify(d * g * d)

assert a == sp.Matrix([[4 + 2 * n**2, n**2], [n**2, 1 + n**2 / 2]])
assert sp.simplify(a.det() - 4 * (1 + n**2)) == 0
assert sp.simplify(a.trace() - 5 * (n**2 + 2) / 2) == 0

for value in [1, 2, 5, 10, 100, 1000]:
    av = a.subs(n, value)
    eigenvalues = sorted(float(x) for x in av.eigenvals())
    lambda_minus = eigenvalues[0]
    lhs = 1 + value**2 / 2
    assert lambda_minus < 2
    print(
        f"N={value:4d}  left_tail={lhs:12.3f}  "
        f"lambda_minus={lambda_minus:.12f}  ratio={lhs/lambda_minus:.3f}"
    )

print("PASS: left tail diverges while the second squared H^(1,0) singular value is < 2")
