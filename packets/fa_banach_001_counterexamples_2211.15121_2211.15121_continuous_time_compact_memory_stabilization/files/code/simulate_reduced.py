#!/usr/bin/env python3
"""Numerical sanity check for the reduced compact-memory counterexample.

This is not part of the proof. It integrates the exact (w,u,v) system by RK4
for deterministic initial scales and phases and checks the generous proved
envelope ||x(t)|| <= 50 sqrt(||x(0)||).
"""

from __future__ import annotations

import math


def rhs(state: tuple[float, float, float]) -> tuple[float, float, float]:
    w, u, v = state
    den = w * w + u * u + v * v
    q = 0.0 if den == 0.0 else (w * w - u * u - v * v) / den
    return 0.5 * q * w, w, 0.0


def add(
    x: tuple[float, float, float],
    k: tuple[float, float, float],
    factor: float,
) -> tuple[float, float, float]:
    return tuple(a + factor * b for a, b in zip(x, k))  # type: ignore[return-value]


def step(
    state: tuple[float, float, float], dt: float
) -> tuple[float, float, float]:
    k1 = rhs(state)
    k2 = rhs(add(state, k1, dt / 2.0))
    k3 = rhs(add(state, k2, dt / 2.0))
    k4 = rhs(add(state, k3, dt))
    nxt = tuple(
        a + dt * (b + 2.0 * c + 2.0 * d + e) / 6.0
        for a, b, c, d, e in zip(state, k1, k2, k3, k4)
    )
    return max(0.0, nxt[0]), nxt[1], nxt[2]


def state_norm(state: tuple[float, float, float]) -> float:
    w, u, v = state
    return math.sqrt(w**4 + u * u + v * v)


def main() -> None:
    dt = 0.005
    steps = int(30.0 / dt)
    worst_ratio = 0.0
    tested = 0

    for exponent in range(1, 11):
        eta = 10.0 ** (-exponent)
        for y_fraction in (0.0, 0.01, 0.1, 0.5, 0.9, 1.0):
            s0 = eta * y_fraction
            a_abs = math.sqrt(max(0.0, eta * eta - s0 * s0))
            for phase_index in range(16):
                phase = 2.0 * math.pi * phase_index / 16.0
                state = (
                    math.sqrt(s0),
                    a_abs * math.cos(phase),
                    a_abs * math.sin(phase),
                )
                max_norm = state_norm(state)
                for _ in range(steps):
                    state = step(state, dt)
                    max_norm = max(max_norm, state_norm(state))
                ratio = max_norm / math.sqrt(eta)
                worst_ratio = max(worst_ratio, ratio)
                assert max_norm <= 50.0 * math.sqrt(eta) * (1.0 + 1e-8)
                tested += 1

    print(f"tested={tested} trajectories")
    print(f"worst max_norm/sqrt(initial_norm)={worst_ratio:.8f}")
    print("all sampled trajectories satisfy the proved envelope")


if __name__ == "__main__":
    main()
