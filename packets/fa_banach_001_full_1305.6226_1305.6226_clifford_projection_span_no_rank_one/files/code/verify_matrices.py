#!/usr/bin/env python3
"""Exact verification for the seven-projection Clifford construction."""

import sympy as sp


def hs(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.trace(a.T * b)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
Y = sp.Matrix([[0, -1], [1, 0]])
I4 = sp.eye(4)

A = [sp.kronecker_product(Z, I2),
     sp.kronecker_product(X, I2),
     sp.kronecker_product(Y, Y)]

Q = [sp.kronecker_product(I2, X),
     sp.kronecker_product(I2, Z),
     sp.kronecker_product(X, X),
     sp.kronecker_product(X, Z),
     sp.kronecker_product(Z, X),
     sp.kronecker_product(Z, Z)]

P = [(I4 + Q[0]) / 2, (I4 - Q[0]) / 2]
P.extend((I4 + q) / 2 for q in Q[1:])

# Clifford identities.
assert all(a == a.T for a in A)
assert all(a * a == I4 for a in A)
assert all(A[i] * A[j] + A[j] * A[i] == sp.zeros(4)
           for i in range(3) for j in range(i + 1, 3))

a, b, c = sp.symbols("a b c", real=True)
C = a * A[0] + b * A[1] + c * A[2]
assert sp.simplify(C * C - (a**2 + b**2 + c**2) * I4) == sp.zeros(4)
assert sp.factor(C.det()) == (a**2 + b**2 + c**2) ** 2

# S = K^perp has the displayed Hilbert--Schmidt orthogonal basis.
S_basis = [I4] + Q
assert all(m == m.T for m in S_basis)
gram_s = sp.Matrix([[hs(u, v) for v in S_basis] for u in S_basis])
assert gram_s == 4 * sp.eye(7)
assert all(hs(u, v) == 0 for u in A for v in S_basis)

# The seven P_i are rank-two orthogonal projections and span S.
assert all(p == p.T and p * p == p and p.rank() == 2 for p in P)
vec_p = sp.Matrix.hstack(*[p.reshape(16, 1) for p in P])
assert vec_p.rank() == 7
vec_s = sp.Matrix.hstack(*[s.reshape(16, 1) for s in S_basis])
assert vec_s.row_join(vec_p).rank() == 7

# Their Hilbert--Schmidt measurement kernel inside Sym_4 is exactly K.
sym_basis = []
for i in range(4):
    for j in range(i, 4):
        e = sp.zeros(4)
        e[i, j] = 1
        e[j, i] = 1
        if i == j:
            e[i, j] = 1
        sym_basis.append(e)
measurement = sp.Matrix([[hs(p, e) for e in sym_basis] for p in P])
assert measurement.rank() == 7
assert all(measurement * sp.Matrix([hs(e, aa) / hs(e, e)
                                    for e in sym_basis]) == sp.zeros(7, 1)
           for aa in A)

# The three quadratic forms obey the Hopf identity, so S has no nonzero zz^T.
x = sp.Matrix(sp.symbols("x1:5", real=True))
q = [sp.expand((x.T * aa * x)[0]) for aa in A]
hopf = sp.expand(sum(qi**2 for qi in q) - (x.dot(x))**2)
assert hopf == 0

print("A quadratic forms:")
for qi in q:
    print(" ", qi)
print("det(a A1+b A2+c A3) =", sp.factor(C.det()))
print("rank(span(P_i)) =", vec_p.rank())
print("rank(measurement map on Sym_4) =", measurement.rank())
print("Hopf remainder =", hopf)
print("all exact checks passed")
