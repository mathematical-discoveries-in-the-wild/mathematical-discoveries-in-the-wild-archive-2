#!/usr/bin/env python3
"""Arithmetic checks for the subcritical-potential proof.

The proof needs Q/2 < p < Q/(2-alpha).  It then uses the negative
resolvent exponent Q/(2p)-1 and local radial integrability exponent
Q-p(2-alpha).
"""

from __future__ import annotations


def witness_p(Q: float, alpha: float) -> float:
    lower = Q / 2.0
    upper = Q / (2.0 - alpha)
    return (lower + upper) / 2.0


def main() -> None:
    for Q in (4.0, 6.0, 8.0, 12.0):
        for alpha in (0.01, 0.1, 0.5, 1.0, 1.5, 1.9):
            p = witness_p(Q, alpha)
            radial = Q - p * (2.0 - alpha)
            resolvent = Q / (2.0 * p) - 1.0
            assert Q / 2.0 < p < Q / (2.0 - alpha)
            assert radial > 0.0
            assert resolvent < 0.0
            assert 2.0 * (2.0 - alpha) < Q
            print(
                f"Q={Q:>4.0f} alpha={alpha:>4.2f} p={p:>10.6f} "
                f"radial={radial:>9.6f} resolvent={resolvent:>10.6f} [PASS]"
            )

    print("all exponent-window and local-L2 checks [PASS]")


if __name__ == "__main__":
    main()
