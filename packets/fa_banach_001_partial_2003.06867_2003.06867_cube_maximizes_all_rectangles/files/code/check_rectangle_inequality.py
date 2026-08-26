"""Numerical sanity checks for the rectangular Brownian-exit theorem.

This script is not used in the proof.
"""

import random

import mpmath as mp


mp.mp.dps = 50
PI = mp.pi
LAMBDA0 = PI**2 / 8


def survival(t):
    """Spectral series for P_0(tau_(-1,1)>t), used away from t=0."""
    return mp.nsum(
        lambda n: (4 / PI)
        * ((-1) ** n)
        / (2 * n + 1)
        * mp.exp(-LAMBDA0 * (2 * n + 1) ** 2 * t),
        [0, mp.inf],
    )


def sech_product(s):
    return mp.nprod(
        lambda n: ((2 * n + 1) ** 2 * PI**2 / 8)
        / ((2 * n + 1) ** 2 * PI**2 / 8 + s),
        [0, mp.inf],
    )


def main():
    print("Laplace-product relative errors")
    for s in [mp.mpf("0.1"), 1, 3, 10]:
        exact = 1 / mp.cosh(mp.sqrt(2 * s))
        approx = sech_product(s)
        print(s, mp.nstr(abs(approx / exact - 1), 8))

    print("sample Jensen gaps S(mean(b)t)^d-product S(b_k t)")
    rng = random.Random(200306867)
    minimum_gap = mp.inf
    for _ in range(40):
        d = rng.randint(2, 7)
        b = [mp.e ** rng.uniform(-1.8, 1.8) for _ in range(d)]
        mean_b = sum(b) / d
        for t in [mp.mpf("0.08"), mp.mpf("0.2"), mp.mpf("0.7"), 2]:
            product = mp.fprod(survival(value * t) for value in b)
            gap = survival(mean_b * t) ** d - product
            minimum_gap = min(minimum_gap, gap)
            if gap < -mp.mpf("1e-35"):
                raise AssertionError((d, b, t, gap))
    print("minimum sampled gap:", mp.nstr(minimum_gap, 12))


if __name__ == "__main__":
    main()
