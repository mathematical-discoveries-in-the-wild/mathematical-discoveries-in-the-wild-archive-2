#!/usr/bin/env python3
"""Finite-dimensional QA for the dyadic Haar absorption construction.

This script is not a proof. It checks the exact coordinate bijection, the
parent/child center discrepancies, and randomized L^p norm ratios on finite
dyadic step-function spaces.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def coefficient_values(coefficients: np.ndarray, depth: int, p: float) -> np.ndarray:
    """Evaluate batches of truncated normalized Haar expansions on dyadic cells."""
    samples = coefficients.shape[0]
    cells = 1 << depth
    if coefficients.shape[1] != cells:
        raise ValueError("A depth-N expansion must have 2^N coefficients")
    values = np.repeat(coefficients[:, :1], cells, axis=1)
    for level in range(depth):
        count = 1 << level
        block = cells // count
        half = block // 2
        signs = np.tile(
            np.concatenate((np.ones(half), -np.ones(half))), count
        )
        amplitudes = np.repeat(
            coefficients[:, (1 << level) : (1 << level) + count], block, axis=1
        )
        values += (2.0 ** (level / p)) * amplitudes * signs
    return values


def apply_absorption(left: np.ndarray, right: np.ndarray, depth: int) -> np.ndarray:
    """Map two depth-N Haar coefficient arrays to one depth-(N+1) array."""
    samples = left.shape[0]
    target = np.zeros((samples, 1 << (depth + 1)))
    target[:, 0] = left[:, 0]   # first constant -> target constant
    target[:, 1] = right[:, 0]  # second constant -> root Haar function
    used = {0, 1}
    for level in range(depth):
        source_offset = 1 << level
        target_offset = 1 << (level + 1)
        for index in range(1 << level):
            left_target = target_offset + 2 * index
            right_target = left_target + 1
            target[:, left_target] = left[:, source_offset + index]
            target[:, right_target] = right[:, source_offset + index]
            used.add(left_target)
            used.add(right_target)
    expected = set(range(1 << (depth + 1)))
    if used != expected:
        raise AssertionError("The image coordinates do not partition the target basis")
    return target


def lp_norm(values: np.ndarray, p: float) -> np.ndarray:
    return np.mean(np.abs(values) ** p, axis=1) ** (1.0 / p)


def check_center_discrepancies(max_depth: int) -> None:
    for level in range(max_depth):
        length = 2.0 ** (-level)
        expected = length / 4.0
        for index in range(1 << level):
            parent_center = (index + 0.5) * length
            left_center = parent_center - expected
            right_center = parent_center + expected
            if not math.isclose(abs(parent_center - left_center), expected):
                raise AssertionError("Left-child center discrepancy failed")
            if not math.isclose(abs(parent_center - right_center), expected):
                raise AssertionError("Right-child center discrepancy failed")


def run(samples: int, max_depth: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    check_center_discrepancies(max_depth)
    print("Exact coordinate coverage and center discrepancies: PASS")
    for p in (1.2, 1.5, 3.0, 5.0):
        overall_min = math.inf
        overall_max = 0.0
        for depth in range(1, max_depth + 1):
            size = 1 << depth
            left = rng.standard_normal((samples, size))
            right = rng.standard_normal((samples, size))
            target = apply_absorption(left, right, depth)
            left_values = coefficient_values(left, depth, p)
            right_values = coefficient_values(right, depth, p)
            target_values = coefficient_values(target, depth + 1, p)
            domain_norm = (
                lp_norm(left_values, p) ** p + lp_norm(right_values, p) ** p
            ) ** (1.0 / p)
            ratios = lp_norm(target_values, p) / domain_norm
            overall_min = min(overall_min, float(np.min(ratios)))
            overall_max = max(overall_max, float(np.max(ratios)))
        print(
            f"p={p:3.1f}: randomized ratio range through depth {max_depth}: "
            f"[{overall_min:.6f}, {overall_max:.6f}]"
        )
    print("No finite-dimensional contradiction found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=500)
    parser.add_argument("--max-depth", type=int, default=8)
    parser.add_argument("--seed", type=int, default=170704798)
    args = parser.parse_args()
    run(args.samples, args.max_depth, args.seed)

