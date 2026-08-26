#!/usr/bin/env python3
"""Exact finite-matrix audit of the Peirce/Sylvester construction."""

import sympy as sp


def block_diag(a: sp.Matrix, d: sp.Matrix) -> sp.Matrix:
    return sp.diag(a, d)


n = 3
A = sp.Matrix([[1, 2], [0, 1]])
L = A.inv()
D = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
C = sp.Matrix([[1, -1], [2, 3], [-2, 1]])
O23 = sp.zeros(2, 3)

a = A.row_join(O23).col_join(C.row_join(D))
Tsmall = sum((D**k * C * L**(k + 1) for k in range(n)), sp.zeros(3, 2))
T = sp.zeros(5)
T[2:5, 0:2] = Tsmall
u = sp.eye(5) + T
uinv = sp.eye(5) - T

assert T * T == sp.zeros(5)
assert Tsmall * A - D * Tsmall == C
assert uinv * u == sp.eye(5)
assert uinv * a * u == block_diag(A, D)

p = sp.diag(0, 0, 1, 1, 1)
q = u * p * uinv
assert q * q == q
assert a * q == q * a
assert (a * q) ** n == sp.zeros(5)

Lbig = block_diag(L, sp.zeros(3))
z = u * Lbig * uinv
assert a * z * a == z * a**2
assert z**2 * a == z
assert z * a ** (n + 1) == a**n

# a^n is group invertible; conjugate the obvious group inverse of A^n+0.
b = a**n
x = u * block_diag(A**(-n), sp.zeros(3)) * uinv
assert b * x * b == x * b**2
assert x**2 * b == x
assert x * b**2 == b

print("n =", n)
print("T A - D T - C =")
print(Tsmall * A - D * Tsmall - C)
print("rank(a^n) =", b.rank())
print("(a q)^n is zero:", (a * q) ** n == sp.zeros(5))
print("constructed z satisfies all left-Drazin equations:", True)
print("constructed x satisfies all left-group equations for a^n:", True)
print("all exact checks passed")
