"""Exact checks for the arXiv:2111.15180 Schatten counterexample packet."""

import mpmath as mp
import sympy as sp


A = sp.diag(sp.Rational(2, 5), sp.Rational(5, 2), 6)
C = sp.diag(sp.Rational(5, 2), sp.Rational(2, 5), 6)
N = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
B = N.T * C * N
H = A.row_join(N).col_join(N.T.row_join(B))
S = A + B

assert N.T * N == sp.eye(3) == N * N.T
assert B == sp.diag(6, sp.Rational(5, 2), sp.Rational(2, 5))
assert sorted(H.eigenvals().keys()) == [0, sp.Rational(29, 10), 5, 7]
assert H.eigenvals() == {0: 2, sp.Rational(29, 10): 2, 5: 1, 7: 1}
assert S.eigenvals() == {sp.Rational(32, 5): 2, 5: 1}

mp.mp.dps = 60
g = lambda p: (mp.mpf(35) / 32) ** p + 2 * (mp.mpf(29) / 64) ** p - 2
q_star = mp.findroot(g, (mp.mpf("7.7"), mp.mpf("7.8")))
assert g(mp.mpf("7.70998")) < 0 < g(mp.mpf("7.71000"))
assert g(8) > 0 and g(2) < 0

print("B =", B)
print("spectrum(H) =", H.eigenvals())
print("spectrum(A+B) =", S.eigenvals())
print("q_star =", mp.nstr(q_star, 50))
print("g(7.70998) =", mp.nstr(g(mp.mpf("7.70998")), 20))
print("g(7.71000) =", mp.nstr(g(mp.mpf("7.71000")), 20))

