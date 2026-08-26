#!/usr/bin/env python3
"""Finite sanity checks for the Cantor-cube function-system packet.

These checks illustrate the finite-coordinate norm and cone identities used
in the proof.  The infinite-dimensional MIN/MAX obstruction is a theorem, not
a computational claim, so this script is not a substitute for the proof.
"""

from __future__ import annotations

import itertools
import math
import random

import numpy as np


def subset_norm(values: list[complex]) -> float:
    best = 0.0
    for mask in range(1 << len(values)):
        total = sum(value for k, value in enumerate(values) if mask & (1 << k))
        best = max(best, abs(total))
    return best


def is_psd(matrix: np.ndarray, tol: float = 1e-9) -> bool:
    return bool(np.linalg.eigvalsh(matrix).min() >= -tol)


def all_subset_sums_psd(matrices: list[np.ndarray]) -> bool:
    zero = np.zeros_like(matrices[0])
    for mask in range(1 << len(matrices)):
        total = sum(
            (matrix for k, matrix in enumerate(matrices) if mask & (1 << k)),
            start=zero.copy(),
        )
        if not is_psd(total):
            return False
    return True


def main() -> None:
    rng = random.Random(231204791)

    real_cases = 0
    complex_cases = 0
    for length in range(1, 9):
        for _ in range(80):
            real_values = [rng.randint(-7, 7) for _ in range(length)]
            actual = subset_norm([complex(x) for x in real_values])
            expected = max(
                sum(max(x, 0) for x in real_values),
                sum(max(-x, 0) for x in real_values),
            )
            assert abs(actual - expected) < 1e-10
            real_cases += 1

            complex_values = [
                complex(rng.randint(-7, 7), rng.randint(-7, 7))
                for _ in range(length)
            ]
            l1_norm = sum(abs(z) for z in complex_values)
            actual = subset_norm(complex_values)
            assert actual <= l1_norm + 1e-10
            assert actual + 1e-10 >= l1_norm / math.pi
            complex_cases += 1

    cone_cases = 0
    for matrix_size, coordinate_count in itertools.product((2, 3), (2, 3, 4)):
        for _ in range(50):
            positive = []
            for _coordinate in range(coordinate_count):
                raw = np.array(
                    [
                        [rng.uniform(-2, 2) for _ in range(matrix_size)]
                        for _ in range(matrix_size)
                    ]
                )
                positive.append(raw.T @ raw)
            assert all_subset_sums_psd(positive)
            assert all(is_psd(matrix) for matrix in positive)

            broken = list(positive)
            broken[0] = -np.eye(matrix_size)
            assert not all_subset_sums_psd(broken)
            assert not all(is_psd(matrix) for matrix in broken)
            cone_cases += 2

    print(f"real subset-norm identity: PASS ({real_cases} cases)")
    print(f"complex 1/pi norm bound: PASS ({complex_cases} cases)")
    print(f"matrix singleton-cone mechanism: PASS ({cone_cases} cases)")
    print("PASS: all finite sanity checks completed")


if __name__ == "__main__":
    main()
