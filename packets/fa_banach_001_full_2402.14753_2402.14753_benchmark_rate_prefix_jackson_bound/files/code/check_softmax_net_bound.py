#!/usr/bin/env python3
"""Numerical sanity check for the m=1 case of the proved estimates.

This is not part of the proof.  It checks the trigonometric gap, the stated
circle covering count, and the actual fixed-head error for one Lipschitz map.
"""

import math

import numpy as np


def stable_head(theta, centers, values, lam, context_length):
    scores = lam * np.cos(theta - centers)
    peak = max(float(np.max(scores)), 0.0)
    weights = np.exp(scores - peak)
    context_weight = context_length * math.exp(-peak)
    return (weights[:, None] * values).sum(axis=0) / (
        weights.sum() + context_weight
    )


def target(theta):
    return np.array([math.sin(2.0 * theta), math.cos(3.0 * theta)])


def main():
    lipschitz_constant = 3.0
    epsilon = 1.2
    context_length = 4
    delta = min(0.5, epsilon / (6.0 * lipschitz_constant))

    # For S^1, C_1=2*pi.  Equally spaced points with this count are
    # delta-separated and form a delta-net.
    count = max(2, math.floor(2.0 * math.pi / delta))
    centers = 2.0 * math.pi * np.arange(count) / count
    values = np.stack([target(t) for t in centers])
    bound = 2.0 * math.pi / delta
    assert count <= bound + 1e-12
    assert math.pi / count <= delta

    gap = math.cos(delta) - math.cos(2.0 * delta)
    assert gap >= 0.5 * delta * delta

    b_norm = math.sqrt(2.0)
    lam_local = 2.0 / (delta * delta) * math.log(math.pi * count / delta)
    lam_context = max(0.0, math.log(2.0 * context_length * b_norm / epsilon)) / math.cos(delta)
    lam = max(lam_local, lam_context)

    grid = np.linspace(0.0, 2.0 * math.pi, 20001, endpoint=False)
    errors = [
        np.linalg.norm(
            stable_head(t, centers, values, lam, context_length) - target(t)
        )
        for t in grid
    ]
    max_error = float(np.max(errors))

    analytic_split_error = 3.0 * lipschitz_constant * delta
    analytic_context_error = b_norm * context_length * math.exp(
        -lam * math.cos(delta)
    )
    analytic_total = analytic_split_error + analytic_context_error

    assert analytic_total <= epsilon + 1e-12
    assert max_error <= epsilon
    print(f"delta={delta:.8f}")
    print(f"N={count} <= {bound:.3f}")
    print(f"lambda={lam:.3f}")
    print(f"analytic_total_bound={analytic_total:.8f} <= epsilon={epsilon}")
    print(f"sampled_max_error={max_error:.8f}")


if __name__ == "__main__":
    main()
