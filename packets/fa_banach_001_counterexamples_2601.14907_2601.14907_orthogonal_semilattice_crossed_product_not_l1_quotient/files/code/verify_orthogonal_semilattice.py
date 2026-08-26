#!/usr/bin/env python3
"""Finite sanity checks for the orthogonal-semilattice counterexample."""

from __future__ import annotations

import math
import random


def pointwise_product(a: list[complex], b: list[complex]) -> list[complex]:
    """Convolution in the finite orthogonal semilattice truncation."""
    return [x * y for x, y in zip(a, b, strict=True)]


def l1_norm(a: list[complex]) -> float:
    return sum(abs(x) for x in a)


def max_norm(a: list[complex]) -> float:
    return max((abs(x) for x in a), default=0.0)


def main() -> None:
    rng = random.Random(260114907)
    for size in (1, 2, 5, 20):
        a = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(size)]
        b = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(size)]
        product = pointwise_product(a, b)
        assert max_norm(product) <= max_norm(a) * max_norm(b) + 1e-12

        ones = [1.0] * size
        assert math.isclose(l1_norm(ones), float(size))
        assert math.isclose(max_norm(ones), 1.0)
        print(f"N={size:2d}: ||1_N||_1={l1_norm(ones):.0f}, "
              f"||1_N||_max={max_norm(ones):.0f}")

    # Truncations h_N=(1,1/2,...,1/N) converge in sup norm to an element of c0.
    # Their l1 norms are harmonic and diverge.
    previous = [1.0 / n for n in range(1, 65)]
    current = [1.0 / n for n in range(1, 129)]
    padded_previous = previous + [0.0] * (len(current) - len(previous))
    sup_tail = max_norm([x - y for x, y in zip(current, padded_previous, strict=True)])
    assert math.isclose(sup_tail, 1.0 / 65.0)
    assert l1_norm(current) > l1_norm(previous)
    print(f"harmonic truncations: sup tail={sup_tail:.8f}, "
          f"l1 norms {l1_norm(previous):.6f} < {l1_norm(current):.6f}")


if __name__ == "__main__":
    main()
