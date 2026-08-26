#!/usr/bin/env python3
"""Numerical sanity checks for the staircase perturbation lemma.

This checks finite staircase truncations for power envelopes m(t)=t^(-1/q).
It is not part of the proof; the packet proves the bounds symbolically.
"""

from __future__ import annotations

import math


def integral_on_interval(low: float, high: float, value: float, power: float) -> float:
    return max(0.0, high - low) * value**power


def build_segments(q: float, ratio: float, levels: int = 20):
    # t_n = ratio^n for n=1,...,levels.  The deepest finite block is
    # continued to zero, which only makes the finite sanity test easier.
    t = [ratio**n for n in range(1, levels + 1)]
    a = [2.0 ** (-(n + 1)) * t[n] ** (-1.0 / q) for n in range(levels)]
    assert all(a[n + 1] >= a[n] for n in range(levels - 1))

    segments = [(0.0, t[-1], a[-1])]
    for n in range(levels - 1):
        segments.append((t[n + 1], t[n], a[n]))
    segments.append((t[0], 1.0, 0.0))
    return t, a, segments


def truncated_integrals(tau: float, segments, p: float):
    head = 0.0
    tail = 0.0
    for low, high, value in segments:
        head_high = min(high, tau)
        if head_high > low:
            head += integral_on_interval(low, head_high, value, p)
        tail_low = max(low, tau)
        if high > tail_low:
            tail += integral_on_interval(tail_low, high, value, 2.0)
    return head, tail


def check_case(p: float, q: float, ratio: float) -> tuple[float, float]:
    t_nodes, _, segments = build_segments(q, ratio)
    lp_mass = sum(integral_on_interval(low, high, value, p) for low, high, value in segments)
    assert math.isfinite(lp_mass) and lp_mass > 0.0

    lower = max(t_nodes[-1] * 1.0e-3, 1.0e-30)
    samples = 4000
    max_ratio = 0.0
    for j in range(samples):
        alpha = j / (samples - 1)
        tau = math.exp(math.log(lower) * (1.0 - alpha))
        head, tail = truncated_integrals(tau, segments, p)
        tp_u = (head / tau) ** (1.0 / p) + math.sqrt(tail / tau)
        m_tau = tau ** (-1.0 / q)
        quotient = tp_u / m_tau
        assert math.isfinite(quotient)
        max_ratio = max(max_ratio, quotient)

    # A deliberately generous regression threshold.  The proof establishes a
    # finite constant depending only on p and the geometric coefficients.
    assert max_ratio < 20.0, (p, q, ratio, max_ratio)
    return lp_mass, max_ratio


def main() -> None:
    exponent_pairs = [(1.0, 1.25), (1.3, 1.55), (1.7, 1.85), (1.9, 1.95)]
    mesh_ratios = [0.03, 0.08, 0.15]
    cases = 0
    worst = (0.0, None)
    for p, q in exponent_pairs:
        for ratio in mesh_ratios:
            lp_mass, max_ratio = check_case(p, q, ratio)
            cases += 1
            if max_ratio > worst[0]:
                worst = (max_ratio, (p, q, ratio, lp_mass))
            print(
                f"PASS p={p:.2f} q={q:.2f} mesh={ratio:.2f} "
                f"Lp_mass={lp_mass:.6g} max(Tu/m)={max_ratio:.6g}"
            )
    print(f"PASS all {cases} cases; worst={worst[0]:.6g} at {worst[1]}")


if __name__ == "__main__":
    main()

