#!/usr/bin/env python3
"""Exact checks for the factorization proof for arXiv:1502.07095."""

from sympy import Rational, Symbol, expand, factorial, prod, rf, series, simplify


t = Symbol("t")
u = Symbol("u")
w = Symbol("w")
X = Symbol("X")
Y = Symbol("Y")


def coeff(expr, var, degree):
    return expand(series(expr, var, 0, degree + 1).removeO()).coeff(var, degree)


def check_universal_identity(max_a=10):
    for a in range(1, max_a + 1):
        lhs = factorial(a) * coeff(
            (1 - t / 2) ** (-Y) * (1 + t / 2) ** (a - 1 + Y), t, a
        )
        rhs = rf(Y, a)
        assert simplify(lhs - rhs) == 0, (a, expand(lhs - rhs))


def beta_q_power(m, n):
    generating = (1 - u / 2) ** (-n) * (
        (1 + u / 2) / (1 - u / 2)
    ) ** X
    return factorial(m) * coeff(generating, u, m)


def check_source_reconstruction():
    # Rational lambda_2 values exercise generalized, rather than only integral,
    # binomial expansions.  lambda_1 is forced by the source weight relation.
    for n in (3, 4, 6):
        for a in range(1, 7):
            for lambda_2 in (Rational(2, 3), Rational(-5, 4)):
                lambda_1 = a - 1 - n - lambda_2
                g = (1 + w) ** (a - lambda_1 - 1) * (
                    1 - w
                ) ** (a - lambda_2 - 1)
                alphas = [coeff(g, w, k) for k in range(a + 1)]
                reconstructed = 0
                for k in range(a + 1):
                    falling = factorial(a) / factorial(a - k)
                    reconstructed += (
                        (-1) ** k
                        * alphas[k]
                        * falling
                        * beta_q_power(a - k, n)
                        / (2**k)
                    )
                expected = prod(X + j - lambda_2 for j in range(a))
                assert simplify(reconstructed - expected) == 0, (
                    n,
                    a,
                    lambda_2,
                    expand(reconstructed - expected),
                )


if __name__ == "__main__":
    check_universal_identity()
    check_source_reconstruction()
    print("PASS: universal coefficient identity for a=1..10")
    print("PASS: source-to-PBW reconstruction for 36 exact parameter cases")
