#!/usr/bin/env python3
"""Numerical and exact checks for the Riesz--Feller sampling packet."""

from __future__ import annotations

import argparse
import math
import numpy as np


def sinc_unscaled(z: np.ndarray) -> np.ndarray:
    """sin(z)/z with the value 1 at zero."""
    return np.sinc(z / np.pi)


def boundary_f(x: np.ndarray) -> np.ndarray:
    return sinc_unscaled(x) ** 2


def shannon_sum(x: np.ndarray, n_cut: int, omega: float = 2.0) -> np.ndarray:
    a = np.pi / omega
    k = np.arange(-n_cut, n_cut + 1)
    samples = boundary_f(a * k)
    kernels = sinc_unscaled(omega * x[:, None] - np.pi * k[None, :])
    return kernels @ samples


def hilbert_l1_example(x: np.ndarray) -> np.ndarray:
    return 1.0 / x - np.sin(2.0 * x) / (2.0 * x**2)


def cumulative_trapezoid(values: np.ndarray, step: float) -> np.ndarray:
    out = np.zeros_like(values)
    out[1:] = np.cumsum((values[:-1] + values[1:]) * (0.5 * step))
    return out


def spacetime_direct_and_sampled(
    x: np.ndarray,
    t: float,
    alpha: float,
    n_cut: int,
    quadrature_points: int = 12001,
) -> tuple[np.ndarray, np.ndarray]:
    """One Hardy component in n=1, theta=1, Omega=R=2."""
    omega = 2.0
    a = np.pi / omega
    xi = np.linspace(-omega, 0.0, quadrature_points)
    multiplier = np.exp(-t * np.abs(xi) ** alpha)
    fhat = np.pi * (1.0 - np.abs(xi) / 2.0)
    phase = np.exp(1j * x[:, None] * xi[None, :])
    direct = np.trapz(multiplier[None, :] * fhat[None, :] * phase, xi, axis=1)
    direct /= 2.0 * np.pi

    k = np.arange(-n_cut, n_cut + 1)
    samples = boundary_f(a * k)
    sampled_values = []
    for x_value in x:
        shifted_phase = np.exp(
            1j * (x_value - a * k[:, None]) * xi[None, :]
        )
        kernels = a * np.trapz(
            multiplier[None, :] * shifted_phase, xi, axis=1
        ) / (2.0 * np.pi)
        sampled_values.append(kernels @ samples)
    sampled = np.asarray(sampled_values)
    return direct, sampled


def run_suite() -> None:
    failures: list[str] = []

    # Exact Parseval test for f=(sin x/x)^2 at spacing a=pi/2.
    a = np.pi / 2.0
    sample_square_sum = 4.0 / 3.0
    sample_parseval = a * sample_square_sum
    integral_exact = 2.0 * np.pi / 3.0
    parseval_error = abs(sample_parseval - integral_exact)
    print(f"Parseval exact error:                 {parseval_error:.3e}")
    if parseval_error > 1e-14:
        failures.append("Parseval constant")

    grid = np.linspace(-4.0, 4.0, 801)
    err_40 = float(np.max(np.abs(shannon_sum(grid, 40) - boundary_f(grid))))
    err_120 = float(np.max(np.abs(shannon_sum(grid, 120) - boundary_f(grid))))
    print(f"boundary Shannon max error N=40:     {err_40:.6e}")
    print(f"boundary Shannon max error N=120:    {err_120:.6e}")
    if not (err_120 < err_40 and err_120 < 2.0e-5):
        failures.append("boundary Shannon convergence")

    # The exact L1 obstruction has logarithmically divergent absolute mass.
    step = 0.002
    x_tail = np.arange(10.0, 1000.0 + step, step)
    h_tail = np.abs(hilbert_l1_example(x_tail))
    cumulative = cumulative_trapezoid(h_tail, step)
    i100 = int(round((100.0 - 10.0) / step))
    i1000 = len(x_tail) - 1
    l1_log_slope = (cumulative[i1000] - cumulative[i100]) / math.log(10.0)
    print(f"L1 Hilbert tail/log slope:            {l1_log_slope:.6f} (expected 1)")
    if abs(l1_log_slope - 1.0) > 0.01:
        failures.append("L1 Hilbert tail")

    # For g=(2/pi)Si, Hg grows as (2/pi)log x.
    x_log = np.arange(step, 1000.0 + step, step)
    integrand = (1.0 - np.cos(x_log)) / x_log
    hg = (2.0 / np.pi) * cumulative_trapezoid(integrand, step)
    j100 = int(round((100.0 - step) / step))
    j1000 = len(x_log) - 1
    linf_log_slope = (hg[j1000] - hg[j100]) / math.log(10.0)
    expected_log_slope = 2.0 / np.pi
    print(
        "Linf Hilbert log-growth slope:        "
        f"{linf_log_slope:.6f} (expected {expected_log_slope:.6f})"
    )
    if abs(linf_log_slope - expected_log_slope) > 0.01:
        failures.append("Linf Hilbert growth")

    # Propagate the same boundary samples through one Riesz--Feller Hardy
    # multiplier and compare with direct Fourier inversion.
    x_eval = np.linspace(-2.0, 2.0, 17)
    direct, sampled_40 = spacetime_direct_and_sampled(x_eval, 0.7, 0.8, 40)
    _, sampled_120 = spacetime_direct_and_sampled(x_eval, 0.7, 0.8, 120)
    space_err_40 = float(np.max(np.abs(direct - sampled_40)))
    space_err_120 = float(np.max(np.abs(direct - sampled_120)))
    print(f"spacetime sampling max error N=40:   {space_err_40:.6e}")
    print(f"spacetime sampling max error N=120:  {space_err_120:.6e}")
    if not (space_err_120 < space_err_40 and space_err_120 < 2.0e-5):
        failures.append("spacetime sampling convergence")

    # Check the uniform tail estimate at the boundary, where C_chi=1.
    n_cut = 40
    k_tail = np.concatenate(
        (np.arange(-200000, -n_cut), np.arange(n_cut + 1, 200001))
    )
    ell2_tail = float(np.linalg.norm(boundary_f(a * k_tail)))
    uniform_error = err_40
    ratio = uniform_error / ell2_tail
    print(f"uniform error / omitted ell2 tail:   {ratio:.6f} (proved <= 1)")
    if ratio > 1.00001:
        failures.append("uniform tail bound")

    if failures:
        print("OVERALL: FAIL")
        for failure in failures:
            print(f" - {failure}")
        raise SystemExit(1)
    print("OVERALL: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", action="store_true", help="run all checks")
    args = parser.parse_args()
    if not args.suite:
        parser.error("pass --suite")
    run_suite()


if __name__ == "__main__":
    main()
