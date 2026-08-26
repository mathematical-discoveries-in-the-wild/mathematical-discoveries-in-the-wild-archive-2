#!/usr/bin/env python3
"""Numerical diagnostics for the affine-Wigner counterexample packet.

These checks do not replace the positive-definiteness proof. They test the
closed-form identities, finite Gram matrices, a conditional-negative-
definiteness matrix, and FFT approximations for 60 parameter triples.
"""

from __future__ import annotations

import itertools

import numpy as np


def h(u: np.ndarray) -> np.ndarray:
    """u/(2*sinh(u/2)), evaluated stably at the origin."""
    u = np.asarray(u, dtype=float)
    out = np.empty_like(u)
    small = np.abs(u) < 1.0e-5
    us = u[small]
    out[small] = 1.0 - us**2 / 24.0 + 7.0 * us**4 / 5760.0
    out[~small] = u[~small] / (2.0 * np.sinh(u[~small] / 2.0))
    return out


def q_cnd(u: np.ndarray) -> np.ndarray:
    """q(u)=u*coth(u/4)-4, evaluated stably at the origin."""
    u = np.asarray(u, dtype=float)
    out = np.empty_like(u)
    small = np.abs(u) < 1.0e-4
    us = u[small]
    out[small] = us**2 / 12.0 - us**4 / 2880.0
    out[~small] = u[~small] / np.tanh(u[~small] / 4.0) - 4.0
    return out


def f_sqrt(u: np.ndarray) -> np.ndarray:
    """sqrt(u*coth(u/4))-2 = sqrt(4+q(u))-2."""
    return np.sqrt(4.0 + q_cnd(u)) - 2.0


def normalized_kernel(u: np.ndarray, p: float, beta: float, a: float) -> np.ndarray:
    return h(u) ** (2.0 * p) * np.exp(-beta * np.sqrt(a) * f_sqrt(u))


def minimum_gram_eigenvalue(values, points: np.ndarray) -> float:
    differences = points[:, None] - points[None, :]
    gram = values(differences)
    return float(np.linalg.eigvalsh(gram).min())


def check_identities() -> None:
    points = np.linspace(-25.0, 25.0, 2001)
    lhs = 2.0 * np.sqrt(h(points)) * np.cosh(points / 4.0) - 2.0
    rhs = f_sqrt(points)
    error = float(np.max(np.abs(lhs - rhs)))
    assert error < 2.0e-12, error

    points = points[np.abs(points) > 1.0e-8]
    direct_q = points / np.tanh(points / 4.0) - 4.0
    error_q = float(np.max(np.abs(direct_q - q_cnd(points))))
    assert error_q < 2.0e-12, error_q
    print(f"identity max errors: f={error:.3e}, q={error_q:.3e}")


def check_gram_matrices() -> None:
    points = np.array([-8.0, -5.4, -3.0, -1.7, -0.4, 0.0, 0.8, 2.2, 4.1, 7.3])
    worst_pd = np.inf
    worst_parameters = None
    for p, beta, a in itertools.product(
        (0.1, 0.3, 1.0, 2.5), (0.2, 1.0, 3.0), (0.05, 0.3, 1.0, 5.0, 20.0)
    ):
        candidates = (
            lambda u, p=p: h(u) ** (2.0 * p),
            lambda u, beta=beta, a=a: np.exp(-beta * np.sqrt(a) * f_sqrt(u)),
            lambda u, p=p, beta=beta, a=a: normalized_kernel(u, p, beta, a),
        )
        for candidate in candidates:
            eig = minimum_gram_eigenvalue(candidate, points)
            if eig < worst_pd:
                worst_pd = eig
                worst_parameters = (p, beta, a)
    assert worst_pd > -2.0e-10, (worst_pd, worst_parameters)

    differences = points[:, None] - points[None, :]
    q_matrix = q_cnd(differences)
    projection = np.eye(len(points)) - np.ones((len(points), len(points))) / len(points)
    centered = projection @ q_matrix @ projection
    worst_cnd = float(np.linalg.eigvalsh(centered).max())
    assert worst_cnd < 2.0e-10, worst_cnd
    print(
        "matrix diagnostics: "
        f"minimum PD Gram eigenvalue={worst_pd:.3e}, "
        f"maximum centered CND eigenvalue={worst_cnd:.3e}"
    )


def check_fft_slices() -> None:
    # The large interval makes even the slow p=0.1 tail negligible at the
    # artificial endpoints; the FFT is only an independent finite diagnostic.
    half_width = 300.0
    sample_count = 2**17
    u = np.linspace(-half_width, half_width, sample_count, endpoint=False)
    du = 2.0 * half_width / sample_count

    worst_value = np.inf
    worst_imaginary = 0.0
    worst_parameters = None
    case_count = 0
    for p, beta, a in itertools.product(
        (0.1, 0.3, 1.0, 2.5), (0.2, 1.0, 3.0), (0.05, 0.3, 1.0, 5.0, 20.0)
    ):
        phi = normalized_kernel(u, p, beta, a)
        spectrum = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(phi))) * du
        minimum = float(spectrum.real.min())
        imaginary = float(np.max(np.abs(spectrum.imag)))
        if minimum < worst_value:
            worst_value = minimum
            worst_parameters = (p, beta, a)
        worst_imaginary = max(worst_imaginary, imaginary)
        case_count += 1

    assert case_count == 60
    assert worst_value > -5.0e-10, (worst_value, worst_parameters)
    assert worst_imaginary < 5.0e-10, worst_imaginary
    print(
        f"FFT diagnostics: {case_count} slices, minimum={worst_value:.3e} "
        f"at p,beta,a={worst_parameters}, max imaginary={worst_imaginary:.3e}"
    )


def main() -> None:
    check_identities()
    check_gram_matrices()
    check_fft_slices()
    print("all affine-Wigner counterexample diagnostics passed")


if __name__ == "__main__":
    main()
