#!/usr/bin/env python3
"""LP search for norm inflation among continuous periodic ridge functions."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import numpy as np


SEARCH = Path(__file__).with_name("1312.3798_cyclic_constant_search.py")
SPEC = importlib.util.spec_from_file_location("cyclic_search", SEARCH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def interpolation_row(value: int, fine: int, knots: int) -> tuple[int, int, float]:
    scaled = value * knots / fine
    left = int(np.floor(scaled)) % knots
    fraction = scaled - np.floor(scaled)
    return left, (left + 1) % knots, fraction


def ridge_matrix(
    modulus: int, rank: int, forms: tuple[tuple[int, ...], ...], knots: int
) -> np.ndarray:
    points = list(itertools.product(range(modulus), repeat=rank))
    a = np.zeros((len(points), knots * len(forms)))
    for row, point in enumerate(points):
        for j, form in enumerate(forms):
            value = sum(coefficient * coordinate for coefficient, coordinate in zip(form, point))
            value %= modulus
            left, right, fraction = interpolation_row(value, modulus, knots)
            a[row, j * knots + left] += 1.0 - fraction
            a[row, j * knots + right] += fraction
    return a


def main() -> None:
    rng = np.random.default_rng(20260811)
    cases = [
        (2, ((1, 0), (0, 1), (1, 1))),
        (2, ((1, 0), (0, 1), (1, 1), (1, 2))),
        (3, ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))),
    ]
    for rank, forms in cases:
        knots = 4 if rank == 3 else 6
        fine = 3 * knots if rank == 3 else 4 * knots
        a = ridge_matrix(fine, rank, forms, knots)
        best = 0.0
        best_f = None
        best_coeffs = None
        for _ in range(80 if rank == 3 else 240):
            direction = rng.normal(size=a.shape[0])
            f = MODULE.range_vertex(a, direction)
            if f is None or np.max(np.abs(f)) < 1e-9:
                continue
            f /= np.max(np.abs(f))
            quotient, coeffs = MODULE.quotient_norm(a, f)
            if quotient > best + 1e-8:
                best = quotient
                best_f = f.copy()
                best_coeffs = coeffs.copy()
        print(f"rank={rank}, n={len(forms)}, sampled quotient={best:.12g}")
        if best > 1.00001:
            print("forms=", forms)
            print("components=", np.round(best_coeffs.reshape(len(forms), knots), 8))
            print("f range=", float(np.min(best_f)), float(np.max(best_f)))
            return


if __name__ == "__main__":
    main()
