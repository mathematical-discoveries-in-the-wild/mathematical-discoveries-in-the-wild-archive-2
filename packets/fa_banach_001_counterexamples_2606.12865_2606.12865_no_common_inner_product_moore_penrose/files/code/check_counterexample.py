"""Exact regression checks for the arXiv:2606.12865 counterexample."""

import sympy as sp


phi = (1 + sp.sqrt(5)) / 2
a = sp.sqrt(phi)
delta = 1 - phi

T = sp.Matrix([[a, 0], [1, 0]])
I = sp.eye(2)
beta2 = T.adjoint() ** 2 * T**2 - 2 * T.adjoint() * T + I
S = 2 * T.adjoint() - T.adjoint() ** 2 * T
P = sp.simplify(S * T)
Q = sp.simplify(T * S)

assert sp.simplify(phi**2 - phi - 1) == 0
assert sp.simplify(delta * phi + 1) == 0
assert sp.simplify(beta2 - sp.diag(0, 1)) == sp.zeros(2)
assert sp.simplify(T * beta2) == sp.zeros(2)
assert sp.simplify(S - sp.Matrix([[a * delta, 2], [0, 0]])) == sp.zeros(2)
assert P == sp.diag(1, 0)
assert sp.simplify(Q - sp.Matrix([[-1, 2 * a], [a * delta, 2]])) == sp.zeros(2)
assert sp.simplify(T * S * T - T) == sp.zeros(2)
assert sp.simplify(S * T * S - S) == sp.zeros(2)

# A general Hermitian G.  P^*G=GP forces the off-diagonal variable z to zero.
x, y = sp.symbols("x y", positive=True, real=True)
z, zbar = sp.symbols("z zbar")
G = sp.Matrix([[x, z], [zbar, y]])
eq_P = sp.simplify(P.adjoint() * G - G * P)
assert eq_P == sp.Matrix([[0, z], [-zbar, 0]])

G_diag = sp.diag(x, y)
eq_Q = sp.simplify(Q.adjoint() * G_diag - G_diag * Q)
assert sp.simplify(eq_Q[0, 1] - a * (delta * y - 2 * x)) == 0
assert sp.simplify(eq_Q[1, 0] + a * (delta * y - 2 * x)) == 0
assert delta.is_negative

print("PASS: all exact matrix identities and the sign obstruction verified")
