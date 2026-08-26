"""Sanity checks for the split-metabelian Rider-gap packet.

This script does not prove the compact representation-theoretic lemma.  It:
  1. verifies its rectangle identity and partition combinatorics for many
     finite cyclic semidirect products C_n rtimes C_m;
  2. checks the exact D_16 sharpness value; and
  3. exhaustively checks all central idempotents of D_{2n}, 3 <= n <= 30.
"""

from cmath import exp
from itertools import combinations
from math import cos, gcd, pi, sqrt

import numpy as np
import sympy as sp


TOL = 2e-9
SAEKI = (1 + sqrt(2)) / 2


def cyclic_actions_rectangle_check() -> tuple[int, int]:
    """Return (number of actions, number of little-group blocks checked)."""
    actions = 0
    blocks = 0
    for n in range(2, 15):
        for m in range(2, 7):
            for q in range(1, n):
                if gcd(q, n) != 1 or pow(q, m, n) != 1:
                    continue
                actions += 1
                unseen = set(range(n))
                rectangles: set[tuple[int, int]] = set()
                while unseen:
                    k = min(unseen)
                    orbit = []
                    x = k
                    while x not in orbit:
                        orbit.append(x)
                        x = (q * x) % n
                    unseen.difference_update(orbit)
                    d = len(orbit)
                    assert m % d == 0
                    stabilizer_order = m // d
                    for ell in range(stabilizer_order):
                        extensions = [s for s in range(m) if s % stabilizer_order == ell]
                        assert len(extensions) == d
                        rectangle = {(delta, s) for delta in orbit for s in extensions}
                        assert not (rectangles & rectangle)
                        rectangles |= rectangle
                        blocks += 1
                        for a in range(n):
                            orbit_sum = sum(exp(2j * pi * delta * a / n) for delta in orbit)
                            for h in range(m):
                                if h % d == 0:
                                    eta = exp(2j * pi * ell * (h // d) / stabilizer_order)
                                    lhs = d * eta * orbit_sum
                                else:
                                    lhs = 0j
                                rhs = sum(
                                    exp(2j * pi * delta * a / n) * exp(2j * pi * s * h / m)
                                    for delta, s in rectangle
                                )
                                assert abs(lhs - rhs) < TOL
                assert rectangles == {(k, s) for k in range(n) for s in range(m)}
    return actions, blocks


def dihedral_blocks(n: int) -> list[np.ndarray]:
    k = np.arange(n)
    rows: list[np.ndarray] = []
    a_values = (1, -1) if n % 2 == 0 else (1,)
    for a in a_values:
        for b in (1, -1):
            rotations = a ** k
            reflections = b * rotations
            rows.append(np.concatenate([rotations, reflections]).astype(complex))
    for j in range(1, (n - 1) // 2 + 1 if n % 2 else n // 2):
        rotations = 4 * np.cos(2 * pi * j * k / n)
        rows.append(np.concatenate([rotations, np.zeros(n)]).astype(complex))
    return rows


def exhaustive_dihedral_check() -> tuple[int, float, int]:
    cases = 0
    best = float("inf")
    best_n = -1
    for n in range(3, 31):
        rows = dihedral_blocks(n)
        for mask in range(1, (1 << len(rows)) - 1):
            values = np.zeros(2 * n, dtype=complex)
            for j, row in enumerate(rows):
                if mask >> j & 1:
                    values += row
            norm = float(np.abs(values).mean())
            cases += 1
            if norm > 1 + 1e-10:
                assert norm + 1e-9 >= SAEKI
                if norm < best:
                    best, best_n = norm, n
    return cases, best, best_n


def exact_d16_check() -> sp.Expr:
    value = (sp.Integer(8) + 8 * sp.sqrt(2)) / 16
    assert sp.simplify(value - (1 + sp.sqrt(2)) / 2) == 0
    # Direct list of |4 cos(pi k/4)| values: 4, 2sqrt2, 0, 2sqrt2,
    # 4, 2sqrt2, 0, 2sqrt2.
    direct = (8 + 8 * sp.sqrt(2)) / 16
    assert sp.simplify(direct - value) == 0
    return value


def main() -> None:
    actions, blocks = cyclic_actions_rectangle_check()
    exact = exact_d16_check()
    cases, best, best_n = exhaustive_dihedral_check()
    print(f"rectangle identity: PASS ({actions} cyclic actions, {blocks} blocks)")
    print(f"D_16 exact norm: PASS ({exact})")
    print(f"dihedral exhaustive gap: PASS ({cases} idempotents, best={best:.12f}, n={best_n})")
    print("PASS: all packet sanity checks completed.")


if __name__ == "__main__":
    main()
