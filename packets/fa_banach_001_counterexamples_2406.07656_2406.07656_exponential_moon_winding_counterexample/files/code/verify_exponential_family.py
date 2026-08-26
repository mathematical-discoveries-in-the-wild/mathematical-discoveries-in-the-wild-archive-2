#!/usr/bin/env python3
"""Numerical sanity checks and figure for the exponential-symbol theorem."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def phi(z: np.ndarray | complex, rho: float = np.pi) -> np.ndarray | complex:
    return np.exp(1j * rho * z)


def winding(curve: np.ndarray, c: complex) -> float:
    increments = np.angle((np.roll(curve, -1) - c) / (curve - c))
    return float(increments.sum() / (2 * np.pi))


def main() -> None:
    rng = np.random.default_rng(240607656)

    # Exact polar description of exp(pi i D), checked at random points.
    radii = np.sqrt(rng.random(20_000))
    angles = rng.uniform(0, 2 * np.pi, 20_000)
    z = radii * np.exp(1j * angles)
    w = phi(z)
    theta = np.angle(w)
    recovered = theta / np.pi - 1j * np.log(np.abs(w)) / np.pi
    assert np.max(np.abs(recovered - z)) < 5e-13
    assert np.max(theta**2 + np.log(np.abs(w)) ** 2) < np.pi**2

    # The two boundary arcs agree only at the kissing point -1.
    theta_grid = np.linspace(-np.pi, np.pi, 4001)
    root = np.sqrt(np.maximum(0.0, np.pi**2 - theta_grid**2))
    inner = np.exp(-root + 1j * theta_grid)
    outer = np.exp(root + 1j * theta_grid)
    assert abs(inner[0] + 1) < 1e-14 and abs(inner[-1] + 1) < 1e-14
    assert abs(outer[0] + 1) < 1e-14 and abs(outer[-1] + 1) < 1e-14
    assert np.min(np.abs(outer[1:-1]) - np.abs(inner[1:-1])) > 0

    # Argument-principle check: several interior values have winding one.
    t = np.linspace(0, 2 * np.pi, 200_001, endpoint=False)
    boundary = phi(np.exp(1j * t))
    test_z = np.array([0, 0.2, -0.35j, 0.45 + 0.3j, -0.6 + 0.1j])
    values = [winding(boundary, phi(zz)) for zz in test_z]
    assert max(abs(v - 1.0) for v in values) < 2e-10

    # Phase-transition witnesses for rho > pi: one and two preimages.
    for rho in (1.01 * np.pi, 1.4 * np.pi, 2.5 * np.pi, 10 * np.pi):
        period = 2 * np.pi / rho
        z_pair = np.array([-0.5j * period, 0.5j * period])
        assert np.all(np.abs(z_pair) < 1)
        assert abs(np.exp(rho * z_pair[0]) - np.exp(rho * z_pair[1])) < 1e-12

        # Move perpendicular to the period and sufficiently near the circle.
        r = np.sqrt(max(0.0, 1 - 0.25 * period**2))
        z_single = min(0.999999, r + 0.25 * (1 - r))
        shifts = z_single + 1j * period * np.arange(-100, 101)
        assert np.count_nonzero(np.abs(shifts) < 1) == 1

    out = Path(__file__).resolve().parents[1] / "figures" / "exponential_moon.png"
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.5),
                             gridspec_kw={"width_ratios": [1.45, 1]})
    for ax in axes:
        ax.fill(outer.real, outer.imag, color="#b9d9f4", alpha=0.85)
        ax.fill(inner.real, inner.imag, color="white")
        ax.plot(outer.real, outer.imag, color="#174a7e", lw=2)
        ax.plot(inner.real, inner.imag, color="#b2452d", lw=2)
        ax.scatter([-1], [0], color="black", s=28, zorder=5)
        ax.set_aspect("equal")
        ax.grid(alpha=0.18)
        ax.set_xlabel(r"$\operatorname{Re} w$")
    axes[0].set_xlim(-5.2, 25.5)
    axes[0].set_ylim(-13, 13)
    axes[0].set_ylabel(r"$\operatorname{Im} w$")
    axes[0].set_title(r"Full image $\exp(\pi i\,\mathrm{D})$")
    axes[1].set_xlim(-1.18, 1.18)
    axes[1].set_ylim(-1.18, 1.18)
    axes[1].set_title("Inner hole and contact")
    axes[1].annotate("kissing point  $-1$", (-1, 0), xytext=(-0.75, 0.45),
                     arrowprops={"arrowstyle": "->", "lw": 1})
    fig.tight_layout()
    fig.savefig(out, dpi=220)
    print("polar reconstruction max error:", np.max(np.abs(recovered - z)))
    print("sample windings:", values)
    print("wrote", out)


if __name__ == "__main__":
    main()
