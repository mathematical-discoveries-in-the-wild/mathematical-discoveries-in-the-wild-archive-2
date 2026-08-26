"""Numerical sanity check for the real phase-difference identity.

This is not part of the proof.
"""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(210914454)
    worst = 0.0
    for _ in range(100_000):
        a = rng.uniform(-10.0, 10.0)
        b = rng.uniform(-10.0, 10.0)
        lhs = ((abs(a + b) - abs(b - a)) / 2.0) ** 2
        rhs = min(a * a, b * b)
        worst = max(worst, abs(lhs - rhs))
    print(f"maximum absolute error over 100000 trials: {worst:.3e}")


if __name__ == "__main__":
    main()

