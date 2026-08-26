#!/usr/bin/env python3
"""Finite truncation check for the coefficient sequences in the proof.

This is illustrative only.  The divergence/convergence statements are proved
by their exact power exponents in the packet.
"""

from __future__ import annotations


def partial_sums(q: float, cutoffs: tuple[int, ...]) -> None:
    r = (1.0 + 1.0 / q) / 2.0
    print(f"q={q:g}, r={r:.8f}, input exponent={-r*q:.8f}, "
          f"output exponent={q - 1.0 - r*q:.8f}")
    for n in cutoffs:
        input_sum = sum(m ** (-r * q) for m in range(1, n + 1))
        output_sum = sum(m ** (q - 1.0 - r * q) for m in range(1, n + 1))
        print(f"  N={n:6d}  input={input_sum:12.6f}  output={output_sum:12.6f}")


if __name__ == "__main__":
    for exponent in (1.25, 2.0, 4.0, 10.0):
        partial_sums(exponent, (10, 100, 1_000, 10_000))
