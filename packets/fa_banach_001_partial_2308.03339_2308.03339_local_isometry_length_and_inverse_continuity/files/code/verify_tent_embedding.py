"""Numerical spot checks for the exact tent-wave construction in the packet."""

from math import atan, floor
from random import Random


def tent(t: float) -> float:
    n = floor(t)
    r = t - n
    return min(r, 1.0 - r)


def F(t: float) -> tuple[float, float, float]:
    return tent(t), tent(t + 0.25), 0.1 * atan(t)


def linf(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


rng = Random(155)
for _ in range(20_000):
    center = rng.uniform(-100, 100)
    s = center + rng.uniform(-1 / 16, 1 / 16)
    t = center + rng.uniform(-1 / 16, 1 / 16)
    assert abs(linf(F(s), F(t)) - abs(s - t)) < 1e-12

assert linf(F(0), F(100)) < 1
print("20,000 local pairs passed; global contraction witnessed at 0 and 100")

