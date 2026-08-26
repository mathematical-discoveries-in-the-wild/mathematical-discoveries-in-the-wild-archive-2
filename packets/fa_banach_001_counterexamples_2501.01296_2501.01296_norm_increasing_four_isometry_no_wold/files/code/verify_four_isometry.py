#!/usr/bin/env python3
"""Exact checks for the proposed 4-isometric rootless-tree counterexample."""

from fractions import Fraction
from math import comb


def a(m: int) -> int:
    return 1 if m == 2 else 2


def p(m: int, r: int) -> int:
    assert r >= 0
    return 1 + a(m) * r + r * r


def weight_square(child: tuple[int, int]) -> Fraction:
    n, m = child
    if n >= 2:
        return Fraction(p(m, n - 1), p(m, n - 2))
    if n == 0:
        return Fraction(m, m + 1) if m >= 1 else Fraction(1)
    return Fraction(1, m) if m >= 1 else Fraction(1)


def children(vertex: tuple[int, int]) -> list[tuple[int, int]]:
    n, m = vertex
    if n == 0:
        return [(0, m - 1), (1, m)]
    return [(n + 1, m)]


def norm_square(vertex: tuple[int, int], power: int) -> Fraction:
    masses = {vertex: Fraction(1)}
    for _ in range(power):
        new = {}
        for v, mass in masses.items():
            for w in children(v):
                new[w] = new.get(w, Fraction(0)) + mass * weight_square(w)
        masses = new
    return sum(masses.values(), Fraction(0))


def delta(vertex: tuple[int, int], order: int) -> Fraction:
    return sum(
        ((-1) ** k) * comb(order, k) * norm_square(vertex, k)
        for k in range(order + 1)
    )


def claimed_delta3_spine(m: int) -> Fraction:
    return Fraction(-2) if m <= 1 else Fraction(-2, m)


def main() -> None:
    # Exhaustive exact arithmetic on a large finite window.
    for m in range(-40, 81):
        for n in range(0, 15):
            v = (n, m)
            assert norm_square(v, 1) >= 1
            assert delta(v, 4) == 0
            if n >= 1:
                for k in range(9):
                    assert norm_square(v, k) == Fraction(
                        p(m, n + k - 1), p(m, n - 1)
                    )
                assert delta(v, 3) == 0
            else:
                assert delta(v, 3) == claimed_delta3_spine(m)

    # The source's Cauchy-dual obstruction series is 1 + sum_{n>=2} 1/n^2.
    partial = sum((Fraction(1, n * n) for n in range(2, 1001)), Fraction(1))
    assert partial < 2

    # The old constant-coefficient choice fails at order four; the m=2
    # coefficient surgery is essential.
    print("exact finite window: PASS")
    print("Delta_4(S)=0 on every checked basis vector")
    print("Delta_3 at spine: -2 (m<=1), -2/m (m>=2)")
    print("Cauchy-dual alpha at (0,0) = 1 + sum_{n>=2} 1/n^2 < 2")
    print("candidate: analytic norm-increasing 4-isometry without Wold decomposition")


if __name__ == "__main__":
    main()
