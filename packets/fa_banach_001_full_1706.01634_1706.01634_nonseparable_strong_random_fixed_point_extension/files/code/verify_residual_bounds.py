#!/usr/bin/env python3
"""Numerically sanity-check the two residual-to-fixed-point constants.

This is not a proof.  It stress-tests the algebraic inequalities used in the
packet over reproducible random scalar configurations satisfying the two
contractive hypotheses.
"""

from __future__ import annotations

import random


def gregus_check(rng: random.Random, trials: int = 100_000) -> None:
    for _ in range(trials):
        a = rng.uniform(1e-6, 1.0 - 1e-6)
        b = 1.0 - a
        cmax = (4.0 - a) / (8.0 - a)
        c = rng.uniform(0.0, cmax)
        delta = 10.0 ** rng.uniform(-8.0, 4.0)
        r = 10.0 ** rng.uniform(-8.0, 4.0)

        d = 10.0 ** rng.uniform(-8.0, 4.0)

        # Retain exactly the scalar consequences used in the proof.
        rhs = a * max(r, c * (r + d)) + b * delta
        tol = 1e-10 * max(1.0, r, d, rhs)
        if d > rhs + tol or r > delta + d + tol:
            continue

        c1 = (1.0 + b) / b
        c2 = (1.0 - a * c + b) / (1.0 - 2.0 * a * c)
        bound = max(c1, c2) * delta
        if r > bound + 1e-9 * max(1.0, r, bound):
            raise AssertionError((a, b, c, delta, r, d, bound))


def hardy_rogers_check(rng: random.Random, trials: int = 100_000) -> None:
    for _ in range(trials):
        raw = [rng.random() for _ in range(5)]
        total = rng.uniform(0.0, 1.0 - 1e-6)
        scale = total / sum(raw)
        alpha = [scale * x for x in raw]
        a1, a2, _a3, a4, a5 = alpha
        delta = 10.0 ** rng.uniform(-8.0, 4.0)
        r = 10.0 ** rng.uniform(-8.0, 4.0)
        d = 10.0 ** rng.uniform(-8.0, 4.0)

        rhs = (a1 + a4) * r + a2 * delta + a5 * d
        tol = 1e-10 * max(1.0, r, d, rhs)
        if d > rhs + tol or r > delta + d + tol:
            continue

        constant = (1.0 - a5 + a2) / (1.0 - a1 - a4 - a5)
        bound = constant * delta
        if r > bound + 1e-9 * max(1.0, r, bound):
            raise AssertionError((alpha, delta, r, d, bound))


def main() -> None:
    rng = random.Random(170601634)
    gregus_check(rng)
    hardy_rogers_check(rng)
    print("PASS: 100000 Gregus-Ciric and 100000 Hardy-Rogers scalar checks")


if __name__ == "__main__":
    main()
