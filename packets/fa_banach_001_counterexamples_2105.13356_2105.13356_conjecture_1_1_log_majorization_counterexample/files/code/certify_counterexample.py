#!/usr/bin/env python3
"""Exact rational ball certificate for a 4x4 counterexample.

All error bounds are operator-norm bounds obtained from exact rational
Frobenius estimates.  Floating-point arithmetic is used only to choose ball
centres; every accepted inequality is then checked over the rational balls.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

import mpmath as mp


N = 4
BITS = 320
DIGITS = 70
mp.mp.dps = 130


def zero():
    return [[F(0) for _ in range(N)] for _ in range(N)]


def eye():
    a = zero()
    for i in range(N):
        a[i][i] = F(1)
    return a


def transpose(a):
    return [[a[j][i] for j in range(N)] for i in range(N)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(N)] for i in range(N)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(N)] for i in range(N)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(N)), F(0))
             for j in range(N)] for i in range(N)]


def matvec(a, v):
    return [sum((a[i][j] * v[j] for j in range(N)), F(0)) for i in range(N)]


def inverse(a):
    aug = [a[i][:] + eye()[i] for i in range(N)]
    for col in range(N):
        pivot = next(i for i in range(col, N) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for i in range(N):
            if i != col:
                q = aug[i][col]
                if q:
                    aug[i] = [aug[i][j] - q * aug[col][j]
                              for j in range(2 * N)]
    return [row[N:] for row in aug]


def ceil_sqrt_fraction(x: F) -> F:
    assert x >= 0
    if not x:
        return F(0)
    scale = 1 << BITS
    q = (x.numerator * scale * scale) // x.denominator
    r = isqrt(q)
    if F(r * r, scale * scale) < x:
        r += 1
    return F(r, scale)


def floor_sqrt_fraction(x: F) -> F:
    assert x >= 0
    if not x:
        return F(0)
    scale = 1 << BITS
    q = (x.numerator * scale * scale) // x.denominator
    return F(isqrt(q), scale)


def frob_up(a) -> F:
    return ceil_sqrt_fraction(sum((x * x for row in a for x in row), F(0)))


def vec_norm_up(v) -> F:
    return ceil_sqrt_fraction(sum((x * x for x in v), F(0)))


def vec_norm_low(v) -> F:
    return floor_sqrt_fraction(sum((x * x for x in v), F(0)))


def spd_pivots(a):
    """Exact LDL^T pivots; positivity is equivalent to SPD."""
    l = [[F(int(i == j)) for j in range(N)] for i in range(N)]
    d = [F(0)] * N
    for j in range(N):
        d[j] = a[j][j] - sum((l[j][k] ** 2 * d[k] for k in range(j)), F(0))
        if d[j] <= 0:
            return d
        for i in range(j + 1, N):
            l[i][j] = (a[i][j] - sum((l[i][k] * l[j][k] * d[k]
                                      for k in range(j)), F(0))) / d[j]
    return d


def lambda_min_lower(a) -> F:
    assert all(x > 0 for x in spd_pivots(a))
    return F(1, 1) / frob_up(inverse(a))


def to_mp(a):
    return mp.matrix([[mp.mpf(x.numerator) / x.denominator for x in row] for row in a])


def round_mp_matrix(a):
    scale = mp.mpf(10) ** DIGITS
    out = zero()
    for i in range(N):
        for j in range(N):
            out[i][j] = F(int(mp.nint(a[i, j] * scale)), 10 ** DIGITS)
    # Force exact symmetry after independent decimal rounding.
    for i in range(N):
        for j in range(i):
            out[i][j] = out[j][i] = (out[i][j] + out[j][i]) / 2
    return out


def approximate_sqrt(a):
    vals, q = mp.eigsy((to_mp(a) + to_mp(a).T) / 2)
    r = q * mp.diag([mp.sqrt(v) for v in vals]) * q.T
    return round_mp_matrix(r)


@dataclass
class Ball:
    c: list
    e: F
    label: str

    @staticmethod
    def exact(c, label):
        return Ball(c, F(0), label)

    def norm_up(self):
        return frob_up(self.c) + self.e

    def __matmul__(self, other):
        nc = mul(self.c, other.c)
        ne = (frob_up(self.c) * other.e + frob_up(other.c) * self.e
              + self.e * other.e)
        return Ball(nc, ne, f"({self.label}{other.label})")

    def inv(self):
        ci = inverse(self.c)
        ni = frob_up(ci)
        q = ni * self.e
        assert q < 1
        return Ball(ci, ni * ni * self.e / (1 - q), f"{self.label}^-1")

    def sqrt(self):
        r = approximate_sqrt(self.c)
        assert all(x > 0 for x in spd_pivots(r))
        lc = lambda_min_lower(self.c)
        assert lc > self.e
        residual = frob_up(sub(mul(r, r), self.c)) + self.e
        denominator = lambda_min_lower(r) + floor_sqrt_fraction(lc - self.e)
        er = residual / denominator
        return Ball(r, er, f"sqrt({self.label})")


def repeated_roots(a: Ball):
    a2 = a.sqrt()
    a4 = a2.sqrt()
    a8 = a4.sqrt()
    a16 = a8.sqrt()
    return a2, a4, a8, a16


def decimal(x: F, places=24):
    return mp.nstr(mp.mpf(x.numerator) / x.denominator, places)


A = [[F(x) for x in row] for row in [
    [17825066, 0, 0, 0],
    [0, 83, 0, 0],
    [0, 0, 24, 0],
    [0, 0, 0, 10],
]]
B = [[F(x) for x in row] for row in [
    [117567, -99513, 2310, -38624],
    [-99513, 131686, 572, 24611],
    [2310, 572, 190, -1191],
    [-38624, 24611, -1191, 14107],
]]

assert all(x > 0 for x in spd_pivots(A))
assert all(x > 0 for x in spd_pivots(B))

a = Ball.exact(A, "A")
b = Ball.exact(B, "B")
a2, a4, a8, a16 = repeated_roots(a)
b2, b4, b8, b16 = repeated_roots(b)
a15 = a2 @ a4 @ a8 @ a16
ainv2 = a2.inv()
m = ainv2 @ b @ ainv2
m2, m4, m8, m16 = repeated_roots(m)
m15 = m2 @ m4 @ m8 @ m16
g = a2 @ m15 @ a2
x = a15 @ g @ b16

# A rational trial vector chosen from the least right singular vector of the
# ball centre.  Its Rayleigh quotient gives an upper bound on s_min(X).
xc = to_mp(x.c)
vals, q = mp.eigsy((xc.T * xc + (xc.T * xc).T) / 2)
approx_smin_x = mp.sqrt(vals[0])
scale = mp.mpf(10) ** 50
w = [F(int(mp.nint(q[i, 0] * scale)), 10 ** 50) for i in range(N)]
upper_x = vec_norm_up(matvec(x.c, w)) / vec_norm_low(w) + x.e

# Set an exact rational threshold just above the certified upper bound, and
# prove s_min(AB) exceeds it by exact LDL^T positivity.
threshold = F(1179, 5)  # 235.8
ab = mul(A, B)
c_ab = mul(transpose(ab), ab)
approx_smin_ab = mp.sqrt(mp.eigsy(to_mp(c_ab), eigvals_only=True)[0])
test = sub(c_ab, [[threshold * threshold if i == j else F(0)
                   for j in range(N)] for i in range(N)])
pivots = spd_pivots(test)

print("A SPD pivots positive:", all(v > 0 for v in spd_pivots(A)))
print("B SPD pivots positive:", all(v > 0 for v in spd_pivots(B)))
print("X ball radius <=", decimal(x.e, 30))
print("approximate s_min(X) =", mp.nstr(approx_smin_x, 30))
print("approximate s_min(AB) =", mp.nstr(approx_smin_ab, 30))
print("approximate prefix-3 ratio =", mp.nstr(approx_smin_ab / approx_smin_x, 30))
print("certified s_min(X) <=", decimal(upper_x, 30))
print("threshold =", decimal(threshold, 30))
print("(AB)^T(AB)-threshold^2 I SPD:", all(v > 0 for v in pivots))
print("smallest normalized LDL pivot sign check:",
      min((p / (1 + abs(p)) for p in pivots)))
assert upper_x < threshold
assert all(v > 0 for v in pivots)
print("CERTIFIED: s_min(X) < threshold < s_min(AB)")
