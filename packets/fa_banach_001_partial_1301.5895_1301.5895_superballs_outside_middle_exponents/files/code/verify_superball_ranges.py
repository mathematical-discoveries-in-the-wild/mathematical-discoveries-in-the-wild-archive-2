#!/usr/bin/env python3
"""Directed-interval and numerical checks for the superball packet."""

from __future__ import annotations

import math
import random

from mpmath import iv


iv.dps = 50
c = iv.log(2)


def interval_t(value: str):
    return iv.mpf([value, value])


def q_interval(t):
    a = iv.exp(-c / t)
    return 2 * t**3 * (1 + a) ** 2 - c**2 * a * (1 + t) * (1 + 3 * t)


def qprime_interval(t):
    a = iv.exp(-c / t)
    b = 1 + 4 * t + 3 * t**2
    return (
        6 * t**2 * (1 + a) ** 2
        + 4 * c * t * a * (1 + a)
        - c**2 * a * (c * b / t**2 + 4 + 6 * t)
    )


def left_interval(t):
    return iv.log((1 + 3 * t) / (1 + t))


def right_interval(t):
    a = iv.exp(-c / t)
    return iv.log(1 + a) + c * a / (t * (1 + a))


def lower(x) -> float:
    return float(x.a)


def upper(x) -> float:
    return float(x.b)


def certify_scalar_lemma() -> None:
    # Subdivide into exact terminating decimal intervals.  The directed
    # interval evaluation proves Q'(t)>0 throughout [1/2,1].
    minimum_lower = float("inf")
    for i in range(5000):
        lo = f"{5000 + i:04d}e-4"
        hi = f"{5001 + i:04d}e-4"
        t = iv.mpf([lo, hi])
        bound = lower(qprime_interval(t))
        minimum_lower = min(minimum_lower, bound)
        assert bound > 0

    t55 = interval_t("0.55")
    t56 = interval_t("0.56")
    assert upper(q_interval(t55)) < 0
    assert lower(q_interval(t56)) > 0

    h55 = left_interval(t55) - right_interval(t55)
    h56 = left_interval(t56) - right_interval(t56)
    middle = left_interval(t55) - right_interval(t56)
    assert lower(h55) > 0
    assert lower(h56) > 0
    assert lower(middle) > 0
    print(f"certified min interval lower bound for Q': {minimum_lower:.12f}")
    print(f"certified H(0.55) > {lower(h55):.12f}")
    print(f"certified H(0.56) > {lower(h56):.12f}")
    print(f"certified L(0.55)-R(0.56) > {lower(middle):.12f}")


def check_bcc_cell() -> None:
    rng = random.Random(13015895)
    for p in (1.0, 1.25, 1.5, 1.75, 2.0):
        radius_p = 0.5 * (1 + 2 ** (-p)) ** (1 / p)
        for _ in range(100_000):
            z = [rng.random() for _ in range(3)]
            d0 = 0.5 * sum(v**p for v in z) ** (1 / p)
            dh = 0.5 * sum((1 - v) ** p for v in z) ** (1 / p)
            assert min(d0, dh) <= radius_p + 2e-15
        witness = (1.0, 0.5, 0.0)
        d0 = 0.5 * sum(v**p for v in witness) ** (1 / p)
        dh = 0.5 * sum((1 - v) ** p for v in witness) ** (1 / p)
        assert abs(d0 - radius_p) < 1e-14
        assert abs(dh - radius_p) < 1e-14
    print("checked 500000 BCC cell points and exact equality witnesses")


def volume_p3(p: float) -> float:
    return 8 * math.gamma(1 + 1 / p) ** 3 / math.gamma(1 + 3 / p)


def check_density_values() -> None:
    ball = 5 * math.sqrt(5) * math.pi / 24
    previous = -1.0
    for i in range(1001):
        p = 1 + i / 1000
        bcc = volume_p3(p) / 4 * (1 + 2 ** (-p)) ** (3 / p)
        assert bcc + 1e-13 >= previous
        assert bcc <= ball + 2e-14
        previous = bcc
    assert abs(previous - ball) < 2e-14

    # Rational decimal witnesses used in the elementary large-p comparison.
    assert 1.443**3 > 3
    assert 2.236**2 < 5
    assert 3.1415 < math.pi
    assert 1.443 < 5 * 2.236 * 3.1415 / 24
    print(f"ball density: {ball:.15f}")
    print("checked BCC density samples and the p>=9 rational comparison")


if __name__ == "__main__":
    certify_scalar_lemma()
    check_bcc_cell()
    check_density_values()
    print("PASS")

