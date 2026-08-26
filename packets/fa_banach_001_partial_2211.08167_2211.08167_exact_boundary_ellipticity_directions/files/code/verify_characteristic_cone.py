#!/usr/bin/env python3
"""Exact checks for the characteristic cone in Example 6.5."""

import sympy as sp


z1, z2, a, b = sp.symbols("z1 z2 a b", real=False)
block = sp.Matrix([[z1, -z2], [z2, z1]])
assert sp.factor(block.det()) == z1**2 + z2**2
assert sp.factor(z1**2 + z2**2, extension=sp.I) == (z1 - sp.I * z2) * (
    z1 + sp.I * z2
)

# If nu=(a,b,0,...,0), then xi=(b,-a,0,...,0) gives a characteristic
# covector on the + branch: xi+i nu=(b+i a)(1,i,0,...,0).
lam = b + sp.I * a
zeta1 = b + sp.I * a
zeta2 = -a + sp.I * b
assert sp.simplify(zeta1 - lam) == 0
assert sp.simplify(zeta2 - sp.I * lam) == 0
assert sp.simplify(zeta1**2 + zeta2**2) == 0

# A concrete bad direction in the first plane.
bad_block = block.subs({z1: sp.I, z2: 1})
bad_vector = sp.Matrix([1, sp.I])
assert bad_block * bad_vector == sp.zeros(2, 1)

# A direction with a nonzero third component cannot lie in the
# characteristic cone, whose coordinates 3,...,n vanish identically.
print("determinant:", sp.factor(block.det(), extension=sp.I))
print("bad-normal identity: xi+i*nu =", (zeta1, zeta2), "=", lam, "*(1,i)")
print("all exact checks passed")
