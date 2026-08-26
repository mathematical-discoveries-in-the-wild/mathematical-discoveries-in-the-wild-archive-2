#!/usr/bin/env python3
"""Numerical transcription checks for the coordinate-axis MDM bounds.

The proof in the packet is analytic.  This script only checks the stated
antiderivative, constants, and cap inclusions on a representative grid.
"""

import math


def main() -> None:
    global_bound = 1.0 + math.pi / 2.0
    assert math.isclose(math.asin(1.0) - math.asin(0.0), math.pi / 2.0)

    radii = [10.0 ** exponent for exponent in range(-6, 4)]
    radii += [0.03, 0.2, 0.7, 1.0, 3.0]
    for radius in radii:
        epsilon = min(1.0 / 8.0, radius / 4.0, radius * radius / 8.0)
        rho = epsilon / 2.0
        r0 = 1.0 - epsilon
        assert r0 + rho < 1.0
        assert 1.5 * epsilon < radius
        assert 2.0 * epsilon < radius * radius
        local_bound = 2.0 / epsilon + math.acos(r0)
        assert math.isfinite(local_bound)

    print(f"global endpoint bound = 1 + pi/2 = {global_bound:.12f}")
    print(f"checked cap constants for {len(radii)} positive radii")
    print("all transcription checks passed")


if __name__ == "__main__":
    main()
