#!/usr/bin/env python3
"""Finite sanity checks for the commuting-qubit hard instance.

This checks the formulas and signs used in the proof.  It is not a proof of
the asymptotic query or copy lower bounds.
"""

from math import log, sqrt


def g(alpha: float, t: float) -> float:
    return (0.25 ** (1.0 - alpha)) * (((1.0 + t) / 2.0) ** alpha) + (
        0.75 ** (1.0 - alpha)
    ) * (((1.0 - t) / 2.0) ** alpha)


def gprime_zero(alpha: float) -> float:
    return alpha * (2.0 ** (-alpha)) * (
        0.25 ** (1.0 - alpha) - 0.75 ** (1.0 - alpha)
    )


def d(alpha: float, t: float) -> float:
    return log(g(alpha, t)) / (alpha - 1.0)


def hellinger(t: float) -> float:
    p = ((1.0 + t) / 2.0, (1.0 - t) / 2.0)
    q = ((1.0 + 2.0 * t) / 2.0, (1.0 - 2.0 * t) / 2.0)
    return sqrt(0.5 * sum((sqrt(x) - sqrt(y)) ** 2 for x, y in zip(p, q)))


def main() -> None:
    alphas = (1.01, 1.1, 1.25, 1.5, 1.75, 2.0)
    hs = (1e-2, 1e-3, 1e-4, 1e-5)
    for alpha in alphas:
        c = gprime_zero(alpha)
        assert c > 0.0
        entropy_derivative = c / ((alpha - 1.0) * g(alpha, 0.0))
        assert entropy_derivative > 0.0
        for h in hs:
            q_gap = (g(alpha, 2.0 * h) - g(alpha, h)) / h
            d_gap = (d(alpha, 2.0 * h) - d(alpha, h)) / h
            assert q_gap > 0.0
            assert d_gap > 0.0
        rel_q = abs((g(alpha, 2e-5) - g(alpha, 1e-5)) / 1e-5 - c) / c
        rel_d = abs((d(alpha, 2e-5) - d(alpha, 1e-5)) / 1e-5 - entropy_derivative) / entropy_derivative
        assert rel_q < 5e-4
        assert rel_d < 5e-4
        print(
            f"alpha={alpha:4.2f}  g'(0)={c:.10g}  "
            f"D'(0)={entropy_derivative:.10g}"
        )
    for h in hs:
        assert hellinger(h) <= h
    print("all finite checks passed")


if __name__ == "__main__":
    main()

