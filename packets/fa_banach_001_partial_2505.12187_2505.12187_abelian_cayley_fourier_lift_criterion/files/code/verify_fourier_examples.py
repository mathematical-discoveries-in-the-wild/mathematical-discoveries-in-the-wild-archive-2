#!/usr/bin/env python3
"""Numerical regression checks for the abelian-Cayley Fourier formula.

This does not prove the theorem.  It checks the closed forms in the packet for
small hypercubes and complete graphs and samples the cubic-phase construction.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def cyclic_fourier_values(h: np.ndarray) -> np.ndarray:
    """Return a(k)=sum_s h(s) exp(-2 pi i k s/n)."""
    return np.fft.fft(h)


def cayley_constant(a: np.ndarray, lambdas: np.ndarray) -> float:
    """Compute max_{xi != 0} mean_eta |a(eta)-a(eta-xi)|^4/lambda^2."""
    values = []
    for xi in range(1, len(a)):
        m_xi = np.mean(np.abs(a - np.roll(a, xi)) ** 4)
        values.append(float(m_xi / lambdas[xi] ** 2))
    return max(values)


def complete_positive(n: int) -> float:
    h = np.full(n, 1.0 / math.sqrt(2 * (n - 1)), dtype=complex)
    h[0] = 0.0
    a = cyclic_fourier_values(h)
    lambdas = np.full(n, n / (n - 1), dtype=float)
    lambdas[0] = 0.0
    return cayley_constant(a, lambdas)


def complete_cubic_phase(p: int) -> float:
    h = np.zeros(p, dtype=complex)
    c = 1.0 / math.sqrt(2 * (p - 1))
    for s in range(1, p):
        h[s] = c * np.exp(2j * np.pi * ((s**3) % p) / p)
    assert np.max(np.abs(h[1:] - np.conj(h[:0:-1]))) < 1e-10
    a = cyclic_fourier_values(h)
    assert np.max(np.abs(a.imag)) < 1e-9
    lambdas = np.full(p, p / (p - 1), dtype=float)
    lambdas[0] = 0.0
    return cayley_constant(a.real, lambdas)


def hypercube_constant(d: int) -> float:
    group = list(itertools.product((0, 1), repeat=d))
    scale = 1.0 / math.sqrt(2 * d)
    a = np.array([scale * sum((-1) ** eta[j] for j in range(d)) for eta in group])
    ratios = []
    for xi in group[1:]:
        k = sum(xi)
        shifted = np.array(
            [
                scale * sum((-1) ** (eta[j] ^ xi[j]) for j in range(d))
                for eta in group
            ]
        )
        m_xi = np.mean((a - shifted) ** 4)
        ratios.append(m_xi / (2 * k / d) ** 2)
    return float(max(ratios))


def main() -> None:
    for n in (4, 7, 12, 25):
        value = complete_positive(n)
        assert abs(value - n / 2) < 1e-9
        print(f"complete positive n={n:2d}: {value:.12g} = n/2")

    for d in range(2, 9):
        value = hypercube_constant(d)
        predicted = 3 - 2 / d
        assert abs(value - predicted) < 1e-9
        print(f"hypercube d={d:2d}: {value:.12g} = 3-2/d")

    for p in (5, 7, 11, 17, 31, 61, 101):
        value = complete_cubic_phase(p)
        assert value < 256
        print(f"complete cubic phase p={p:3d}: {value:.12g} < 256")


if __name__ == "__main__":
    main()

