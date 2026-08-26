#!/usr/bin/env python3
"""Exact verification of the three-element weak-exactness counterexample."""

from __future__ import annotations

import itertools


S = (0, 1, 2)
TABLE = (
    (0, 0, 2),
    (0, 1, 2),
    (0, 2, 2),
)


def mul(s: int, t: int) -> int:
    return TABLE[s][t]


def phi(s: int) -> int:
    """Augmentation character on basis elements."""
    return 1


def psi(s: int) -> int:
    """Coefficient-at-the-identity character on basis elements."""
    return int(s == 1)


def derivation(s: int) -> int:
    """D(delta_0)=e, D(delta_1)=D(delta_2)=0."""
    return int(s == 0)


def main() -> None:
    assert all(
        mul(mul(r, s), t) == mul(r, mul(s, t))
        for r, s, t in itertools.product(S, repeat=3)
    )
    assert all(mul(1, s) == s == mul(s, 1) for s in S)
    assert set(mul(s, t) for s in S for t in S) == set(S)
    assert all(phi(mul(s, t)) == phi(s) * phi(t) for s in S for t in S)
    assert all(psi(mul(s, t)) == psi(s) * psi(t) for s in S for t in S)

    # The (phi,psi)-derivation identity.
    assert all(
        derivation(mul(s, t))
        == phi(s) * derivation(t) + derivation(s) * psi(t)
        for s in S
        for t in S
    )

    # Inner derivations have values lambda*(1,0,1); D has values (1,0,0).
    inner_pattern = tuple(phi(s) - psi(s) for s in S)
    d_pattern = tuple(derivation(s) for s in S)
    assert inner_pattern == (1, 0, 1)
    assert d_pattern == (1, 0, 0)
    assert d_pattern != inner_pattern
    print("verified associative unital monoid, injective coproduct, derivation, non-innerness")
    print("table", TABLE)
    print("inner_pattern", inner_pattern, "derivation_pattern", d_pattern)


if __name__ == "__main__":
    main()
