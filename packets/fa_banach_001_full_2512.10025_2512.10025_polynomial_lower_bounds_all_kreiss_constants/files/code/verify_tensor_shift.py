#!/usr/bin/env python3
"""Finite checks for the tensor-weighted-shift proof.

This script is a numerical sanity check, not a proof.  It verifies the
telescoping tensor-product identity, the scalar averaging inequality on a
finite grid, the advertised power witness, and sampled Kreiss ratios.
"""

from __future__ import annotations

import math

import numpy as np


J = np.array([[0.0, 1.0], [0.0, 0.0]])
I2 = np.eye(2)


def tensor_power(a: np.ndarray, m: int) -> np.ndarray:
    out = np.array([[1.0]])
    for _ in range(m):
        out = np.kron(out, a)
    return out


def internal_weight(a: float, m: int, k: int) -> np.ndarray:
    c = a / m
    return tensor_power(I2 + c * math.log(k / (k - 1)) * J, m)


def truncated_shift(a: float, m: int, length: int) -> np.ndarray:
    h = 2**m
    shift = np.zeros((h * length, h * length))
    for k in range(2, length + 1):
        block = internal_weight(a, m, k)
        shift[(k - 2) * h : (k - 1) * h, (k - 1) * h : k * h] = block
    return shift


def averaging_constant_squared(a: float) -> float:
    return 6 * a * a / ((1 - 2 * a) * (1 - a))


def scalar_coefficient(a: float, n_average: int, k: int) -> float:
    upper = min(n_average, k - 1)
    return sum(((k / (k - n)) ** a - 1) ** 2 for n in range(1, upper + 1)) / n_average


def check_product_identity() -> None:
    for a in (0.04, 0.12, 0.21):
        for m in range(1, 5):
            c = a / m
            for j, n in ((1, 4), (3, 5), (7, 3)):
                product = np.eye(2**m)
                for k in range(j + 1, j + n + 1):
                    product = product @ internal_weight(a, m, k)
                expected = tensor_power(I2 + c * math.log((j + n) / j) * J, m)
                assert np.linalg.norm(product - expected) < 2e-13
    print("product identity: passed")


def check_scalar_averaging_bound() -> None:
    for a in (0.02, 0.08, 0.16, 0.24):
        bound = averaging_constant_squared(a)
        worst = 0.0
        argmax = None
        for n_average in (1, 2, 3, 5, 10, 20, 50, 100, 200):
            for k in range(2, 8 * n_average + 20):
                value = scalar_coefficient(a, n_average, k)
                if value > worst:
                    worst = value
                    argmax = (n_average, k)
                assert value <= bound * (1 + 1e-12)
        print(
            f"averaging a={a:.2f}: worst={worst:.8f} at {argmax}, "
            f"proved bound={bound:.8f}"
        )


def check_power_and_sampled_kreiss() -> None:
    for a, m, length in ((0.08, 2, 9), (0.16, 3, 10), (0.22, 3, 12)):
        matrix = truncated_shift(a, m, length)
        h = 2**m
        e2 = np.array([0.0, 1.0])
        internal_vector = tensor_power(e2[:, None], m).reshape(-1)
        vector = np.zeros(h * length)
        vector[(length - 1) * h :] = internal_vector
        power_vector = np.linalg.matrix_power(matrix, length - 1) @ vector
        t = (a / m) * math.log(length)
        expected = (math.sqrt(1 + t * t)) ** m
        actual = np.linalg.norm(power_vector)
        assert abs(actual - expected) <= 5e-12 * max(1.0, expected)

        # The theorem bounds all z.  This finite grid merely checks for an
        # obvious contradiction in small examples.
        sampled = 0.0
        identity = np.eye(matrix.shape[0])
        for delta in np.geomspace(2e-3, 2.0, 9):
            radius = 1 + delta
            for theta in np.linspace(0, 2 * math.pi, 49)[:-1]:
                z = radius * np.exp(1j * theta)
                smallest = np.linalg.svd(z * identity - matrix, compute_uv=False)[-1]
                sampled = max(sampled, delta / smallest)
        rigorous_bound = 1 + math.sqrt(averaging_constant_squared(a))
        assert sampled <= rigorous_bound * (1 + 2e-8)
        print(
            f"matrix a={a:.2f}, m={m}, L={length}, dim={matrix.shape[0]}: "
            f"power witness={actual:.8f}, sampled Kreiss={sampled:.8f}, "
            f"proved bound={rigorous_bound:.8f}"
        )


def main() -> None:
    check_product_identity()
    check_scalar_averaging_bound()
    check_power_and_sampled_kreiss()
    print("all finite checks passed (these checks are not a proof)")


if __name__ == "__main__":
    main()
