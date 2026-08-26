"""Exact verification for the H^6 backward-shift packet."""

import sympy as sp


a, c = sp.symbols("a c", real=True)
m = 3

# ||I_a-c||_6^6 = ||(I_a-c)^3||_2^2 and
# <I_a^j,I_a^k> = a^|j-k|.
D = sp.Integer(0)
for j in range(m + 1):
    for k in range(m + 1):
        D += (
            sp.binomial(m, j)
            * sp.binomial(m, k)
            * (-c) ** (2 * m - j - k)
            * a ** abs(j - k)
        )
D = sp.factor(D)

expected = (
    1
    + 9 * c**2
    + 9 * c**4
    + c**6
    - 6 * a * c
    - 18 * a * c**3
    - 6 * a * c**5
    + 6 * a**2 * c**2
    + 6 * a**2 * c**4
    - 2 * a**3 * c**3
)
assert sp.expand(D - expected) == 0
assert sp.factor(D.subs(c, a) - (1 - a**2) * (a**4 + 4 * a**2 + 1)) == 0

a0 = sp.Rational(32, 35)
c0 = sp.Rational(11, 28)
ratio6 = sp.factor(D.subs({a: a0, c: a0}) / D.subs({a: a0, c: c0}))
claimed = sp.Rational(6229716996096, 1533633162625)
assert ratio6 == claimed

phi = (1 + sp.sqrt(5)) / 2
lower = sp.N(ratio6 ** sp.Rational(1, 6), 16)
upper = sp.N(2 ** sp.Rational(1, 3) * phi ** sp.Rational(1, 6), 16)

print("D(a,c) =", D)
print("sixth-power ratio =", ratio6)
print("lower endpoint =", lower)
print("upper endpoint =", upper)
