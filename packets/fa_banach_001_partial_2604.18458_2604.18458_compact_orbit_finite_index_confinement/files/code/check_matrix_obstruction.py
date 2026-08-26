#!/usr/bin/env python3
"""Exact sanity checks for the finite-matrix obstruction."""

from fractions import Fraction


def check_dimension(d: int) -> None:
    # It suffices to check scalar expectation >= (1/d) id on the extremal
    # rays of the cone of nonnegative diagonal matrices.
    for coordinate in range(d):
        ray = [Fraction(0) for _ in range(d)]
        ray[coordinate] = Fraction(1)
        trace = sum(ray) / d
        dominated = [trace - value / d for value in ray]
        assert all(value >= 0 for value in dominated)

    # A traceless direction is completely erased by scalar expectation.
    traceless = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (d - 2)
    assert sum(traceless) / d == 0
    assert any(value != 0 for value in traceless)


def main() -> None:
    for dimension in range(2, 13):
        check_dimension(dimension)
    print("exact finite-matrix obstruction checks passed: dimensions 2..12")


if __name__ == "__main__":
    main()
