"""Numerical sanity checks for the separated-interval structure factor."""

from __future__ import annotations

import math


def omega(u: float, lengths: list[float]) -> float:
    return sum(min(u, ell) for ell in lengths)


def main() -> None:
    print("exponential lengths: omega/(u log(1/u))")
    exp_lengths = [2.0 ** (-n) for n in range(1, 2000)]
    for k in (8, 12, 16, 20):
        u = 2.0 ** (-k)
        ratio = omega(u, exp_lengths) / (u * math.log(1.0 / u))
        print(k, ratio)

    print("polynomial p=2: omega/sqrt(u)")
    poly_lengths = [n ** -2.0 for n in range(1, 2_000_000)]
    for k in (4, 6, 8, 10):
        u = 10.0 ** (-k)
        ratio = omega(u, poly_lengths) / math.sqrt(u)
        print(k, ratio)

    print("exact finite overlap identity")
    lengths = [0.4, 0.1, 0.03, 0.007]
    for u in (0.005, 0.02, 0.08, 0.2):
        overlap = sum(max(ell - u, 0.0) for ell in lengths)
        structure = sum(lengths) - overlap
        print(u, structure, omega(u, lengths), abs(structure - omega(u, lengths)))


if __name__ == "__main__":
    main()
