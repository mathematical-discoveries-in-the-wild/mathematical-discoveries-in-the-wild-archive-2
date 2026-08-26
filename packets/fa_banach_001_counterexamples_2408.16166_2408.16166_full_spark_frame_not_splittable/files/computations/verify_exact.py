#!/usr/bin/env python3
"""Exact rational audit for the 2408.16166 splittability counterexample."""

from fractions import Fraction as Q


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def scale(t, u):
    return (t * u[0], t * u[1])


a = (Q(-7, 25), Q(-24, 25))
b = (Q(1), Q(0))
c = (Q(20, 29), Q(-21, 29))
atoms = (a, b, c)

u1 = (Q(1), Q(3, 4))
u2 = (Q(-3, 11), Q(37, 33))
u3 = (Q(-1), Q(3, 7))
facets = (u1, u2, u3)


def norm(z):
    return max(abs(dot(u, z)) for u in facets)


def distances(z):
    z1, z2 = z
    return (
        abs(24 * z1 - 7 * z2) / 24,
        25 * abs(z2) / 24,
        25 * abs(21 * z1 + 20 * z2) / 627,
    )


assert all(dot(v, v) == 1 for v in atoms)
assert (det(a, b), det(a, c), det(b, c)) == (
    Q(24, 25), Q(627, 725), Q(-21, 29)
)
assert all(max(abs(dot(u, v)) for v in atoms) == 1 for u in facets)
assert all(norm(v) == 1 for v in atoms)

x = (Q(-4, 5), Q(3, 5))
y = (Q(7, 15), Q(-8, 15))
x1 = scale(Q(-1131, 1045), c)
y1 = scale(Q(6496, 9405), c)
rx = sub(x, x1)
ry = sub(y, y1)
assert distances(x) == (Q(39, 40), Q(5, 8), Q(40, 209))
assert distances(y) == (Q(28, 45), Q(5, 9), Q(65, 1881))
assert rx == scale(Q(40, 209), a)
assert ry == scale(Q(65, 1881), a)
assert norm(add(x, y)) == Q(38, 105)
l1 = norm(add(x, y)) - norm(x1) + norm(y1)
d1 = norm(ry) - norm(rx)
assert (l1, d1, l1 / d1) == (Q(-391, 13167), Q(-295, 1881), Q(391, 2065))

xp = b
yp = (Q(-3, 10), Q(-1, 5))
xp1 = b
yp1 = (Q(-29, 120), Q(0))
rxp = sub(xp, xp1)
ryp = sub(yp, yp1)
assert distances(yp) == (Q(29, 120), Q(5, 24), Q(515, 1254))
assert ryp == scale(Q(5, 24), a)
assert norm(add(xp, yp)) == Q(11, 14)
l2 = norm(add(xp, yp)) - norm(xp1) + norm(yp1)
d2 = norm(ryp) - norm(rxp)
assert (l2, d2, l2 / d2) == (Q(23, 840), Q(5, 24), Q(23, 175))
assert l1 / d1 - l2 / d2 == Q(598, 10325) > 0

print("full_spark_minors", det(a, b), det(a, c), det(b, c))
print("witness_1", "L=", l1, "D=", d1, "beta>=", l1 / d1)
print("witness_2", "L=", l2, "D=", d2, "beta<=", l2 / d2)
print("incompatibility_gap", l1 / d1 - l2 / d2)
print("PASS: all exact rational checks succeeded")
