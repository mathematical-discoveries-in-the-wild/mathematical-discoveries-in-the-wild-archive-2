"""Numerical sanity checks; the packet proof is analytic and exact."""

from __future__ import annotations

import math


def mean_cos(t: float, h: float) -> float:
    return (math.sin(t + h) - math.sin(t)) / h


def mean_sin(t: float, h: float) -> float:
    return (math.cos(t) - math.cos(t + h)) / h


def formula_cos(t: float, h: float) -> float:
    return math.sin(h) / h * math.cos(t) + (math.cos(h) - 1) / h * math.sin(t)


def formula_sin(t: float, h: float) -> float:
    return (1 - math.cos(h)) / h * math.cos(t) + math.sin(h) / h * math.sin(t)


max_error = 0.0
for t in [-4.7, -1.0, -0.2, 0.0, 0.9, 3.3]:
    for h in [0.01, 0.2, 1.0, math.pi, 5.1]:
        max_error = max(max_error, abs(mean_cos(t, h) - formula_cos(t, h)))
        max_error = max(max_error, abs(mean_sin(t, h) - formula_sin(t, h)))
        assert math.tanh(t + h) > math.tanh(t)

assert max_error < 2e-13, max_error
assert abs((math.cos(math.pi) - 1) / math.pi + 2 / math.pi) < 1e-15
assert abs((1 - math.cos(math.pi)) / math.pi - 2 / math.pi) < 1e-15
print(f"PASS: max trigonometric mean identity error = {max_error:.3e}")
