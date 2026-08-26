"""Exact checks for the one-generator Hankel witness in the packet."""

from fractions import Fraction

import sympy as sp


def expected_determinant(size: int) -> sp.Rational:
    q = sp.Rational(1, 4)
    diagonal_product_squared = sp.prod(
        sp.Rational(1, 2) ** (2 * j * j) for j in range(size)
    )
    vandermonde = sp.prod(
        q**ell - q**j for j in range(size) for ell in range(j + 1, size)
    )
    return sp.factor(diagonal_product_squared * vandermonde)


for size in range(1, 8):
    matrix = sp.Matrix(
        size,
        size,
        lambda j, k: sp.Rational(1, 2) ** ((j + k) ** 2),
    )
    determinant = sp.factor(matrix.det())
    assert determinant == expected_determinant(size)
    assert determinant != 0
    print(f"size={size}: determinant nonzero ({determinant})")

# For each fixed p, the test vector phi_n=2^{-n^2} has squared F_a,p norm
# sum_n 2^{-2n^2+pn}.  The following finite values merely check the exponent
# and its rapid decay; convergence itself follows immediately from the
# negative quadratic term.
for p in (1, 2, 5, 10):
    terms = [Fraction(2) ** (-2 * n * n + p * n) for n in range(20)]
    assert terms[-1] < Fraction(1, 10**50)
    print(f"p={p}: first 20 terms sum to {float(sum(terms)):.12g}")
