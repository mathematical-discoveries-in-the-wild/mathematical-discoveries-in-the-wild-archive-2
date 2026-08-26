#!/usr/bin/env python3
"""High-precision checks for the rank-one-split counterexample.

The proof in the packet is analytic.  This script checks its closed formulas
for representative exponents and separately verifies a simple rational-
correlation illustration at p=4/3.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 100


def positive_root(p: mp.mpf) -> mp.mpf:
    def f(x: mp.mpf) -> mp.mpf:
        return x**p - 2 * x - 1

    lo = mp.mpf(1)
    hi = mp.mpf(2)
    while f(hi) <= 0:
        hi *= 2
    for _ in range(500):
        mid = (lo + hi) / 2
        if f(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def proposed_constant(p: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    x = positive_root(p)
    value = mp.sqrt(x * (x + 1)) / (x**p + 1) ** (1 / p)
    return value, x


def rank_one_ratio(p: mp.mpf, alpha: mp.mpf, beta: mp.mpf) -> mp.mpf:
    numerator_p = ((1 + alpha) * (1 + beta)) ** (p / 2)
    numerator_p += ((1 - alpha) * (1 - beta)) ** (p / 2)
    denominator_p = (1 + beta) ** p + (1 - beta) ** p
    return (numerator_p / denominator_p) ** (1 / p)


def proof_choice(p: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    q = p / 2
    _, x = proposed_constant(p)
    beta = (x - 1) / (x + 1)
    threshold = ((((1 - beta) / (1 + beta)) ** q) / q) ** (1 / (1 - q))
    delta = mp.mpf("0.5") * min(mp.mpf(1), threshold)
    return 1 - delta, beta, delta


def main() -> None:
    ps = [
        mp.mpf(21) / 20,
        mp.mpf(6) / 5,
        mp.mpf(4) / 3,
        mp.mpf(3) / 2,
        mp.mpf(7) / 4,
        mp.mpf(19) / 10,
    ]
    for p in ps:
        predicted, _ = proposed_constant(p)
        alpha, beta, delta = proof_choice(p)
        actual = rank_one_ratio(p, alpha, beta)
        assert actual > predicted
        print(
            "p={} alpha={} beta={} delta={} actual={} proposed={} gap={}".format(
                mp.nstr(p, 8),
                mp.nstr(alpha, 16),
                mp.nstr(beta, 16),
                mp.nstr(delta, 8),
                mp.nstr(actual, 20),
                mp.nstr(predicted, 20),
                mp.nstr(actual - predicted, 12),
            )
        )

    p = mp.mpf(4) / 3
    alpha = mp.mpf(9) / 10
    beta = mp.mpf(13) / 20
    actual = rank_one_ratio(p, alpha, beta)
    predicted, _ = proposed_constant(p)
    assert actual > predicted
    print(
        "explicit p=4/3, alpha=9/10, beta=13/20: "
        f"actual={mp.nstr(actual, 30)}, proposed={mp.nstr(predicted, 30)}, "
        f"gap={mp.nstr(actual-predicted, 20)}"
    )


if __name__ == "__main__":
    main()
