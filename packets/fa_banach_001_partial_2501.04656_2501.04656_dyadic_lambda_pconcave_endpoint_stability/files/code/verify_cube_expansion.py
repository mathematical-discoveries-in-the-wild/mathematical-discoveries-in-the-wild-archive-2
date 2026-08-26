#!/usr/bin/env python3
"""Symbolic checks for the homothetic-cube sharpness calculation."""

import sympy as sp


eps, lam, n, p = sp.symbols("eps lam n p", positive=True)

# For p != 0, log(1+deficit) is more stable to differentiate than the
# expression itself.  Its first derivative vanishes at eps=0, so its second
# derivative is also the quadratic coefficient of the original expression.
log_factor = n * sp.log(1 + lam * eps) + sp.log(
    lam * (1 + eps) ** (-n * p) + 1 - lam
) / p

first = sp.simplify(sp.diff(log_factor, eps).subs(eps, 0))
second = sp.factor(sp.diff(log_factor, eps, 2).subs(eps, 0))
expected = n * (n * p + 1) * lam * (1 - lam)

assert first == 0
assert sp.simplify(second - expected) == 0

# The p=0 (Prékopa--Leindler) limit is checked independently.
log_factor_zero = n * sp.log(1 + lam * eps) - n * lam * sp.log(1 + eps)
first_zero = sp.simplify(sp.diff(log_factor_zero, eps).subs(eps, 0))
second_zero = sp.factor(sp.diff(log_factor_zero, eps, 2).subs(eps, 0))

assert first_zero == 0
assert sp.simplify(second_zero - n * lam * (1 - lam)) == 0

# The exact L1 distance between the two nested uniform densities is
# 2(1-(1+eps)^(-n)); its linear coefficient is 2n.
distance = 2 * (1 - (1 + eps) ** (-n))
distance_linear = sp.simplify(sp.diff(distance, eps).subs(eps, 0))
assert distance_linear == 2 * n

print("p != 0 first derivative: PASS (0)")
print(f"p != 0 second derivative: PASS ({second})")
print(f"p = 0 second derivative: PASS ({second_zero})")
print(f"L1 distance linear coefficient: PASS ({distance_linear})")

