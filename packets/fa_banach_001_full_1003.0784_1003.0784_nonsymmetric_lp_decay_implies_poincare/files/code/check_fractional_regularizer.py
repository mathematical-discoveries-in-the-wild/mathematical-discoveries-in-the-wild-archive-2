#!/usr/bin/env python3
"""Regression checks for the fractional-power regularizer in the proof."""

from __future__ import annotations

import math

import numpy as np


def check_case(p: float, epsilon: float, s: float) -> None:
    alpha = 2.0 / p
    base = s * s + epsilon
    psi = s * base ** ((alpha - 1.0) / 2.0)
    derivative = base ** ((alpha - 3.0) / 2.0) * (epsilon + alpha * s * s)
    assert derivative > 0.0
    assert abs(psi) ** p <= s * s + 2e-11 * max(1.0, s * s)
    weighted = abs(psi) ** (p - 2.0) * derivative * derivative
    assert weighted <= 1.0 + 2e-11


def main() -> None:
    p_values = np.concatenate((np.linspace(2.01, 4.0, 25), np.linspace(4.5, 30.0, 18)))
    epsilon_values = np.logspace(-12, 4, 32)
    positive_s = np.logspace(-12, 8, 421)
    s_values = np.concatenate((-positive_s[::-1], np.array([0.0]), positive_s))
    tested = 0
    for p in p_values:
        for epsilon in epsilon_values:
            for s in s_values:
                check_case(float(p), float(epsilon), float(s))
                tested += 1
    expected = len(p_values) * len(epsilon_values) * len(s_values)
    assert tested == expected
    print(f"passed {tested}/{expected} scalar regularizer checks")


if __name__ == "__main__":
    main()
