"""Exact algebra check for the counterexample to arXiv:0801.1749, Problem 2."""

import sympy as sp

z, x, y = sp.symbols("z x y")

M = sp.Rational(99, 100) * sp.cosh(z) + sp.Rational(1, 100) * sp.exp(z**2 / 2)
N = sp.series(1 / M, z, 0, 8).removeO().expand()

inverse_image = sp.expand(
    sum(N.coeff(z, k) * sp.diff(x**6, x, k) for k in range(7))
)
expected = x**6 - 15 * x**4 + sp.Rational(747, 10) * x**2 - sp.Rational(3027, 50)
assert sp.expand(inverse_image - expected) == 0

R = 50 * y**3 - 750 * y**2 + 3735 * y - 3027
discriminant = sp.discriminant(R, y)
assert discriminant == -668_917_845_000

print("reciprocal_through_degree_6:", N)
print("inverse_image_x6:", inverse_image)
print("integer_cubic_discriminant:", discriminant)
