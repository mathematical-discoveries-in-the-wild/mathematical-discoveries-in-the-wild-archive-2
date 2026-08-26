#!/usr/bin/env python3
"""Directed-interval certificate for the Appendix C counterexample.

Only the 5 x 5 candidate sum is used as a lower bound.  The complete
hexagonal sum is bounded above by its 5 x 5 square plus the analytic
one-dimensional Gaussian-tail bound proved in the packet.
"""

from mpmath import iv


iv.dps = 60
I = iv.mpf
N = 2


def quadratic_form(x, y, z1, z2, k, ell):
    u = I(k) + z1
    v = I(ell) + z2
    return (u * u + 2 * x * u * v + (x * x + y * y) * v * v) / y


def finite_theta(x, y, z1, z2):
    return sum(
        (
            iv.exp(-iv.pi * quadratic_form(x, y, z1, z2, k, ell))
            for k in range(-N, N + 1)
            for ell in range(-N, N + 1)
        ),
        I(0),
    )


# Counterexample lattice and the globally admissible selector from the packet.
x = I(9) / 20
y = iv.sqrt(319) / 20
g = 4 * x * (1 - x)  # exactly 99/100
z2 = I(1) / 2 - g**100 / (8 * y * y)
z1 = I(1) / 2 - x * z2
candidate_square = finite_theta(x, y, z1, z2)

# Hexagonal lattice, where the deep hole is (1/3,1/3).
x_hex = I(1) / 2
y_hex = iv.sqrt(3) / 2
hex_square = finite_theta(x_hex, y_hex, I(1) / 3, I(1) / 3)

# q_hex(u,v) >= (u^2+v^2)/sqrt(3).  Bound the complement of the
# [-N,N]^2 square by a union of two separable one-dimensional tails.
c = iv.pi / iv.sqrt(3)
tail_1d = 2 * iv.exp(-c * (I(N) + I(2) / 3) ** 2) / (
    1 - iv.exp(-c * (2 * I(N) + I(7) / 3))
)
inside_1d = sum(
    (iv.exp(-c * (I(k) + I(1) / 3) ** 2) for k in range(-N, N + 1)),
    I(0),
)
hex_tail_bound = 2 * (inside_1d + tail_1d) * tail_1d
certified_gap = candidate_square - hex_square - hex_tail_bound

print("x =", x)
print("y =", y)
print("z1 =", z1)
print("z2 =", z2)
print("candidate 5x5 lower enclosure =", candidate_square)
print("hexagonal 5x5 enclosure =", hex_square)
print("one-dimensional tail bound =", tail_1d)
print("hexagonal two-dimensional tail bound =", hex_tail_bound)
print("certified lower enclosure for reversed gap =", certified_gap)

assert bool(certified_gap.a > I(0)), "the certified gap must be positive"
print("PASS: theta_L(tilde z;1) > theta_hex((1/3,1/3);1)")

