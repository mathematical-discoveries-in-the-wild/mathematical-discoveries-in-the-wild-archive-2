"""Exact symbolic certificate for the ellipsoid trace telescoping identity."""

import sympy as sp


m, n, lam, r = sp.symbols("m n lam r", integer=True, nonnegative=True)
s = m + 2 * n + lam

c11 = (2 * n + lam - 1) / (s * (s - 1))
c22 = (2 * n + 2) * (2 * n + 3) / (s * (s + 1)) - (
    (2 * n) * (2 * n + 1) / ((s - 2) * (s - 1))
)
p_squared = 4 * (m + 1) * (2 * n) * (2 * n + 1) / (
    (s - 1) * s**2 * (s - 2) ** 2
)
q_squared = 4 * m * (2 * n + 2) * (2 * n + 3) / (
    s * (s + 1) ** 2 * (s - 1) ** 2
)
chi = sp.cancel(2 * c11 * c22 - p_squared - q_squared)

# The four-term expression printed in the source paper.
source_chi = (
    -2
    * n
    * (2 * n + 1)
    * (2 * m + 2 * n + lam - 1)
    / ((s - 2) ** 2 * (s - 1) ** 2)
    + (2 * n + 2)
    * (2 * n + 3)
    * (2 * m + 2 * n + lam + 1)
    / (s**2 * (s + 1) ** 2)
    + 2
    * (m + 1)
    * ((2 * n + 1) * (m + lam - 1) + 2 * (n + 1) * (m + 2 * n + lam - 1))
    / ((s - 1) * s**2 * (s + 1))
    - 2
    * m
    * ((2 * n + 1) * (m + lam - 2) + 2 * (n + 1) * (m + 2 * n + lam - 2))
    / ((s - 2) * (s - 1) ** 2 * s)
)
assert sp.cancel(chi - source_chi) == 0

even_shell = sp.summation(sp.cancel(chi.subs(m, 2 * r - 2 * n)), (n, 0, r))
odd_shell = sp.summation(
    sp.cancel(chi.subs(m, 2 * r + 1 - 2 * n)), (n, 0, r)
)
shell = sp.cancel(even_shell + odd_shell)

x = lam + 2 * r
a = -(lam - 4) * (lam - 2) * (lam**2 - 8 * lam + 18) / 24
a0 = -(lam - 2) * (2 * lam**2 - 11 * lam + 18) / 6
b = -(lam - 3) * (lam - 1) * (lam**2 - 6 * lam + 11) / 6
c = (3 * lam**4 - 30 * lam**3 + 96 * lam**2 - 88 * lam - 28) / 24
c0 = -(3 * lam**4 - 30 * lam**3 + 96 * lam**2 - 96 * lam - 8) / 12
e = 2 * (2 * lam - 5) / 3

potential = (
    a / (x - 2) ** 2
    + (a + a0) / x**2
    + b / (x - 1) ** 2
    + c / (x - 2)
    + (c + c0) / x
    + e / (x - 1)
)

assert sp.cancel(shell - (potential - potential.subs(r, r + 1))) == 0
assert sp.simplify(potential.subs(r, 0) - sp.Rational(2, 3)) == 0
assert sp.limit(potential, r, sp.oo) == 0

volume = 4 * sp.pi**2 * sp.integrate(
    sp.Symbol("rho") * (1 - sp.Symbol("rho") ** 2) ** 2 / 2,
    (sp.Symbol("rho"), 0, 1),
)
assert sp.simplify(volume - sp.pi**2 / 3) == 0

print("source eigenvalue identity: verified")
print("shell identity B_r = F_r - F_{r+1}: verified")
print("F_0 =", sp.simplify(potential.subs(r, 0)))
print("lim F_r =", sp.limit(potential, r, sp.oo))
print("ellipsoid volume =", volume)
print("trace = 2/3 = (2/pi^2) volume")
