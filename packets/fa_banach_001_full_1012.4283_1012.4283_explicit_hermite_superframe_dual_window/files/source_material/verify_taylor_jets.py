"""Symbolically verify E_j = z^j/j! modulo z^N for generic q."""

import sympy as sp

z = sp.Symbol("z")
for order in range(1, 9):
    coefficients = sp.symbols(f"q0:{order + 1}")
    q = sum(coefficients[k] * z**k for k in range(order + 1))
    reciprocal = sp.series(1 / q, z, 0, order).removeO()
    for j in range(order):
        truncation = sp.series(reciprocal, z, 0, order - j).removeO()
        candidate = z**j / sp.factorial(j) * q * truncation
        remainder = sp.series(candidate - z**j / sp.factorial(j), z, 0, order).removeO()
        assert sp.simplify(remainder) == 0, (order, j, remainder)
print("generic Taylor-jet identities verified for N=1,...,8")
