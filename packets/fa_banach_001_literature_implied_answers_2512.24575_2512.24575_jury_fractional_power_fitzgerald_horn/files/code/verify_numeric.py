#!/usr/bin/env python3
"""Numerically stress-test the Jury fractional-power derivative matrix."""

from __future__ import annotations

import argparse
import math

import numpy as np


def multiply(p, q, n):
    out = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            if i + k < n and j + ell < n:
                out[i + k, j + ell] = out.get((i + k, j + ell), 0.0) + a * b
    return out


def binomial(alpha, k):
    value = 1.0
    for j in range(k):
        value *= (alpha - j) / (j + 1)
    return value


def derivative_matrix(a, alpha):
    n = a.shape[0]
    a00 = a[0, 0]
    g = {
        (i, j): a[i, j] / a00
        for i in range(n)
        for j in range(n)
        if (i, j) != (0, 0)
    }
    power = {(0, 0): 1.0}
    coeff = {}
    for k in range(2 * n - 1):
        for key, value in power.items():
            coeff[key] = coeff.get(key, 0.0) + binomial(alpha, k) * value
        power = multiply(power, g, n)
    return np.array(
        [
            [
                a00**alpha
                * math.factorial(i)
                * math.factorial(j)
                * coeff.get((i, j), 0.0)
                for j in range(n)
            ]
            for i in range(n)
        ]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--alpha", type=float, default=1.5)
    parser.add_argument("--samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=251224575)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    worst = math.inf
    checked = 0
    for rank in range(1, args.n + 1):
        for _ in range(args.samples // args.n):
            x = np.exp(rng.normal(0.0, 2.0, size=(args.n, rank)))
            a = x @ x.T
            b = derivative_matrix(a, args.alpha)
            eigenvalues = np.linalg.eigvalsh(b)
            scale = max(np.linalg.norm(b, ord=2), 1e-300)
            score = eigenvalues[0] / scale
            worst = min(worst, score)
            checked += 1
            if score < -1e-8:
                raise AssertionError((args.n, args.alpha, rank, a, b, eigenvalues))

    print(f"n={args.n} alpha={args.alpha} checked={checked}")
    print(f"worst_normalized_min_eigenvalue={worst:.17g}")
    print("status=PASS")


if __name__ == "__main__":
    main()
