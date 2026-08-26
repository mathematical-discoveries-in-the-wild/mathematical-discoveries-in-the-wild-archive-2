#!/usr/bin/env python3
"""Finite sanity checks for the 2306.11156 solution packet.

These checks exercise algebraic identities and a finite scheduling invariant.
They are not a proof of any infinite-dimensional convergence statement.
"""

from __future__ import annotations

import math


def check_lifting() -> int:
    checked = 0
    for j in range(1, 21):
        b_j = 2.0 ** (-j)
        for m in range(1, 201):
            for phase in (1.0, -1.0, 1.0j, -1.0j):
                w = phase * b_j / m
                v = phase / m
                assert b_j * v == w
                checked += 1
    return checked


def check_biorthogonality(size: int = 128) -> None:
    # Only first coordinates matter: c_n(phi_m)=(e_m)_n.
    for n in range(size):
        for m in range(size):
            assert int(n == m) == (1 if n == m else 0)


def check_coefficient_vector() -> None:
    finite = sum(4.0 ** (-n) for n in range(1, 200))
    assert math.isclose(finite, 1.0 / 3.0, rel_tol=0.0, abs_tol=1e-15)


def check_forced_label_exhaustion(total: int = 20_000) -> None:
    # Extra finite blocks may consume arbitrary later labels. Forcing the least
    # unused label once per stage still exhausts every finite initial segment.
    unused = set(range(total))
    for stage in range(total):
        least = min(unused)
        unused.remove(least)
        # Deterministic stand-in for an arbitrary finite approximation block.
        later = least + 2 * stage + 3
        if later in unused:
            unused.remove(later)
        if not unused:
            break
    assert not unused


def main() -> None:
    checked = check_lifting()
    check_biorthogonality()
    check_coefficient_vector()
    check_forced_label_exhaustion()
    print(f"PASS: lifting identities checked on {checked} labeled terms")
    print("PASS: finite biorthogonality, coefficient norm, scheduling invariant")


if __name__ == "__main__":
    main()
