#!/usr/bin/env python3
"""Finite sanity checks for the dyadic-block Schrodinger counterexample.

This verifies only numerical consequences of the proof.  It is not a proof of
Dixmier measurability or of the modulated-operator eigenvalue formula.
"""

from __future__ import annotations

import math


def potential(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    block = n.bit_length() - 1
    if n == 1 << block:
        block -= 1
    return block % 2


def cubic_test_diagonal(n: int) -> int:
    """Diagonal of p(H), p(t)=1+t+t^2+t^3, on the infinite half-line."""
    a_n = 2 + potential(n)
    neighbours = []
    if n > 1:
        neighbours.append(n - 1)
    neighbours.append(n + 1)
    degree = len(neighbours)
    h2 = a_n * a_n + degree
    h3 = a_n**3 + sum(2 * a_n + 2 + potential(k) for k in neighbours)
    return 1 + a_n + h2 + h3


def main() -> None:
    arithmetic_ones = 0
    harmonic_total = 0.0
    harmonic_ones = 0.0
    harmonic_cubic = 0.0
    rows = []
    targets = {2**e for e in range(10, 21)}

    for n in range(1, max(targets) + 1):
        v_n = potential(n)
        arithmetic_ones += v_n
        harmonic_total += 1.0 / n
        harmonic_ones += v_n / n
        harmonic_cubic += cubic_test_diagonal(n) / n
        if n in targets:
            rows.append(
                (
                    n,
                    arithmetic_ones / n,
                    harmonic_ones / math.log(2 + n),
                    harmonic_cubic / math.log(2 + n),
                )
            )

    print("N arithmetic(v) harmonic(v)/log harmonic(p(H))/log")
    for row in rows:
        print(f"{row[0]:7d} {row[1]:.8f} {row[2]:.8f} {row[3]:.8f}")

    even = rows[-3]  # N=2^18
    odd = rows[-2]   # N=2^19
    last = rows[-1]  # N=2^20
    assert abs(even[1] - 2 / 3) < 1e-4
    assert abs(odd[1] - 1 / 3) < 1e-4
    # The proved error is only O(1/log N), so convergence at 2^20 is slow.
    assert abs(last[2] - 0.5) < 0.07

    # For constant potential c, the bulk diagonal of p(H) is 29 for c=0
    # and 60 for c=1, so the predicted logarithmic limit is 44.5.
    assert abs(last[3] - 44.5) < 2.5
    print("checks: PASS (predicted cubic logarithmic limit = 44.5)")


if __name__ == "__main__":
    main()
