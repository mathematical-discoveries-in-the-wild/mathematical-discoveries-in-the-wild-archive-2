#!/usr/bin/env python3
"""Regression check for the anisotropically stretched regular polygons.

This checks finite cases only; the symbolic argument in the packet is the proof.
"""

from __future__ import annotations

import math


def main() -> None:
    stretch = 2.0
    for n in range(1, 101):
        m = 4 * n + 2
        vertices = [
            (
                stretch * math.cos(2.0 * math.pi * k / m),
                math.sin(2.0 * math.pi * k / m),
            )
            for k in range(m)
        ]
        lengths = []
        for k in range(m):
            x0, y0 = vertices[k]
            x1, y1 = vertices[(k + 1) % m]
            lengths.append(math.hypot(x1 - x0, y1 - y0))

        a = math.pi / m
        formula = [
            2.0
            * math.sin(a)
            * math.sqrt(
                stretch**2 * math.sin((2 * k + 1) * a) ** 2
                + math.cos((2 * k + 1) * a) ** 2
            )
            for k in range(m)
        ]
        assert max(abs(x - y) for x, y in zip(lengths, formula)) < 1.0e-12
        assert not math.isclose(lengths[0], lengths[n], rel_tol=1.0e-12)

    print("verified n=1,...,100 at stretch=2")


if __name__ == "__main__":
    main()

