#!/usr/bin/env python3
"""Search for positive one-particle sector-raising intertwiners.

For adjacent particle sectors m and m+1 of the positive staggered transfer
matrix B, this asks whether an inclusion-supported matrix U can satisfy
    B_{m+1} U >= U B_m
entrywise.  Such a U would prove monotonicity of Perron roots.  The finite LP
is only a route diagnostic, not a proof for arbitrary N.
"""

from __future__ import annotations

import argparse
import pathlib
import runpy

import numpy as np
from scipy.optimize import linprog


def positive_transfer(n: int, temperature: float, zeta: float, field: float) -> np.ndarray:
    probe = runpy.run_path(str(pathlib.Path(__file__).with_name("qtm_perron_probe.py")))
    matrix = np.abs(probe["qtm"](n, temperature, zeta, field, 1.0))
    dimension = 1 << (2 * n)
    permutation = []
    for state in range(dimension):
        flipped = state
        for site in range(2, 2 * n + 1, 2):
            flipped ^= 1 << (2 * n - site)
        permutation.append(flipped)
    return matrix[np.ix_(permutation, permutation)]


def solve_intertwiner(matrix: np.ndarray, width: int, m: int) -> tuple[bool, str]:
    lower = [state for state in range(1 << width) if state.bit_count() == m]
    upper = [state for state in range(1 << width) if state.bit_count() == m + 1]
    edges = [(row, col) for row, y in enumerate(upper) for col, x in enumerate(lower) if x & ~y == 0]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    block_lower = matrix[np.ix_(lower, lower)]
    block_upper = matrix[np.ix_(upper, upper)]
    constraints = []
    for row in range(len(upper)):
        for col in range(len(lower)):
            coefficients = np.zeros(len(edges))
            for mid in range(len(upper)):
                index = edge_index.get((mid, col))
                if index is not None:
                    coefficients[index] += block_upper[row, mid]
            for mid in range(len(lower)):
                index = edge_index.get((row, mid))
                if index is not None:
                    coefficients[index] -= block_lower[mid, col]
            constraints.append(-coefficients)  # scipy convention: A_ub x <= 0
    result = linprog(
        np.zeros(len(edges)),
        A_ub=np.array(constraints),
        b_ub=np.zeros(len(constraints)),
        bounds=[(1.0, None)] * len(edges),
        method="highs",
    )
    return result.success, result.message


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=3)
    args = parser.parse_args()
    for n in range(1, args.max_n + 1):
        matrix = positive_transfer(n, temperature=1.0, zeta=1.1, field=0.7)
        for m in range(n):
            success, message = solve_intertwiner(matrix, 2 * n, m)
            print(f"N={n} m={m}->{m+1} feasible={success} message={message}")


if __name__ == "__main__":
    main()
