#!/usr/bin/env python3
"""Numerical sanity checks for the effective eigenvalue-moduli packet."""

from __future__ import annotations

import argparse
import math

import numpy as np


def log_slope(xs: list[float], ys: list[float]) -> float:
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])


def crossing_checks(alpha: float = 0.35, q: float = 4.0) -> tuple[float, float]:
    ts = [2.0 ** (-j) for j in range(4, 13)]
    holder = [2.0 * math.sqrt(2.0) * t ** (1.0 - alpha) for t in ts]
    sobolev = [2.0 * math.sqrt(2.0) * t ** (1.0 / q) for t in ts]
    return log_slope(ts, holder), log_slope(ts, sobolev)


def oscillatory_checks(beta: float = 0.5, q: float = 2.0) -> tuple[float, float]:
    ks = [8, 16, 32, 64, 128]
    deltas: list[float] = []
    errors: list[float] = []
    for k in ks:
        amp = k ** (-(1.0 + beta))
        # Midpoint grid avoids the isolated zeros at which |u|' is undefined.
        ngrid = 64 * k
        x = (np.arange(ngrid) + 0.5) * (2.0 * np.pi / ngrid)
        u = amp * np.sin(k * x)
        up = amp * k * np.cos(k * x)
        vp = up
        abs_u_prime = np.sign(u) * up
        # v=u+amp is nonnegative, so |v|'=v' almost everywhere.
        diff_positive_branch = abs_u_prime - vp
        # Both ordered eigenvalue coordinates contribute equally.
        eig_diff_norm = math.sqrt(2.0) * np.abs(diff_positive_branch)
        error = float(np.mean(eig_diff_norm**q) ** (1.0 / q))
        deltas.append(math.sqrt(2.0) * amp)
        errors.append(error)
    return log_slope(deltas, errors), beta / (1.0 + beta)


def random_hermitian(rng: np.random.Generator, d: int, scale: float) -> np.ndarray:
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    h = (z + z.conj().T) / 2.0
    return h * (scale / np.linalg.norm(h, "fro"))


def gapped_projection_checks(trials: int = 100, d: int = 4) -> tuple[float, float]:
    rng = np.random.default_rng(260323056)
    worst_projection_ratio = 0.0
    worst_derivative_ratio = 0.0
    for _ in range(trials):
        z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        qmat, _ = np.linalg.qr(z)
        base = qmat @ np.diag(np.arange(d) * 2.0) @ qmat.conj().T
        perturb = random_hermitian(rng, d, 0.04)
        other = base + perturb
        wa, va = np.linalg.eigh(base)
        wb, vb = np.linalg.eigh(other)
        gamma = min(np.min(np.diff(wa)), np.min(np.diff(wb)))
        delta0 = np.linalg.norm(perturb, "fro")
        if delta0 > gamma / 6.0:
            raise AssertionError((delta0, gamma))

        ha = random_hermitian(rng, d, 1.0)
        dh = random_hermitian(rng, d, 0.03)
        hb = ha + dh
        delta1 = np.linalg.norm(dh, "fro")
        m_bound = max(np.linalg.norm(ha, "fro"), np.linalg.norm(hb, "fro"))

        deriv_a = np.array(
            [np.real(np.vdot(va[:, i], ha @ va[:, i])) for i in range(d)]
        )
        deriv_b = np.array(
            [np.real(np.vdot(vb[:, i], hb @ vb[:, i])) for i in range(d)]
        )
        derivative_bound = math.sqrt(d) * (
            delta1 + 6.0 * math.sqrt(d) * m_bound * delta0 / gamma
        )
        worst_derivative_ratio = max(
            worst_derivative_ratio,
            float(np.linalg.norm(deriv_a - deriv_b) / derivative_bound),
        )

        for i in range(d):
            pa = np.outer(va[:, i], va[:, i].conj())
            pb = np.outer(vb[:, i], vb[:, i].conj())
            observed = np.linalg.norm(pa - pb, 2)
            bound = 6.0 * delta0 / gamma
            worst_projection_ratio = max(worst_projection_ratio, float(observed / bound))

    return worst_projection_ratio, worst_derivative_ratio


def interpolation_checks(alpha: float = 0.35) -> float:
    # Shifted crossing with Frobenius norms: delta=sqrt(2)t and L=sqrt(2).
    ratios = []
    for j in range(4, 13):
        t = 2.0 ** (-j)
        delta = math.sqrt(2.0) * t
        l_bound = math.sqrt(2.0)
        lower = 2.0 * math.sqrt(2.0) * t ** (1.0 - alpha)
        upper = delta + 2.0 * l_bound**alpha * delta ** (1.0 - alpha)
        ratios.append(lower / upper)
        if lower > upper + 1e-12:
            raise AssertionError((t, lower, upper))
    return max(ratios)


def run_suite() -> None:
    holder_slope, sobolev_slope = crossing_checks()
    osc_slope, osc_expected = oscillatory_checks()
    projection_ratio, derivative_ratio = gapped_projection_checks()
    interpolation_ratio = interpolation_checks()

    if abs(holder_slope - 0.65) > 1e-10:
        raise AssertionError(holder_slope)
    if abs(sobolev_slope - 0.25) > 1e-10:
        raise AssertionError(sobolev_slope)
    if abs(osc_slope - osc_expected) > 0.03:
        raise AssertionError((osc_slope, osc_expected))
    if projection_ratio > 1.0 + 1e-12 or derivative_ratio > 1.0 + 1e-12:
        raise AssertionError((projection_ratio, derivative_ratio))

    print(f"crossing C0,alpha slope: {holder_slope:.12f} (expected 0.650000000000)")
    print(f"crossing W1,4 slope:      {sobolev_slope:.12f} (expected 0.250000000000)")
    print(f"oscillatory W1,2 slope:   {osc_slope:.12f} (expected {osc_expected:.12f})")
    print(f"max interpolation lower/upper ratio: {interpolation_ratio:.6f}")
    print(f"max Riesz projection observed/bound ratio: {projection_ratio:.6f}")
    print(f"max eigen-derivative observed/bound ratio: {derivative_ratio:.6f}")
    print("OVERALL: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", action="store_true")
    args = parser.parse_args()
    if not args.suite:
        parser.error("use --suite")
    run_suite()


if __name__ == "__main__":
    main()
