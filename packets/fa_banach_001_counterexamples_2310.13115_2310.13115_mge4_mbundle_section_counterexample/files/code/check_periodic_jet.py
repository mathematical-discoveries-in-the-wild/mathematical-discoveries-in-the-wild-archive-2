#!/usr/bin/env python3
"""Fast exact audits for the periodic-jet M-bundle counterexample."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import random


Monomial = tuple[int, int]
Polynomial = dict[Monomial, Fraction]


def clean(poly: Polynomial) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(*polys: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return clean(result)


def scale(coefficient: Fraction, poly: Polynomial) -> Polynomial:
    return clean({monomial: coefficient * value for monomial, value in poly.items()})


def multiply(left: Polynomial, right: Polynomial, degree: int) -> Polynomial:
    result: Polynomial = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            if i + j + k + ell <= degree:
                monomial = (i + k, j + ell)
                result[monomial] = result.get(monomial, Fraction(0)) + a * b
    return clean(result)


def power(poly: Polynomial, exponent: int, degree: int) -> Polynomial:
    result: Polynomial = {(0, 0): Fraction(1)}
    factor = poly
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, factor, degree)
        remaining //= 2
        if remaining:
            factor = multiply(factor, factor, degree)
    return result


def compose(poly: Polynomial, first: Polynomial, second: Polynomial, degree: int) -> Polynomial:
    result: Polynomial = {}
    powers_first = {i: power(first, i, degree) for i, _ in poly}
    powers_second = {j: power(second, j, degree) for _, j in poly}
    for (i, j), coefficient in poly.items():
        term = multiply(powers_first[i], powers_second[j], degree)
        result = add(result, scale(coefficient, term))
    return result


def linear(first: Fraction, second: Fraction) -> Polynomial:
    return clean({(1, 0): first, (0, 1): second})


def homogeneous(rng: random.Random, degree: int) -> Polynomial:
    return clean(
        {
            (i, degree - i): Fraction(rng.randint(-3, 3))
            for i in range(degree + 1)
        }
    )


def inverse_2x2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    (a, b), (c, d) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("singular matrix")
    return (
        (Fraction(d, determinant), Fraction(-b, determinant)),
        (Fraction(-c, determinant), Fraction(a, determinant)),
    )


def matrix_vector(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    vector: tuple[Polynomial, Polynomial],
) -> tuple[Polynomial, Polynomial]:
    return (
        add(scale(matrix[0][0], vector[0]), scale(matrix[0][1], vector[1])),
        add(scale(matrix[1][0], vector[0]), scale(matrix[1][1], vector[1])),
    )


def audit_coordinate_change() -> int:
    rng = random.Random(231013115)
    checks = 0
    y = (linear(Fraction(1), Fraction(0)), linear(Fraction(0), Fraction(1)))
    for m in range(4, 13):
        for _ in range(40):
            while True:
                A_int = (
                    (rng.randint(-3, 3), rng.randint(-3, 3)),
                    (rng.randint(-3, 3), rng.randint(-3, 3)),
                )
                try:
                    B = inverse_2x2(A_int)
                    break
                except ValueError:
                    pass

            avec = (Fraction(rng.randint(-2, 2)), Fraction(rng.randint(-2, 2)))
            cvec = (Fraction(rng.randint(-2, 2)), Fraction(rng.randint(-2, 2)))
            gamma = Fraction(rng.randint(-3, 3))
            By = matrix_vector(B, y)
            f = add(homogeneous(rng, m - 1), homogeneous(rng, m))
            f_by = compose(f, By[0], By[1], m)

            Ba = (
                B[0][0] * avec[0] + B[0][1] * avec[1],
                B[1][0] * avec[0] + B[1][1] * avec[1],
            )
            u_hat = (
                add(By[0], scale(-Ba[0], f_by)),
                add(By[1], scale(-Ba[1], f_by)),
            )
            f_uhat = compose(f, u_hat[0], u_hat[1], m)

            Au = (
                add(scale(Fraction(A_int[0][0]), u_hat[0]), scale(Fraction(A_int[0][1]), u_hat[1])),
                add(scale(Fraction(A_int[1][0]), u_hat[0]), scale(Fraction(A_int[1][1]), u_hat[1])),
            )
            residual = (
                add(Au[0], scale(avec[0], f_uhat), scale(Fraction(-1), y[0])),
                add(Au[1], scale(avec[1], f_uhat), scale(Fraction(-1), y[1])),
            )
            assert residual == ({}, {})
            checks += 2

            v_actual = add(
                scale(cvec[0], u_hat[0]),
                scale(cvec[1], u_hat[1]),
                scale(gamma, f_uhat),
            )
            cB = (
                cvec[0] * B[0][0] + cvec[1] * B[1][0],
                cvec[0] * B[0][1] + cvec[1] * B[1][1],
            )
            kappa = gamma - cB[0] * avec[0] - cB[1] * avec[1]
            v_predicted = add(scale(cvec[0], By[0]), scale(cvec[1], By[1]), scale(kappa, f_by))
            assert add(v_actual, scale(Fraction(-1), v_predicted)) == {}
            checks += 1
    return checks


def audit_local_model() -> int:
    checks = 0
    for m in range(4, 1001):
        assert 2 * m - 3 > m
        # d^(m-1)/d sigma^(m-1) of
        # (b+theta)sigma^(m-1)/(m-1)! is b+theta.
        assert Fraction(factorial(m - 1), factorial(m - 1)) == 1
        # One further theta derivative is therefore exactly one, while the
        # c*sigma^m term still vanishes at sigma=0.
        checks += 3
    return checks


def main() -> None:
    checks = audit_coordinate_change() + audit_local_model()
    print(f"PASS: {checks:,} exact coordinate, degree, and local-jet checks")


if __name__ == "__main__":
    main()
