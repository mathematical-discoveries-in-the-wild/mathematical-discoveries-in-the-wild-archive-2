"""Finite-Fourier sanity check for the two-branch counterexample.

This script is not part of the proof.  It samples trigonometric polynomials,
composes them with the explicit piecewise-linear lift, and compares truncated
critical weighted Fourier norms.
"""

from __future__ import annotations

import numpy as np


def phi(x: np.ndarray) -> np.ndarray:
    return np.where(x <= 1.0 / 3.0, 2.0 * x, (x + 1.0) / 2.0)


def psi(y: np.ndarray) -> np.ndarray:
    return np.where(y <= 2.0 / 3.0, y / 2.0, 2.0 * y - 1.0)


def weighted_norm(coefficients: np.ndarray, frequencies: np.ndarray, p: float) -> float:
    weights = np.maximum(1, np.abs(frequencies))
    return float(np.sum((weights * np.abs(coefficients)) ** p) ** (1.0 / p))


def run() -> None:
    rng = np.random.default_rng(180306083)
    sample_count = 65536
    x = np.arange(sample_count) / sample_count

    round_trip = np.max(np.abs(psi(phi(x)) - x))
    print(f"grid round-trip error: {round_trip:.3e}")

    for p in (1.25, 1.5, 3.0, 5.0):
        print(f"p={p}")
        for cutoff in (16, 32, 64, 128):
            frequencies = np.arange(-cutoff, cutoff + 1)
            weights = np.maximum(1, np.abs(frequencies))
            ratios = []
            for _ in range(8):
                coefficients = (
                    rng.normal(size=frequencies.size)
                    + 1j * rng.normal(size=frequencies.size)
                ) / (1.0 + weights) ** 1.5
                values = np.exp(2j * np.pi * np.outer(phi(x), frequencies)) @ coefficients
                output = np.fft.fft(values) / sample_count
                output_frequencies = np.fft.fftfreq(sample_count, d=1.0 / sample_count).astype(int)
                ratios.append(
                    weighted_norm(output, output_frequencies, p)
                    / weighted_norm(coefficients, frequencies, p)
                )
            print(f"  cutoff={cutoff:3d} max sampled ratio={max(ratios):.4f}")


if __name__ == "__main__":
    run()

