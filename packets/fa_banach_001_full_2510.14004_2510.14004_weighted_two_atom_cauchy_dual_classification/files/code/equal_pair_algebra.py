#!/usr/bin/env python3
"""Exact quadratic-extension algebra for the equal-weight case.

Elements are represented as u+v*x with x+1/x=2*t.  This keeps the
unit-circle conjugation and the Fejer relation small enough for exact
factorization.
"""

import sympy as s

b, c, t = s.symbols("b c t", nonzero=True, real=True)
a = b * (c + 2) / (b + 1)
t_phys = s.factor((4 * b * (c + 1) - b**2 - 1 - 2 * a**2) / (2 * (a**2 - b)))


def simp(q):
    return s.factor(s.cancel(q).subs(t, t_phys))


class Q:
    def __init__(self, u=0, v=0):
        self.u = simp(u)
        self.v = simp(v)

    def __add__(self, other):
        other = asq(other)
        return Q(self.u + other.u, self.v + other.v)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.u, -self.v)

    def __sub__(self, other):
        return self + (-asq(other))

    def __rsub__(self, other):
        return asq(other) - self

    def __mul__(self, other):
        other = asq(other)
        return Q(
            self.u * other.u - self.v * other.v,
            self.u * other.v + self.v * other.u + 2 * t * self.v * other.v,
        )

    __rmul__ = __mul__

    def conj(self):
        return Q(self.u + 2 * t * self.v, -self.v)

    def inv(self):
        norm = simp(self.u**2 + 2 * t * self.u * self.v + self.v**2)
        z = self.conj()
        return Q(z.u / norm, z.v / norm)

    def __truediv__(self, other):
        return self * asq(other).inv()

    def __rtruediv__(self, other):
        return asq(other) / self

    def __repr__(self):
        return f"({self.u}) + ({self.v})*x"


def asq(x):
    return x if isinstance(x, Q) else Q(x, 0)


one = Q(1)
x = Q(0, 1)
scoef = a * (one + x)
pcoef = b * x

def qeval(z):
    return z * z - scoef * z + pcoef

q1 = qeval(one)
qx = qeval(x)
qprime1 = 2 * one - scoef
qprimex = 2 * x - scoef
n1_slope = q1 / (one - x)
n2_slope = qx / (x - one)

c11 = c * (one / (one - x) - qprime1 / q1)
c22 = c * x * (one / (x - one) - qprimex / qx)

# O'(1) conjugate(O'(x)) (1-conjugate(x)); sqrt(b)^2=b.
o1_without_sqrt = (one - x) / q1
o2_without_sqrt = (x - one) / qx
c12 = one / (b * o1_without_sqrt * o2_without_sqrt.conj() * (one - x.conj()))
c21 = c12.conj()
detc = c11 * c22 - c12 * c21

ci11 = c22 / detc
ci12 = -c12 / detc
ci21 = -c21 / detc
ci22 = c11 / detc

A = n1_slope
B = n2_slope
R11 = (
    ci11 * A * A.conj()
    + ci12 * B * A.conj()
    + ci21 * A * B.conj()
    + ci22 * B * B.conj()
)
a22 = Q(1 - b) + R11
F = a * a22 - 2 * b * c

for name, value in [
    ("t_phys", Q(t_phys)),
    ("c11", c11),
    ("c22", c22),
    ("c12", c12),
    ("detc", detc),
    ("R11", R11),
    ("a22", a22),
    ("a*a22-2bc", F),
]:
    print(name, value)
