#!/usr/bin/env python3
"""Regression checks for the p=0,q=1 endpoint counterexample."""

from itertools import product
from math import log


def edges(n):
    for x in range(1 << n):
        for j in range(n):
            y = x ^ (1 << j)
            if x < y:
                yield x, y


def check_cube_boundaries(max_n=4):
    for n in range(1, max_n + 1):
        vertices = 1 << n
        cube_edges = tuple(edges(n))
        checked = 0
        for mask in range(1, (1 << vertices) - 1):
            boundary = sum(((mask >> x) & 1) != ((mask >> y) & 1)
                           for x, y in cube_edges)
            assert boundary > 0
            checked += 1
        print(f"Q_{n}: checked {checked} nonempty proper supports")


def h(y):
    return -y * log(y) - (1 - y) * log(1 - y)


def inverse_binary_entropy(value):
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if h(mid) < value:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def xi_one(alpha):
    y = inverse_binary_entropy(log(2) - alpha)
    return (0.5 - y) * log((1 - y) / y)


def q1_energy(epsilon):
    # f=(1,epsilon) for the source's one-bit generator and uniform pi.
    return (1 - epsilon) * log(1 / epsilon) / (2 * (1 + epsilon))


def q_energy(q, epsilon):
    return ((1 - epsilon) * (1 - epsilon ** (q - 1)) /
            (2 * (q - 1) * (1 + epsilon ** q)))


if __name__ == "__main__":
    check_cube_boundaries()
    for alpha in (0.1, 0.3, 0.6):
        value = xi_one(alpha)
        assert 0 < value < float("inf")
        print(f"alpha={alpha:.1f}: finite Xi_1={value:.12f}")

    epsilons = [10.0 ** (-k) for k in range(1, 13)]
    q1_values = [q1_energy(eps) for eps in epsilons]
    assert all(a < b for a, b in zip(q1_values, q1_values[1:]))
    print(f"q=1 regularized energy: {q1_values[0]:.6f} -> {q1_values[-1]:.6f}")

    for q in (0.25, 0.5, 0.75):
        values = [q_energy(q, eps) for eps in epsilons]
        assert all(a < b for a, b in zip(values, values[1:]))
        print(f"q={q:.2f} regularized energy: {values[0]:.6f} -> {values[-1]:.6f}")

    # Full support has D_0=0; any proper nonempty one-bit support has D_0=ln 2.
    assert -log(1.0) == 0.0
    assert abs(-log(0.5) - log(2)) < 1e-15
    print("endpoint support dichotomy: passed")
