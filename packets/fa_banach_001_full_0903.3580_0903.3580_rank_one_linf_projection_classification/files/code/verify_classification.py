#!/usr/bin/env python3
"""Numerical sanity checks for the rank-one projection classification."""

import math
import random


def normalize(values):
    norm = math.sqrt(sum(abs(z) ** 2 for z in values))
    return [z / norm for z in values]


def formula_norm(v):
    return max(abs(z) for z in v) * sum(abs(z) for z in v)


def direct_row_sum_norm(v):
    return max(sum(abs(v[i] * v[j].conjugate()) for j in range(len(v)))
               for i in range(len(v)))


def spherical(xi, phi):
    return [math.sin(xi) * math.cos(phi),
            math.sin(xi) * math.sin(phi),
            math.cos(xi)]


def main():
    rng = random.Random(9033580)
    checked = 0
    for trial in range(20000):
        n = 2 + trial % 7
        raw = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(n)]
        v = normalize(raw)
        assert abs(formula_norm(v) - direct_row_sum_norm(v)) < 1e-12
        assert formula_norm(v) >= 1 - 1e-12
        checked += 1

    alpha = math.atan(math.sqrt(2))
    pairs = []
    pairs.extend((0.0, k * math.pi / 19) for k in range(19))
    pairs.extend((math.pi / 2, phi) for phi in
                 (0, math.pi / 4, math.pi / 2, 3 * math.pi / 4))
    pairs.extend((xi, phi) for xi in (math.pi / 4, 3 * math.pi / 4)
                 for phi in (0, math.pi / 2))
    pairs.extend((xi, phi) for xi in (alpha, math.pi - alpha)
                 for phi in (math.pi / 4, 3 * math.pi / 4))
    for xi, phi in pairs:
        assert abs(formula_norm(spherical(xi, phi)) - 1) < 1e-12

    nondegenerate = [p for p in pairs if p[0] != 0]
    strict = 0
    for xi, phi in nondegenerate:
        for delta in (1e-4, -1e-4):
            perturbed = spherical(xi + delta, phi + 0.37 * delta)
            if formula_norm(perturbed) > 1 + 1e-9:
                strict += 1

    print(f"random norm identities checked: {checked}")
    print(f"listed parameter representatives checked: {len(pairs)}")
    print(f"strict generic perturbations observed: {strict}/{2 * len(nondegenerate)}")


if __name__ == "__main__":
    main()
