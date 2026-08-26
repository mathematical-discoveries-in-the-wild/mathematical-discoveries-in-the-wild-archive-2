#!/usr/bin/env python3
"""Finite sanity checks for the lattice spectral-triple counterexample.

This script is not part of the proof.  It checks the shell multiplicities,
the logarithmic partial-sum ratio tending to 1/2, and numerical convergence
of the trace contributed by finitely many first-coordinate rows.
"""

from __future__ import annotations

import math


def shell_count(max_shell: int) -> int:
    return sum(m - 1 for m in range(2, max_shell + 1))


def shell_mass(max_shell: int) -> float:
    return sum((m - 1) / (1.0 + m * m) for m in range(2, max_shell + 1))


def row_mass(row: int, cutoff: int) -> float:
    return sum(1.0 / (1.0 + (row + j) ** 2) for j in range(1, cutoff + 1))


def main() -> None:
    shells = (10, 100, 1_000, 10_000, 100_000)
    print("shell  eigenvalues  logarithmic_ratio")
    previous_ratio = 0.0
    for max_shell in shells:
        count = shell_count(max_shell)
        expected = max_shell * (max_shell - 1) // 2
        assert count == expected
        ratio = shell_mass(max_shell) / math.log1p(count)
        assert ratio > previous_ratio
        previous_ratio = ratio
        print(f"{max_shell:6d}  {count:11d}  {ratio:.10f}")

    assert abs(previous_ratio - 0.5) < 0.05

    print("\nfinite-row trace approximations")
    for rows in (1, 2, 5, 10):
        coarse = sum(row_mass(i, 10_000) for i in range(1, rows + 1))
        fine = sum(row_mass(i, 100_000) for i in range(1, rows + 1))
        assert fine >= coarse
        # Integral comparison makes the omitted tail at most rows/cutoff.
        assert fine - coarse < rows / 10_000
        print(f"rows={rows:2d}  cutoff=100000  trace~{fine:.10f}")

    print("\nPASS: finite checks agree with the proved asymptotics.")


if __name__ == "__main__":
    main()

