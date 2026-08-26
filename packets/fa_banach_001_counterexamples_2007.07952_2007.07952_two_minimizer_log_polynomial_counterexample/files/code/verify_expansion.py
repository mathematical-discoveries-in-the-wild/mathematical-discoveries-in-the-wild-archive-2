"""Sanity checks for the two-minimizer counterexample (not proof)."""

from __future__ import annotations

import argparse
import math

import numpy as np
import sympy as sp


def symbolic_coefficient() -> None:
    alpha, lam, kappa, epsilon, cosine = sp.symbols(
        "alpha lam kappa epsilon cosine", positive=True
    )
    logs = 2 * alpha * epsilon + kappa * epsilon**2
    scale = sp.exp(logs).series(epsilon, 0, 3).removeO()
    plus = ((1 + epsilon) ** alpha).series(epsilon, 0, 3).removeO()
    minus = ((1 - epsilon) ** alpha).series(epsilon, 0, 3).removeO()
    aa = ((1 - lam) * plus + lam * scale * minus).series(epsilon, 0, 3).removeO()
    bb = ((1 - lam) * minus + lam * scale * plus).series(epsilon, 0, 3).removeO()
    A = ((aa ** (1 / alpha) + bb ** (1 / alpha)) / 2).series(epsilon, 0, 3).removeO()
    B = ((aa ** (1 / alpha) - bb ** (1 / alpha)) / 2).series(epsilon, 0, 3).removeO()
    integrand = ((A + B * cosine) ** (-2 * alpha)).series(epsilon, 0, 3).removeO().expand()
    average = integrand.subs(cosine, 0) + integrand.coeff(cosine, 2) / 2
    log_volume = sp.log(average).series(epsilon, 0, 3).removeO()
    Q = (2 * lam * logs + log_volume - log_volume.subs(lam, 0)).expand()
    log_difference = sp.factor(Q.coeff(epsilon, 2))
    expected = 2 * alpha * (1 - 6 * alpha) * lam * (1 - lam)
    print("symbolic coefficient:", log_difference)
    assert sp.simplify(log_difference - expected) == 0


def numeric_profile(degree: int, epsilon: float, samples: int, kappa: float = 1.0) -> None:
    alpha = 1 / degree
    scale = ((1 + epsilon) / (1 - epsilon)) ** alpha * math.exp(kappa * epsilon**2)
    delta = 2 * math.log(scale)
    theta = np.linspace(0, 2 * math.pi, samples, endpoint=False)
    cosine = np.cos(degree * theta)

    def value(lam: float) -> float:
        endpoint_plus = (1 + epsilon) ** alpha
        endpoint_minus = scale * (1 - epsilon) ** alpha
        a = (1 - lam) * endpoint_plus + lam * endpoint_minus
        endpoint_plus_2 = (1 - epsilon) ** alpha
        endpoint_minus_2 = scale * (1 + epsilon) ** alpha
        b = (1 - lam) * endpoint_plus_2 + lam * endpoint_minus_2
        A = (a**degree + b**degree) / 2
        B = (a**degree - b**degree) / 2
        volume = math.pi * float(np.mean((A + B * cosine) ** (-2 / degree)))
        return lam * delta + math.log(volume)

    vals = np.array([value(lam) for lam in np.linspace(0, 1, 101)])
    endpoint_error = abs(vals[-1] - vals[0])
    interior_gap = float(np.min(vals[1:-1] - vals[0]))
    midpoint_scaled = (value(0.5) - value(0.0)) / (epsilon**2 / 4)
    prediction = 2 / degree * (1 - 6 / degree)
    print(
        f"d={degree} eps={epsilon:.5g} endpoint_error={endpoint_error:.3e} "
        f"interior_gap={interior_gap:.3e} midpoint_scaled={midpoint_scaled:.8g} "
        f"prediction={prediction:.8g}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=400_000)
    args = parser.parse_args()
    symbolic_coefficient()
    for degree in (8, 10, 12):
        for epsilon in (0.08, 0.04, 0.02):
            numeric_profile(degree, epsilon, args.samples)


if __name__ == "__main__":
    main()
