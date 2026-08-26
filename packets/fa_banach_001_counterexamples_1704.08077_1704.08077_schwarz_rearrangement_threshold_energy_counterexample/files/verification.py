"""Independent check of the interval sums and the rigorous radical bound."""

from fractions import Fraction
from math import inf, isinf, log, sqrt


P = 1.5


def pair_integral(a, b, c, d):
    """Integral over [a,b] x [c,d] of (y-x)^(-1-P), for b<c."""
    q = 1.0 - P
    value = (c - a) ** q - (c - b) ** q
    if not isinf(d):
        value -= (d - a) ** q - (d - b) ** q
    return value / (P * q)


def energy(regions):
    """Ordered-pair threshold energy for disjoint (left,right,value) regions."""
    left = min(a for a, _, _ in regions)
    right = max(b for _, b, _ in regions)
    regions = [(-inf, left, 0)] + sorted(regions) + [(right, inf, 0)]
    total = 0.0
    for i, (a, b, first) in enumerate(regions):
        for c, d, second in regions[i + 1 :]:
            if abs(first - second) <= 1:
                continue
            if isinf(-a):
                contribution = pair_integral(-d, -c, -b, inf)
            else:
                contribution = pair_integral(a, b, c, d)
            total += 2.0 * contribution
    return total


u = [
    (-15, -14, 1),
    (-14, 7, 2),
    (7, 8, 3),
    (8, 10, 4),
    (10, 11, 3),
    (11, 14, 2),
    (14, 15, 1),
]

u_star = [
    (-15, -14, 1),
    (-14, -2, 2),
    (-2, -1, 3),
    (-1, 1, 4),
    (1, 2, 3),
    (2, 14, 2),
    (14, 15, 1),
]

e_u = energy(u)
e_star = energy(u_star)
assert e_star - e_u > 0.043

# Certified lower bound for the exact radical difference.  The positive
# radical terms use lower bounds and the negative radical terms upper bounds.
positive = {
    7: Fraction(264575, 100000),
    22: Fraction(4690415, 1000000),
    17: Fraction(4123105, 1000000),
    15: Fraction(3872983, 1000000),
}
negative = {
    13: Fraction(3605552, 1000000),
    6: Fraction(2449490, 1000000),
    2: Fraction(1414214, 1000000),
    21: Fraction(4582576, 1000000),
    26: Fraction(5099020, 1000000),
}
assert all(bound * bound < radicand for radicand, bound in positive.items())
assert all(bound * bound > radicand for radicand, bound in negative.items())

lower = (
    Fraction(28, 15)
    + Fraction(8, 21) * positive[7]
    + Fraction(8, 33) * positive[22]
    + Fraction(16, 51) * positive[17]
    + Fraction(16, 45) * positive[15]
    - Fraction(32, 39) * negative[13]
    - Fraction(2, 3) * negative[6]
    - Fraction(2, 3) * negative[2]
    - Fraction(8, 63) * negative[21]
    - Fraction(4, 39) * negative[26]
)
assert lower == Fraction(1376155019, 31906875000)
assert lower > Fraction(43, 1000)

print(f"I_1(u)   = {e_u:.15f}")
print(f"I_1(u*)  = {e_star:.15f}")
print(f"difference = {e_star - e_u:.15f}")
print(f"certified lower bound = {lower} = {float(lower):.15f}")

