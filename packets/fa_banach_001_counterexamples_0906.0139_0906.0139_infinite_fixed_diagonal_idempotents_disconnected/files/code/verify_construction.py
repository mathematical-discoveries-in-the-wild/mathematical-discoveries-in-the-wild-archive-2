#!/usr/bin/env python3
"""Numerical/exact sanity checks for the explicit idempotent construction.

The proof is infinite-dimensional and does not depend on this script.  The
script checks the finite algebraic identities and the first 2,000 basis
groups of the indexing construction.
"""

from __future__ import annotations

import math

import numpy as np


def phi(m: int, bit: int) -> int:
    if m == 0:
        return 1 if bit == 0 else 2
    if m == 1:
        return 3 if bit == 0 else 0
    return 2 * m + (1 if bit == 0 else 0)


def main() -> None:
    # Each original two-dimensional block is an idempotent of rank one.
    block = np.array([[-1.0, 1.0], [-2.0, 2.0]])
    assert np.array_equal(block @ block, block)
    assert np.linalg.matrix_rank(block) == 1

    # Columns give the new orthonormal basis in every three-vector group.
    orth = np.array(
        [
            [1 / math.sqrt(2), -1 / math.sqrt(2), 0.0],
            [1 / math.sqrt(6), 1 / math.sqrt(6), -2 / math.sqrt(6)],
            [1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)],
        ]
    )
    assert np.allclose(orth.T @ orth, np.eye(3), atol=1e-14)
    u_weights = np.sum(orth[:2, :] ** 2, axis=0)
    v_weights = orth[2, :] ** 2
    assert np.allclose(u_weights, np.full(3, 2 / 3), atol=1e-14)
    assert np.allclose(v_weights, np.full(3, 1 / 3), atol=1e-14)
    assert np.allclose(-u_weights + 2 * v_weights, np.zeros(3), atol=1e-14)

    groups = 2_000
    values = [phi(m, bit) for m in range(groups) for bit in (0, 1)]
    assert len(set(values)) == 2 * groups
    assert set(values) == set(range(2 * groups))
    assert all(phi(m, bit) != m for m in range(groups) for bit in (0, 1))

    # Directly apply R to the first `groups` triples using sparse coordinate
    # dictionaries.  No finite truncation itself can have an all-zero
    # idempotent diagonal because of the finite-dimensional trace identity.
    for m in range(groups):
        a, b = phi(m, 0), phi(m, 1)
        for column in range(3):
            w = {
                ("u", a): orth[0, column],
                ("u", b): orth[1, column],
                ("v", m): orth[2, column],
            }
            rw: dict[tuple[str, int], float] = {}
            for (kind, index), coefficient in w.items():
                if kind == "u":
                    rw[("u", index)] = rw.get(("u", index), 0.0) - coefficient
                    rw[("v", index)] = rw.get(("v", index), 0.0) - 2 * coefficient
                else:
                    rw[("u", index)] = rw.get(("u", index), 0.0) + coefficient
                    rw[("v", index)] = rw.get(("v", index), 0.0) + 2 * coefficient
            value = sum(coefficient * rw.get(key, 0.0) for key, coefficient in w.items())
            assert abs(value) < 2e-13

    print(
        "PASS: block idempotence/rank, orthogonality, weight cancellation, "
        f"bijection/no-fixed-pairing, and {3 * groups:,} diagonal values"
    )


if __name__ == "__main__":
    main()
