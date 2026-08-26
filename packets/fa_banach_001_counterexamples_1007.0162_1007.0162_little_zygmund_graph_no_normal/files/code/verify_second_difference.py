"""Numerical sanity checks for the little-Zygmund graph counterexample.

This script is illustrative only; the proof packet gives the uniform analytic
estimate.  The cutoff below is C^2 rather than the C-infinity cutoff used in
the theorem, which is enough for sampling away from its transition endpoints.
"""

from __future__ import annotations

import math
import numpy as np

R0 = math.exp(-3.0)


def cutoff(r: float) -> float:
    if r <= R0:
        return 1.0
    if r >= 2.0 * R0:
        return 0.0
    t = (r - R0) / R0
    return 1.0 - 10.0 * t**3 + 15.0 * t**4 - 6.0 * t**5


def f(x: float) -> float:
    if x == 0.0:
        return 0.0
    return cutoff(abs(x)) * x * math.sin(math.log(math.log(math.e / abs(x))))


def sampled_ratio(h: float) -> float:
    near = np.linspace(-3.0 * h, 3.0 * h, 4001)
    if 2.0 * h < R0 / 2.0:
        positive = np.geomspace(2.0 * h, R0 / 2.0, 5000)
        points = np.concatenate((near, positive, -positive))
    else:
        points = near
    values = [abs(f(float(x + h)) + f(float(x - h)) - 2.0 * f(float(x))) / h
              for x in points]
    return max(values)


def main() -> None:
    for h in (1e-3, 1e-4, 1e-6, 1e-9, 1e-12):
        print(f"h={h:.0e} sampled second-difference/h={sampled_ratio(h):.8f}")

    for label, phase in (("plus", math.pi / 2.0), ("minus", 3.0 * math.pi / 2.0)):
        x = math.e * math.exp(-math.exp(phase))
        print(f"{label} phase: x={x:.6e}, f(x)/x={f(x) / x:.12f}")


if __name__ == "__main__":
    main()
