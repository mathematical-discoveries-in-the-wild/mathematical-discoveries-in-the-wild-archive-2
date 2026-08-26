#!/usr/bin/env python3
"""Exact checks for the S_3 regular-action counterexample."""

from itertools import permutations

import sympy as sp


def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def permutation_matrix(p):
    matrix = sp.zeros(3)
    for i, image in enumerate(p):
        matrix[image, i] = 1
    return matrix


group = list(permutations(range(3)))
index = {g: i for i, g in enumerate(group)}
rho = {g: permutation_matrix(g) for g in group}

a = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
b = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
c = a + b
E = sp.Matrix.hstack(a, b)


def coefficient_matrix(q):
    # Columns are v=a,b; rows are g in S_3; F_q(v)(g)=v^T rho(g)q.
    return sp.Matrix(
        [[sp.simplify(v.dot(rho[g] * q)) for v in (a, b)] for g in group]
    )


def left_translation(h):
    # (U_h f)(g)=f(h^{-1}g).
    matrix = sp.zeros(6)
    h_inv = inverse(h)
    for g in group:
        matrix[index[g], index[compose(h_inv, g)]] = 1
    return matrix


A = coefficient_matrix(a)
B = coefficient_matrix(b)
C = coefficient_matrix(c)

assert A.rank() == B.rank() == C.rank() == 2
assert sp.simplify(C - A - B) == sp.zeros(6, 2)
assert sp.simplify(A.T * A / 6 - sp.eye(2) / 2) == sp.zeros(2)
assert sp.simplify(B.T * B / 6 - sp.eye(2) / 2) == sp.zeros(2)
assert sp.simplify(A.T * B / 6) == sp.zeros(2)
assert sp.simplify(A.T * C / 6 - sp.eye(2) / 2) == sp.zeros(2)
assert sp.Matrix.hstack(A, C).rank() == 4

for h in group:
    R_h = sp.simplify(E.T * rho[h] * E)
    assert sp.simplify(left_translation(h) * A - A * R_h) == sp.zeros(6, 2)
    assert sp.simplify(left_translation(h) * B - B * R_h) == sp.zeros(6, 2)
    assert sp.simplify(left_translation(h) * C - C * R_h) == sp.zeros(6, 2)

# The commutant of the two generating transpositions is one-dimensional,
# which certifies irreducibility of this unitary two-dimensional representation.
s = (1, 0, 2)
t = (0, 2, 1)
R_s = sp.simplify(E.T * rho[s] * E)
R_t = sp.simplify(E.T * rho[t] * E)
x11, x12, x21, x22 = sp.symbols("x11 x12 x21 x22")
X = sp.Matrix([[x11, x12], [x21, x22]])
equations = list(X * R_s - R_s * X) + list(X * R_t - R_t * X)
solution = sp.linsolve(equations, (x11, x12, x21, x22))
assert solution == sp.FiniteSet((x22, 0, 0, x22))

print("S_3 elements:", len(group))
print("rank(M_a)=rank(M_b)=rank(M_c)=2")
print("M_a is orthogonal to M_b")
print("M_a and M_c are distinct and nonorthogonal")
print("all exact invariance and irreducibility checks pass")
