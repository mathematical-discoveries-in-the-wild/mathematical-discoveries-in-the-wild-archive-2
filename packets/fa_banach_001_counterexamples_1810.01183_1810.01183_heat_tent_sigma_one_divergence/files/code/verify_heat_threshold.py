#!/usr/bin/env python3
"""Numerical checks for the heat tent-space sigma=1 threshold."""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60


def truncated_factor(sigma: mp.mpf, lam: mp.mpf, eps: mp.mpf) -> mp.mpf:
    return mp.quad(lambda t: t ** (-sigma) * lam * mp.exp(-2 * lam * t), [eps, 1, mp.inf])


def main() -> None:
    lam = mp.mpf("1.7")
    for sigma in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.75")):
        exact = mp.power(2, sigma - 1) * mp.gamma(1 - sigma) * lam**sigma
        # Substitute t=u^(1/(1-sigma)) to remove the endpoint singularity.
        power = 1 / (1 - sigma)
        numeric = mp.quad(
            lambda u: lam / (1 - sigma) * mp.exp(-2 * lam * u**power),
            [0, 1, mp.inf],
        )
        rel = abs(numeric - exact) / exact
        assert rel < mp.mpf("1e-30")
        print(f"sigma={float(sigma):.2f}: exact relative error {float(rel):.3e}")

    epsilons = [mp.mpf(10) ** (-k) for k in (2, 4, 6, 8)]
    endpoint = [truncated_factor(mp.mpf(1), lam, eps) for eps in epsilons]
    assert all(endpoint[j + 1] > endpoint[j] for j in range(len(endpoint) - 1))
    # Decreasing epsilon by 10^2 adds asymptotically lambda*log(100).
    increments = [endpoint[j + 1] - endpoint[j] for j in range(len(endpoint) - 1)]
    target = lam * mp.log(100)
    assert abs(increments[-1] - target) / target < mp.mpf("1e-5")
    print("sigma=1 truncated values:", " ".join(f"{float(v):.8f}" for v in endpoint))

    supercritical = [truncated_factor(mp.mpf("1.5"), lam, eps) for eps in epsilons]
    assert all(supercritical[j + 1] > 5 * supercritical[j] for j in range(1, len(supercritical) - 1))
    print("sigma=1.5 truncated values:", " ".join(f"{float(v):.8f}" for v in supercritical))
    print("PASS")


if __name__ == "__main__":
    main()
