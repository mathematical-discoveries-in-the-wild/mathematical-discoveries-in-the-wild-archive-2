#!/usr/bin/env python3
"""Exact checks for the `(1-x)(1-y)` optimal-approximation recursion.

For small n this builds the primal Gram matrix over Fraction, solves the
normal equations exactly, and compares the squared residual with 1/e_n.
It also gives a floating-point long-run check of sqrt(n)/e_n -> 1.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import sqrt


Word = tuple[int, ...]


def words_through(n: int) -> list[Word]:
    return [tuple(w) for length in range(n + 1) for w in product((0, 1), repeat=length)]


def column(word: Word) -> dict[Word, Fraction]:
    """Coefficient vector of word * (1-x)(1-y)."""
    return {
        word: Fraction(1),
        word + (0,): Fraction(-1),
        word + (1,): Fraction(-1),
        word + (0, 1): Fraction(1),
    }


def dot_sparse(a: dict[Word, Fraction], b: dict[Word, Fraction]) -> Fraction:
    if len(a) > len(b):
        a, b = b, a
    return sum((value * b.get(key, 0) for key, value in a.items()), Fraction(0))


def solve_fraction(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """Gauss-Jordan solve over the rational numbers."""
    n = len(rhs)
    aug = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def primal_error(n: int) -> Fraction:
    basis = words_through(n)
    columns = [column(word) for word in basis]
    gram = [[dot_sparse(a, b) for b in columns] for a in columns]
    rhs = [Fraction(1) if word == () else Fraction(0) for word in basis]
    solution = solve_fraction(gram, rhs)
    projection_squared = sum(b * q for b, q in zip(rhs, solution))
    return Fraction(1) - projection_squared


def recurrence_errors(max_n: int) -> list[Fraction]:
    e = Fraction(1)
    kappa = Fraction(1, 2)
    errors: list[Fraction] = []
    for _ in range(max_n + 1):
        new_e = Fraction(1) + kappa * e / (kappa + e)
        new_kappa = kappa + e / (1 + e)
        e, kappa = new_e, new_kappa
        errors.append(1 / e)
    return errors


def asymptotic_check(n: int) -> tuple[float, float, float]:
    e = 1.0
    kappa = 0.5
    for _ in range(n + 1):
        new_e = 1.0 + kappa * e / (kappa + e)
        new_kappa = kappa + e / (1.0 + e)
        e, kappa = new_e, new_kappa
    return e, kappa, sqrt(n) / e


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-through", type=int, default=4)
    parser.add_argument("--asymptotic-n", type=int, default=100000)
    args = parser.parse_args()

    recurrence = recurrence_errors(args.exact_through)
    print("n  primal c_n  recurrence c_n  exact match")
    for n, expected in enumerate(recurrence):
        actual = primal_error(n)
        print(f"{n:2d} {str(actual):>12} {str(expected):>15} {actual == expected}")
        if actual != expected:
            raise SystemExit(f"mismatch at n={n}")

    e, kappa, scaled = asymptotic_check(args.asymptotic_n)
    print()
    print(f"n={args.asymptotic_n}")
    print(f"e_n={e:.12g}")
    print(f"kappa_n={kappa:.12g}")
    print(f"sqrt(n)*c_n={scaled:.12g}")


if __name__ == "__main__":
    main()
