#!/usr/bin/env python3
"""Numerical regression for the Poissonized telescoping counterexample.

This is not the proof. It evaluates E[a_N] stably around the mode of a Poisson
law and compares it with the proved leading asymptotic.
"""

from __future__ import annotations

import math

C = math.e**2


def s(x: float) -> float:
    y = x + C
    return math.sin(math.log(y)) / math.log(y)


def a(x: float) -> float:
    return s(x) - s(x + 1.0)


def poisson_average(t: float) -> float:
    m = int(t)
    radius = int(14.0 * math.sqrt(t) + 80.0)
    lo = max(0, m - radius)
    hi = m + radius
    p_m = math.exp(-t + m * math.log(t) - math.lgamma(m + 1.0))
    total = a(float(m)) * p_m
    p = p_m
    for k in range(m - 1, lo - 1, -1):
        p *= (k + 1.0) / t
        total += a(float(k)) * p
    p = p_m
    for k in range(m + 1, hi + 1):
        p *= t / k
        total += a(float(k)) * p
    return total


def leading(t: float) -> float:
    y = t + C
    return -math.cos(math.log(y)) / (y * math.log(y))


def main() -> None:
    # Telescoping identity and o(1/k) trend.
    for n in (10, 100, 1000, 10000):
        partial = sum(a(float(k)) for k in range(n + 1))
        assert abs(partial - (s(0.0) - s(float(n + 1)))) < 2.0e-13

    rows = []
    for t in (100.0, 300.0, 1000.0, 3000.0, 10000.0, 30000.0):
        exact = poisson_average(t)
        lead = leading(t)
        scaled_error = abs(exact - a(t)) * t * t * math.log(t)
        rows.append((t, exact, lead, scaled_error))
        # A generous regression bound for the O(t^-2/log t) estimate.
        assert scaled_error < 20.0

    # Logarithmic-period samples with |cos(log(t+C))| near one retain the
    # predicted 1/(t log t) magnitude.
    for j in (1.0, 1.5, 2.0):
        t = math.exp(2.0 * math.pi * j) - C
        exact = poisson_average(t)
        normalized = -exact * (t + C) * math.log(t + C)
        expected = math.cos(2.0 * math.pi * j)
        assert abs(normalized - expected) < 0.18

    print("PASS: telescoping identities, Poisson smoothing, and asymptotic sign")
    for row in rows:
        print("t=%7g F=% .6e lead=% .6e scaled_error=% .4f" % row)


if __name__ == "__main__":
    main()
