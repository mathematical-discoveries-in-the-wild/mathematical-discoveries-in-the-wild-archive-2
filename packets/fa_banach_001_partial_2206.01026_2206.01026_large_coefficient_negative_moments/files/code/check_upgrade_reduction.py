#!/usr/bin/env python3
"""Finite regression checks for the unproved d=3 upgrade inequality.

Nothing in this file is used in the proof of the promoted large-coefficient
theorem.  It only checks the algebraic reduction and searches a finite grid
for contradictions to the proposed all-small extension.
"""

from __future__ import annotations

import argparse
import math


def ratio(beta: float, x: float, y: float, z: float) -> float:
    """Left/right ratio in scalar inequality (*) from the packet."""
    p = 3.0 - beta
    numerator = 1.0 - x**beta - y**beta - z**beta
    qform = 1.0 + x * x + y * y + z * z
    denominator = beta * 2.0 ** (p / 2.0) * (1.0 - x) * (1.0 - y) * (1.0 - z)
    return numerator * qform ** (p / 2.0) / denominator


def endpoint_margin(x: float, y: float, z: float) -> float:
    """Margin in the beta=2 endpoint reduction."""
    s2 = x * y + y * z + z * x
    s3 = x * y * z
    return (s2 - s3) - s2 * math.sqrt(max(0.0, 1.0 - s2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh", type=int, default=400)
    parser.add_argument("--beta-steps", type=int, default=100)
    args = parser.parse_args()

    worst = (-math.inf, None)
    endpoint_min = (math.inf, None)
    for ib in range(1, args.beta_steps):
        beta = 1.0 + ib / args.beta_steps
        for ix in range(args.mesh + 1):
            x = ix / args.mesh
            for iy in range(args.mesh + 1 - ix):
                y = iy / args.mesh
                z = max(0.0, 1.0 - x - y)
                if max(x, y, z) >= 1.0:
                    continue
                value = ratio(beta, x, y, z)
                if value > worst[0]:
                    worst = (value, (beta, x, y, z))
                margin = endpoint_margin(x, y, z)
                if margin < endpoint_min[0]:
                    endpoint_min = (margin, (x, y, z))

    print(f"largest finite-grid ratio: {worst[0]:.12f} at {worst[1]}")
    print(f"smallest beta=2 endpoint margin: {endpoint_min[0]:.12e} at {endpoint_min[1]}")
    if worst[0] > 1.0 + 1e-10:
        raise SystemExit("finite-grid contradiction found")
    if endpoint_min[0] < -1e-10:
        raise SystemExit("endpoint algebra regression found")


if __name__ == "__main__":
    main()
