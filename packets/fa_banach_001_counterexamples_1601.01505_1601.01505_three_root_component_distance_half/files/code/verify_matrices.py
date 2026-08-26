#!/usr/bin/env python3
"""Exact symbolic checks and numerical norm checks for the packet matrices."""

import numpy as np
import sympy as sp


def op_norm(matrix: sp.Matrix) -> float:
    arr = np.array(matrix.evalf(), dtype=np.complex128)
    return float(np.linalg.norm(arr, 2))


I = sp.eye(2)
Z = sp.zeros(2)
e = sp.Matrix([[1, 0], [0, 0]])
f = sp.Matrix([[sp.Rational(9, 8), 1], [sp.Rational(-9, 64), sp.Rational(-1, 8)]])
D = 2 * f - e
N = D - sp.Rational(1, 2) * I
P = sp.Matrix([[8, 0], [-3, 4]])
J = sp.Matrix([[0, 1], [0, 0]])

assert e * e == e
assert f * f == f
assert e.rank() == f.rank() == 1
assert D == sp.Rational(1, 2) * I + N
assert N != Z and N * N == Z
assert P.inv() * N * P == J
assert sp.trace(e) == 1 and sp.trace(2 * f) == 2

print("Exact base identities: OK")
print("D =", D.tolist())
print("N =", N.tolist())
print("||N||_2 =", op_norm(N), "(exactly 73/32)")

for t in map(sp.Rational, [1, sp.Rational(1, 2), sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)]):
    S = P * sp.diag(t, 1) * P.inv()
    assert S.det() != 0
    assert S * N * S.inv() == t * N

    a = S * e * S.inv()
    b = 2 * S * f * S.inv()
    assert a * (a - I) * (a - 2 * I) == Z
    assert b * (b - I) * (b - 2 * I) == Z
    assert sp.trace(a) == 1 and sp.trace(b) == 2
    assert b - a == sp.Rational(1, 2) * I + t * N

    print(f"t={t}: ||b_t-a_t||_2={op_norm(b-a):.12f}")

S = P * sp.diag(sp.Rational(1, 10), 1) * P.inv()
a = S * e * S.inv()
b = 2 * S * f * S.inv()
assert op_norm(b - a) < 1
print("Fixed t=1/10 counterexample has norm gap < 1: OK")

