#!/usr/bin/env python3
"""Search the x, y, x+y torus model for a norm-one obstruction."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np


SEARCH = Path(__file__).with_name("1312.3798_cyclic_constant_search.py")
SPEC = importlib.util.spec_from_file_location("cyclic_search", SEARCH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def torus_basis(m: int) -> np.ndarray:
    rows = [(x, y) for x in range(m) for y in range(m)]
    blocks = []
    for coordinate in (lambda x, y: x, lambda x, y: y, lambda x, y: (x + y) % m):
        block = np.zeros((m * m, m))
        for row, (x, y) in enumerate(rows):
            block[row, coordinate(x, y)] = 1.0
        blocks.append(block)
    return np.concatenate(blocks, axis=1)


def main() -> None:
    rng = np.random.default_rng(20260811)
    for m in range(2, 13):
        a = torus_basis(m)
        directions = list(np.eye(m * m)) + list(-np.eye(m * m))
        directions += [rng.normal(size=m * m) for _ in range(300)]
        best = 0.0
        best_f = None
        best_coeffs = None
        for direction in directions:
            f = MODULE.range_vertex(a, direction)
            if f is None or np.max(np.abs(f)) < 1e-9:
                continue
            f /= np.max(np.abs(f))
            quotient, coeffs = MODULE.quotient_norm(a, f)
            if quotient > best + 1e-8:
                best = quotient
                best_f = f.copy()
                best_coeffs = coeffs.copy()
        print(f"m={m}, max sampled quotient={best:.12g}")
        if best > 1.00001:
            print("f matrix=\n", np.round(best_f.reshape(m, m), 8))
            print("components=", np.round(best_coeffs.reshape(3, m), 8))
            return


if __name__ == "__main__":
    main()
