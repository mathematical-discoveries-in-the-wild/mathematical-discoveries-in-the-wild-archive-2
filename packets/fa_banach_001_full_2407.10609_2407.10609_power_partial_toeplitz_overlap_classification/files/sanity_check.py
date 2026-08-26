"""Exact check of the rank-one partial-isometry/non-PPI example."""

import sympy as sp


r = sp.sqrt(2) / 2
A = sp.Matrix([[r, r], [0, 0]])
initial = A.conjugate().T * A
final = A * A.conjugate().T
A2_initial = (A**2).conjugate().T * (A**2)

assert sp.simplify(initial * initial - initial) == sp.zeros(2)
assert sp.simplify(final * final - final) == sp.zeros(2)
assert sp.simplify(A**2 - r * A) == sp.zeros(2)
assert sp.simplify(A2_initial * A2_initial - A2_initial) != sp.zeros(2)

print("A*A =", initial)
print("AA* =", final)
print("(A^2)*(A^2) =", A2_initial)
print("counterexample_verified=true")
