#!/usr/bin/env python3
"""Verify the critical exponents in the two lacunary constructions."""

from __future__ import annotations

import math

import sympy as sp


s, t, d, theta, alpha = sp.symbols(
    "s t d theta alpha", positive=True, finite=True
)
p = 2 / theta
q = s / theta - d

# Compact remote peak: a_n^p R_n^q, with a_n ~ R_n^(-t/2).
compact_power = sp.simplify(-t * p / 2 + q)
assert sp.simplify(compact_power - ((s - t) / theta - d)) == 0
compact_root = sp.solve(sp.Eq(compact_power, 0), s)[0]
assert sp.simplify(compact_root - (t + d * theta)) == 0

# Noncompact remote peak: w_n^p L_n^-d R_n^q, where
# w_n ~ R_n^(-t/2), L_n ~ R_n^(t/(2 alpha)).
general_power = sp.simplify(-t * p / 2 - t * d / (2 * alpha) + q)
expected_power = (s - t) / theta - d - t * d / (2 * alpha)
assert sp.simplify(general_power - expected_power) == 0
general_root = sp.solve(sp.Eq(general_power, 0), s)[0]
expected_root = t + d * (1 + t / (2 * alpha)) * theta
assert sp.simplify(general_root - expected_root) == 0

# Compact peak-ball argument: solve the divergence exponent for s.
u, v = sp.symbols("u v", positive=True)
ball_power = -u / theta + s / theta - d - d * (u - v) / 2
ball_root = sp.solve(sp.Eq(ball_power, 0), s)[0]
expected_ball_root = u + d * theta + d * theta * (u - v) / 2
assert sp.simplify(ball_root - expected_ball_root) == 0
assert sp.simplify(expected_ball_root.subs({u: t, v: t}) - (t + d * theta)) == 0

# Numerical sign checks above and below the thresholds.
samples = [
    (1.7, 3.0, 0.4, 0.75),
    (0.3, 1.0, 1.0, 0.5),
    (4.0, 2.0, 0.8, 1.0),
]
for t0, d0, th0, a0 in samples:
    c0 = t0 + d0 * th0
    g0 = t0 + d0 * (1 + t0 / (2 * a0)) * th0
    cp = sp.lambdify((s, t, d, theta), compact_power, "math")
    gp = sp.lambdify((s, t, d, theta, alpha), general_power, "math")
    assert cp(c0 - 0.1, t0, d0, th0) < 0
    assert cp(c0 + 0.1, t0, d0, th0) > 0
    assert gp(g0 - 0.1, t0, d0, th0, a0) < 0
    assert gp(g0 + 0.1, t0, d0, th0, a0) > 0

# A finite truncation illustrates superlacunary dominance away from criticality.
def log_peak_contribution(n: int, r_log: float, power: float, exp_loss: float) -> float:
    return -exp_loss * n * math.log(2.0) + power * r_log


for power in (-0.2, 0.2):
    vals = [log_peak_contribution(n, n * n, power, 8.0) for n in range(10, 41)]
    if power < 0:
        assert vals[-1] < vals[0]
    else:
        assert vals[-1] > vals[0]

print("verified compact threshold:", compact_root)
print("verified general threshold:", general_root)
print("verified compact peak-ball threshold:", ball_root)
print("all symbolic and numerical checks passed")
