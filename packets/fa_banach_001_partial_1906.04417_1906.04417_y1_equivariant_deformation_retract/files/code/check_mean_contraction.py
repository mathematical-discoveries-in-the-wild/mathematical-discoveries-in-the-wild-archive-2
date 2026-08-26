"""Numerical stress tests for the Y_1 normalized-mean contraction.

These checks illustrate the exact proof; they do not replace it.
"""

from __future__ import annotations

import numpy as np


def variation(g: np.ndarray) -> float:
    return float(np.abs(np.diff(g)).sum())


def check_phase(g: np.ndarray, label: str) -> None:
    var = variation(g)
    if var > np.pi + 1.0e-10:
        raise AssertionError(f"{label}: variation {var} exceeds pi")

    h = np.exp(1j * g)
    mean = h.mean()
    if abs(mean) < 1.0e-8:
        raise AssertionError(f"{label}: unexpectedly tiny mean {mean}")

    u = mean / abs(mean)
    antipode_distance = float(np.min(np.abs(h + u)))
    if antipode_distance < 1.0e-8:
        raise AssertionError(f"{label}: mean antipode met by phase curve")

    theta = np.unwrap(np.angle(np.conj(u) * h))
    # Since the curve avoids the mean antipode, the unwrapped and principal
    # branches agree up to one constant multiple of 2*pi.
    for s in (0.0, 0.2, 0.5, 0.8, 1.0):
        contracted = (1.0 - s) * theta
        got = variation(contracted)
        want = (1.0 - s) * variation(theta)
        if not np.isclose(got, want, atol=2.0e-10, rtol=2.0e-10):
            raise AssertionError(f"{label}: variation scaling failed at {s}")

    print(
        f"{label}: variation={var:.8f}, |mean|={abs(mean):.8f}, "
        f"antipode_gap={antipode_distance:.8f}"
    )


def main() -> None:
    grid = np.linspace(0.0, 1.0, 20001)

    # A smooth monotone curve attaining the sharp total variation pi.
    smoothstep = 3.0 * grid**2 - 2.0 * grid**3
    check_phase(np.pi * smoothstep, "sharp_monotone_semicircle")

    rng = np.random.default_rng(190604417)
    for sample in range(40):
        g = np.zeros_like(grid)
        for frequency in range(1, 7):
            a, b = rng.normal(size=2)
            g += a * np.sin(2.0 * np.pi * frequency * grid)
            g += b * np.cos(2.0 * np.pi * frequency * grid)
        var = variation(g)
        scale = rng.uniform(0.05, 0.999) * np.pi / var
        check_phase(scale * g, f"random_{sample:02d}")

    print("all normalized-mean contraction stress tests passed")


if __name__ == "__main__":
    main()
