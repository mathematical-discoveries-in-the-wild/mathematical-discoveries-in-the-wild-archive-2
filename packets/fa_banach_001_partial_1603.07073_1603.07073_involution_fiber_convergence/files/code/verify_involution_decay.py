#!/usr/bin/env python3
"""Exact coefficient checks and finite-cycle tests for the packet theorem."""

from __future__ import annotations

from fractions import Fraction
from math import comb, cos, pi, sqrt
import random


def p(m: int, k: int) -> Fraction:
    if abs(k) > m:
        return Fraction(0)
    return Fraction(comb(2 * m, m + k), 4**m)


def q(m: int, k: int) -> Fraction:
    return (p(m, k - 1) - p(m, k + 1)) / 4


def sup_norm(x: list[float]) -> float:
    return max(abs(a) for a in x)


def add(x: list[float], y: list[float], a: float = 1.0) -> list[float]:
    return [xi + a * yi for xi, yi in zip(x, y)]


def scale(a: float, x: list[float]) -> list[float]:
    return [a * xi for xi in x]


def main() -> None:
    # L^m D has coefficients q_m(k).  Check the telescoping total variation
    # identity and the Wallis-type bound used in the proof.
    for m in range(101):
        l1 = sum(abs(q(m, k)) for k in range(-m - 1, m + 2))
        expected = (p(m, 0) + p(m, 1)) / 2
        assert l1 == expected
        assert float(l1) <= 1 / sqrt(m + 1) + 1e-15

    rng = random.Random(160307073)
    for npoints in (4, 6, 10, 18, 34):
        sigma = [(-k) % npoints for k in range(npoints)]
        tau = [(1 - k) % npoints for k in range(npoints)]

        def U(x: list[float]) -> list[float]:
            return [x[sigma[k]] for k in range(npoints)]

        def V(x: list[float]) -> list[float]:
            return [x[tau[k]] for k in range(npoints)]

        def P(x: list[float]) -> list[float]:
            return scale(0.5, add(x, U(x), -1.0))

        def Q(x: list[float]) -> list[float]:
            return scale(0.5, add(x, V(x), -1.0))

        def T(x: list[float]) -> list[float]:
            return Q(P(x))

        def R(x: list[float]) -> list[float]:
            return V(U(x))

        def Rinv(x: list[float]) -> list[float]:
            return U(V(x))

        def D(x: list[float]) -> list[float]:
            return scale(0.25, add(R(x), Rinv(x), -1.0))

        def L(x: list[float]) -> list[float]:
            return scale(0.25, add(add(scale(2.0, x), R(x)), Rinv(x)))

        raw = [rng.uniform(-1.0, 1.0) for _ in range(npoints)]
        invariant = scale(0.5, add(raw, V(raw)))
        assert sup_norm(add(V(invariant), invariant, -1.0)) < 1e-12
        assert sup_norm(add(T(invariant), D(invariant), -1.0)) < 1e-12

        direct = T(invariant)
        formula = D(invariant)
        for power in range(1, 21):
            assert sup_norm(add(direct, formula, -1.0)) < 1e-11
            assert sup_norm(direct) <= sup_norm(invariant) / sqrt(power) + 1e-11
            direct = T(direct)
            formula = L(formula)

        # The long-cycle witness used to prove that the algebraic sum need
        # not be closed: invariant summands have size one while their sum is
        # a phase difference of order 1/npoints.
        theta = 2 * pi / npoints
        u = [cos(theta * k) for k in range(npoints)]
        v = [-cos(theta * (k - 0.5)) for k in range(npoints)]
        assert sup_norm(add(U(u), u, -1.0)) < 1e-12
        assert sup_norm(add(V(v), v, -1.0)) < 1e-12
        assert sup_norm(add(u, v)) <= pi / npoints + 1e-12

    print("verified coefficients m=0..100 and finite involution cycles")


if __name__ == "__main__":
    main()
