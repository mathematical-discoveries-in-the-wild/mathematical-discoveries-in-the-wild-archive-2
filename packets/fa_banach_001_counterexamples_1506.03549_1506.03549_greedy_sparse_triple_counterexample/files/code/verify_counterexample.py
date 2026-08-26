#!/usr/bin/env python3
"""Exact rational verification of the coordinate-group counterexample."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement


SUPPORTS = (
    frozenset((0, 1)),
    frozenset((2, 3)),
    frozenset((0, 2)),
    frozenset((4,)),
)


def norm1(x: tuple[Fraction, ...]) -> Fraction:
    return sum(map(abs, x), Fraction())


def project(x: tuple[Fraction, ...], support: frozenset[int]) -> tuple[Fraction, ...]:
    return tuple(value if j in support else Fraction() for j, value in enumerate(x))


def subtract(x: tuple[Fraction, ...], y: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a - b for a, b in zip(x, y))


def greedy(x: tuple[Fraction, ...], steps: int) -> tuple[list[int], tuple[Fraction, ...]]:
    residual = x
    selected: list[int] = []
    for _ in range(steps):
        errors = [norm1(subtract(residual, project(residual, support))) for support in SUPPORTS]
        best = min(errors)
        minimizers = [i for i, error in enumerate(errors) if error == best]
        assert len(minimizers) == 1, (residual, errors)
        chosen = minimizers[0]
        selected.append(chosen)
        residual = subtract(residual, project(residual, SUPPORTS[chosen]))
    return selected, residual


def sigma_k(x: tuple[Fraction, ...], k: int) -> Fraction:
    best: Fraction | None = None
    for indices in combinations_with_replacement(range(len(SUPPORTS)), k):
        union = frozenset().union(*(SUPPORTS[i] for i in indices))
        error = norm1(subtract(x, project(x, union)))
        best = error if best is None else min(best, error)
    assert best is not None
    return best


def main() -> None:
    for epsilon in (Fraction(1, 2), Fraction(1, 10), Fraction(1, 1000)):
        x = (Fraction(2), Fraction(3, 2), Fraction(2), Fraction(1), epsilon)
        selected2, residual2 = greedy(x, 2)
        selected3, residual3 = greedy(x, 3)

        assert selected2 == [2, 0]
        assert selected3 == [2, 0, 1]
        assert norm1(residual2) == 1 + epsilon
        assert norm1(residual3) == epsilon
        assert sigma_k(x, 2) == epsilon
        assert sigma_k(x, 3) == 0

        ratio = norm1(residual2) / sigma_k(x, 2)
        print(
            f"epsilon={epsilon}: choices={[i + 1 for i in selected3]}, "
            f"g2={norm1(residual2)}, sigma2={sigma_k(x, 2)}, "
            f"ratio={ratio}, g3={norm1(residual3)}, sigma3={sigma_k(x, 3)}"
        )

    # The supports S1,S2,S4 span every coordinate, proving 3A=R^5.
    assert SUPPORTS[0] | SUPPORTS[1] | SUPPORTS[3] == frozenset(range(5))
    print("coordinate-group greedy counterexample: PASS")


if __name__ == "__main__":
    main()
