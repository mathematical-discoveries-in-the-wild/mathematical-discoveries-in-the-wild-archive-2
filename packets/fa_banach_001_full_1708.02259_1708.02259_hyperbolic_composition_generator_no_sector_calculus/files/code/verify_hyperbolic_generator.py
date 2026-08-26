#!/usr/bin/env python3
"""Sanity checks for the hyperbolic-composition generator packet."""

from __future__ import annotations

import argparse
import cmath
import math
import random


def alpha(r: float, z: complex) -> complex:
    return (z + r) / (1.0 + r * z)


def check_flow_identities() -> tuple[float, float]:
    points = [0.0, 0.2 + 0.1j, -0.43 + 0.31j, 0.77j]
    times = [0.03, 0.2, 0.71, 1.4]
    group_error = 0.0
    reflection_error = 0.0
    for z in points:
        for s in times:
            for t in times:
                lhs = alpha(math.tanh(s), alpha(math.tanh(t), z))
                rhs = alpha(math.tanh(s + t), z)
                group_error = max(group_error, abs(lhs - rhs))
            r = math.tanh(s)
            lhs = -alpha(r, -z)
            rhs = alpha(-r, z)
            reflection_error = max(reflection_error, abs(lhs - rhs))
    return group_error, reflection_error


def weight_families(size: int) -> dict[str, list[float]]:
    rng = random.Random(170802259)
    random_logs = [rng.uniform(-18.0, 18.0) for _ in range(size)]
    return {
        "constant": [1.0 for _ in range(size)],
        "alternating": [3.0 if n % 2 == 0 else 1.0 for n in range(size)],
        "polynomial": [(n + 1.0) ** 2.75 for n in range(size)],
        "geometric": [math.exp(0.025 * n) for n in range(size)],
        "pseudorandom": [math.exp(x) for x in random_logs],
    }


def check_weights(beta: list[float], max_n: int) -> tuple[float, int]:
    worst_margin = math.inf
    witness_count = 0
    for n in range(1, max_n + 1):
        forward = n * beta[n + 1] / beta[n]
        backward_next = (n + 1) * beta[n] / beta[n + 1]
        target = math.sqrt(n * (n + 1))
        margin = max(forward, backward_next) / target
        worst_margin = min(worst_margin, margin)
        if margin + 1e-12 < 1.0:
            raise AssertionError((n, forward, backward_next, target, margin))
        if max(forward, backward_next) >= target:
            witness_count += 1
        product_error = abs(forward * backward_next - n * (n + 1))
        if product_error > 1e-8 * n * (n + 1):
            raise AssertionError(("product identity", n, product_error))
    return worst_margin, witness_count


def run_suite() -> None:
    max_n = 500
    group_error, reflection_error = check_flow_identities()
    if group_error > 2e-13 or reflection_error > 2e-13:
        raise AssertionError((group_error, reflection_error))

    print(f"flow group max error: {group_error:.3e}")
    print(f"reflection max error: {reflection_error:.3e}")
    for name, beta in weight_families(max_n + 2).items():
        margin, count = check_weights(beta, max_n)
        print(
            f"{name:12s}: PASS n=1..{max_n}, "
            f"minimum normalized max-coefficient={margin:.12f}, "
            f"witnesses={count}"
        )
    print("OVERALL: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", action="store_true")
    args = parser.parse_args()
    if args.suite:
        run_suite()
    else:
        parser.error("use --suite")


if __name__ == "__main__":
    main()
