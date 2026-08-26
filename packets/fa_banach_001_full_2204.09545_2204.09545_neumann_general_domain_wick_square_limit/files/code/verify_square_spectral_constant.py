#!/usr/bin/env python3
"""Square-domain spectral sanity check for the coefficient 1/(8*pi).

For the unit square with Neumann boundary conditions, the nonzero eigenvalues
are pi^2(m^2+n^2), m,n>=0.  The spatial average of the stationary covariance
at unit noise amplitude is half the sum of 1/[mu(1-eps+eps*mu)].
"""

from __future__ import annotations

import math

import numpy as np


def covariance_average(epsilon: float, cutoff: int = 1800) -> float:
    indices = np.arange(cutoff + 1, dtype=np.float64)
    m2 = indices[:, None] ** 2
    n2 = indices[None, :] ** 2
    mu = math.pi**2 * (m2 + n2)
    mu[0, 0] = np.inf
    lamb = mu * (1.0 - epsilon + epsilon * mu)
    return float(0.5 * np.sum(1.0 / lamb))


def main() -> None:
    target = 1.0 / (8.0 * math.pi)
    print(f"target coefficient 1/(8*pi) = {target:.10f}")
    print("epsilon cutoff covariance/log ratio relative_error")
    samples: list[tuple[float, float]] = []
    for epsilon, cutoff in ((1e-2, 1200), (3e-3, 1400), (1e-3, 1600),
                            (3e-4, 1800), (1e-4, 1800), (3e-5, 1800),
                            (1e-5, 1800)):
        value = covariance_average(epsilon, cutoff)
        samples.append((epsilon, value))
        ratio = value / math.log(1.0 / epsilon)
        relative = abs(ratio - target) / target
        print(
            f"{epsilon:.0e} {cutoff:4d} {value:.9f} "
            f"{ratio:.9f} {relative:.6f}"
        )

    # A fit removes the finite part of the Green trace, which makes raw
    # value/log ratios converge slowly.  Use the four smallest epsilons.
    fit = samples[-4:]
    x = np.array([math.log(1.0 / epsilon) for epsilon, _ in fit])
    y = np.array([value for _, value in fit])
    slope = float(np.polyfit(x, y, deg=1)[0])
    relative = abs(slope - target) / target
    print(f"tail fitted slope = {slope:.10f}; relative_error = {relative:.6f}")
    assert relative < 0.03

    # Direct scalar check of the heat-kernel partial fraction identity.
    epsilon, mu = 0.037, 13.25
    a = 1.0 - epsilon
    lhs = 1.0 / (mu * (a + epsilon * mu))
    rhs = (1.0 / a) * (1.0 / mu - 1.0 / (mu + a / epsilon))
    assert math.isclose(lhs, rhs, rel_tol=1e-14, abs_tol=1e-14)
    print("partial-fraction identity [PASS]")


if __name__ == "__main__":
    main()
