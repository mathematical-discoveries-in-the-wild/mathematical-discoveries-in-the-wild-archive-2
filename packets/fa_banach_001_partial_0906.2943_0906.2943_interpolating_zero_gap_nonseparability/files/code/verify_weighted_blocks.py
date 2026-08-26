#!/usr/bin/env python3
"""Finite checks for the weighted Cauchy-block construction; not a proof."""

from __future__ import annotations

import cmath
import random


def main() -> None:
    rng = random.Random(9062943)
    blocks: list[list[complex]] = []
    start = 50.0
    for k in range(1, 6):
        height = 0.08 / k
        block = [complex(start + 3.0 * j, height) for j in range(12 * k)]
        blocks.append(block)
        start = 1.0e4 * (max(abs(z) for z in block) + 1.0)

    trials = 80
    worst_energy_error = 0.0
    worst_upper_ratio = 0.0
    worst_recovery_error = 0.0
    for _ in range(trials):
        d = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in blocks]
        dnorm = max(abs(x) for x in d)
        lambdas: list[list[complex]] = []
        previous = 0.0 + 0.0j
        for values, target in zip(blocks, d):
            delta = target - previous
            mass = sum(z.imag for z in values)
            lam = [delta * z.imag / mass for z in values]
            assert abs(sum(lam) - delta) < 1e-12
            energy = sum(abs(a) ** 2 / z.imag for a, z in zip(lam, values))
            expected = abs(delta) ** 2 / mass
            worst_energy_error = max(worst_energy_error, abs(energy - expected))
            lambdas.append(lam)
            previous = target

        def cminus(y: float) -> complex:
            return sum(
                a / (z.conjugate() - 1j * y)
                for values, lam in zip(blocks, lambdas)
                for z, a in zip(values, lam)
            )

        def cplus(y: float) -> complex:
            return sum(
                a.conjugate() / (z - 1j * y)
                for values, lam in zip(blocks, lambdas)
                for z, a in zip(values, lam)
            )

        grid = [1.0]
        for values in blocks:
            p = min(abs(z) for z in values)
            q = max(abs(z) for z in values)
            grid.extend([p, (p * q) ** 0.5, q])
        for left, right in zip(blocks[:-1], blocks[1:]):
            grid.append((max(abs(z) for z in left) * min(abs(z) for z in right)) ** 0.5)
        for y in grid:
            worst_upper_ratio = max(
                worst_upper_ratio,
                y * abs(cminus(y)) / max(dnorm, 1e-15),
                y * abs(cplus(y)) / max(dnorm, 1e-15),
            )

        for k in range(len(blocks) - 1):
            y = (
                sum(max(abs(z) for z in block) for block in blocks[: k + 1])
                * min(abs(z) for z in blocks[k + 1])
            ) ** 0.5
            recovered = -1j * y * cminus(y)
            worst_recovery_error = max(
                worst_recovery_error, abs(recovered - d[k]) / max(dnorm, 1e-15)
            )

    assert worst_energy_error < 1e-10
    assert worst_upper_ratio < 8.0
    assert worst_recovery_error < 0.08
    print(f"trials={trials}")
    print(f"worst_energy_identity_error={worst_energy_error:.3e}")
    print(f"worst_scaled_cauchy_ratio={worst_upper_ratio:.6f}")
    print(f"worst_block_recovery_relative_error={worst_recovery_error:.6f}")
    print("finite weighted-block checks passed (not a proof)")


if __name__ == "__main__":
    main()
