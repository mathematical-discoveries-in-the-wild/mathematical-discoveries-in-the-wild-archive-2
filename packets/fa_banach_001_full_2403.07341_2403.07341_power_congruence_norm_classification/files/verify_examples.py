#!/usr/bin/env python3
"""Floating-point sanity checks only; this is not part of the proof."""

import numpy as np
from scipy.linalg import fractional_matrix_power


def positive_power(matrix, exponent):
    value = fractional_matrix_power(matrix, exponent)
    return np.real_if_close((value + value.conj().T) / 2)


def lhs(a, x, p):
    ahalf = positive_power(a, p / 2)
    inside = ahalf @ positive_power(x, p) @ ahalf
    return np.linalg.norm(positive_power(inside, 1 / p) @ np.linalg.inv(a), 2)


theta = 0.4
rotation = np.array(
    [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
)
a_noncentral = np.diag([1.0, 3.0])
x_noncommuting = rotation @ np.diag([1.0, 4.0]) @ rotation.T
target = np.linalg.norm(x_noncommuting, 2)

print("noncentral M2 tests")
for p in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 10.0):
    value = lhs(a_noncentral, x_noncommuting, p)
    print(f"p={p:4.1f} lhs={value:.12f} rhs={target:.12f} gap={value-target:+.3e}")

assert abs(lhs(a_noncentral, x_noncommuting, 2.0) - target) < 1e-10
for p in (0.5, 1.0, 1.5, 3.0, 4.0, 10.0):
    assert abs(lhs(a_noncentral, x_noncommuting, p) - target) > 1e-3

a_central = 2.5 * np.eye(2)
for p in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 10.0):
    assert abs(lhs(a_central, x_noncommuting, p) - target) < 1e-8

print("SANITY CHECKS PASSED")
