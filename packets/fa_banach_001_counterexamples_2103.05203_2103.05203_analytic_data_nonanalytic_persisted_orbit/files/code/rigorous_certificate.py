#!/usr/bin/env python3
"""Exact certificate for the Taylor obstruction used in the solution packet.

All finite Taylor arithmetic is rational.  The only infinite-tail estimates used
below are the explicit geometric majorants documented in the packet.
"""

from fractions import Fraction as Q
from math import factorial


N = 30
BETA = Q(1, 10)
Y0_BOUND = Q(10, 9)
B = Q(11, 10)
RHO = Q(1, 2)


def mul(p, q, degree=N):
    out = [Q(0)] * (degree + 1)
    for i, x in enumerate(p):
        if not x:
            continue
        for j, z in enumerate(q[: degree + 1 - i]):
            if z:
                out[i + j] += x * z
    return out


def affine_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def affine_scale(c, x):
    return (c * x[0], c * x[1])


# eta(t)=t+arctan(sin(t)), represented through degree N.  This choice comes
# from the globally bounded real-analytic delay r(u,v,z)=2*pi-arctan(v).
sin_series = [Q(0)] * (N + 1)
sin_series[1] = Q(1)
for n in range(3, N + 1, 2):
    sin_series[n] = Q((-1) ** ((n - 1) // 2), factorial(n))

atan_sin = [Q(0)] * (N + 1)
sin_power = sin_series[:]
sin_squared = mul(sin_series, sin_series)
for j in range((N + 1) // 2):
    coefficient = Q((-1) ** j, 2 * j + 1)
    for n in range(N + 1):
        atan_sin[n] += coefficient * sin_power[n]
    sin_power = mul(sin_power, sin_squared)

eta = atan_sin
eta[1] += Q(1)

eta_powers = [[Q(0)] * (N + 1) for _ in range(N + 1)]
eta_powers[0][0] = Q(1)
for k in range(1, N + 1):
    eta_powers[k] = mul(eta_powers[k - 1], eta)

# y_n = a_n*y(0)+b_n for the formal equation
# y'=-y+(1/10)y(t+arctan(sin t))+sin t.
y = [(Q(1), Q(0))]
w = []
for n in range(N + 1):
    scale = Q(factorial(n), 1) / (
        BETA**n * Q(2) ** (n * (n - 1) // 2)
    )
    w.append(affine_scale(scale, y[n]))
    if n == N:
        break
    comp = (Q(0), Q(0))
    for k in range(n + 1):
        comp = affine_add(comp, affine_scale(eta_powers[k][n], y[k]))
    h_n = Q(0)
    if n % 2 == 1:
        h_n = Q((-1) ** ((n - 1) // 2), factorial(n))
    rhs = affine_add(affine_scale(-1, y[n]), affine_scale(BETA, comp))
    rhs = affine_add(rhs, (Q(0), h_n))
    y.append(affine_scale(Q(1, n + 1), rhs))

a30, b30 = w[N]
lower_w30 = abs(b30) - Y0_BOUND * abs(a30)
max_w_to_30 = max(abs(b) + Y0_BOUND * abs(a) for a, b in w)

# For n>=30, the row sum in |w_{n+1}-w_n| is bounded by
# R_n = 10/2^n plus the nonlinear-composition terms.  With
# eta=2t(1+u).  On |t|=1/2, the elementary majorant
# |u(t)| <= (atanh(sinh(1/2))-1/2)/(2(1/2)) < 1/10.
# Cauchy's estimate therefore gives
# T(n,d)=B^(n-d)(10n/RHO)^d 2^{-d(2n-d+1)/2}, d even, d>=2.
# Log-convexity in d and the endpoint estimates proved in the packet imply
# sum_d T(n,d) <= floor(n/2)T(n,2).  The latter majorant has successive
# ratio <1/3 for n>=30.
def t2(n):
    return B ** (n - 2) * (Q(10 * n, 1) / RHO) ** 2 / Q(2 ** (2 * n - 1))


def endpoint(n):
    d = n if n % 2 == 0 else n - 1
    exponent = d * (2 * n - d + 1) // 2
    return B ** (n - d) * (Q(10 * n, 1) / RHO) ** d / Q(2**exponent)


assert endpoint(30) < t2(30)
assert endpoint(31) < t2(31)
# For either parity, the endpoint/T(n,2) quotient two rows later is at
# most 6400*n^2*(1+2/n)^n/2^(2n+3); use (1+2/n)^n<e^2<8.
assert Q(6400 * 30**2 * 8, 2 ** (2 * 30 + 3)) < 1
# The floor(n/2)T(n,2) row majorant has ratio <1/3 thereafter.
assert Q(31, 29) * B * Q(31**2, 30**2) / 4 < Q(1, 3)
composition_tail = Q(3, 2) * (N // 2) * t2(N)
alpha_tail = Q(10, 2 ** (N - 1))
row_sum_tail = alpha_tail + composition_tail

# Only odd n contribute forcing increments.  Their ratio two indices later is
# 100*2^{-(2n+3)}, so the tail from n=31 is less than twice its first term.
forcing_31 = Q(10**32, 2 ** (31 * 32 // 2))
forcing_tail = 2 * forcing_31

assert lower_w30 > 227
assert max_w_to_30 < 735
assert composition_tail < Q(1, 10**9)
assert row_sum_tail < Q(1, 50_000_000)
assert forcing_tail < Q(1, 10**100)

# If S=sum R_n and H=sum F_n, then all later |w_n| are bounded by
# (W_N+H)/(1-S), and the total displacement from w_N is at most
# S(W_N+H)/(1-S)+H.
tail_displacement = (
    row_sum_tail * (max_w_to_30 + forcing_tail) / (1 - row_sum_tail)
    + forcing_tail
)
assert tail_displacement < Q(1, 1000)


def decimal(q, digits=14):
    return f"{float(q):.{digits}g}"


print("exact Taylor obstruction certificate: PASS")
print("a_30 =", decimal(a30))
print("b_30 =", decimal(b30))
print("inf_{|y0|<=10/9} |w_30| >", decimal(lower_w30))
print("max_{k<=30, |y0|<=10/9} |w_k| <", decimal(max_w_to_30))
print("sum_{n>=30} R_n <", decimal(row_sum_tail))
print("sum_{n>=30} F_n <", decimal(forcing_tail))
print("|w_infinity-w_30| <", decimal(tail_displacement))
print("therefore |w_infinity| >", decimal(lower_w30 - tail_displacement))
