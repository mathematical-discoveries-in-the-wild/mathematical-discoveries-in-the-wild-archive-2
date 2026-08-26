"""Numerical checks for the dyadic-shell Patterson--Sullivan construction.

This is verification only.  The z=0 L2 computation uses the exact Fourier
Gram matrix of the root-of-unity shell aliases, so it does not discretize the
boundary circle.
"""

from __future__ import annotations

import math


def radius(n: int) -> float:
    m = 2**n
    return (m - 1.0) / (m + 1.0)


def shell_gram(n: int, k: int) -> float:
    """L2 inner product of the zero-basepoint alias kernels E_n and E_k."""
    # r_n=(1-2^{-n})/(1+2^{-n}).  Evaluate (r_n r_k)^lcm
    # logarithmically so shells far beyond machine-resolution remain stable.
    an, ak = math.ldexp(1.0, -n), math.ldexp(1.0, -k)
    log_rn = math.log1p(-an) - math.log1p(an)
    log_rk = math.log1p(-ak) - math.log1p(ak)
    log_q = math.ldexp(log_rn + log_rk, max(n, k))
    q = math.exp(log_q)
    return 2.0 * q / (1.0 - q)


def zero_basepoint_l2(s: float, nmax: int = 700) -> float:
    """Exact truncated L2 error of the normalized boundary kernel at z=0."""
    t = 2.0 ** (1.0 - s)
    raw = [t**n for n in range(1, nmax + 1)]
    denom = sum(raw)
    weights = [a / denom for a in raw]
    square = 0.0
    for i, ai in enumerate(weights, start=1):
        square += ai * ai * shell_gram(i, i)
        for j in range(i + 1, nmax + 1):
            square += 2.0 * ai * weights[j - 1] * shell_gram(i, j)
    return math.sqrt(square)


def hyperbolic_distance(z: complex, x: complex) -> float:
    q = abs((x - z) / (1.0 - z.conjugate() * x))
    return math.log((1.0 + q) / (1.0 - q))


def poisson(z: complex, boundary: complex) -> float:
    return (1.0 - abs(z) ** 2) / abs(boundary - z) ** 2


def busemann_relative_error(z: complex, n: int, samples: int = 2048) -> float:
    m, r = 2**n, radius(n)
    worst = 0.0
    for j in range(samples):
        theta = 2.0 * math.pi * j / samples
        boundary = complex(math.cos(theta), math.sin(theta))
        ratio = math.exp(n * math.log(2.0) - hyperbolic_distance(z, r * boundary))
        target = poisson(z, boundary)
        worst = max(worst, abs(ratio / target - 1.0))
    return worst


def main() -> None:
    print("exact z=0 normalized L2 alias error")
    for s in (1.25, 1.125, 1.0625, 1.03125, 1.015625):
        err = zero_basepoint_l2(s)
        print(f"s={s:.6f}  error={err:.8f}  error/sqrt(s-1)={err/math.sqrt(s-1):.8f}")

    z = 0.47 + 0.31j
    print("\nuniform Busemann relative error for z=0.47+0.31i")
    for n in (4, 6, 8, 10, 12):
        err = busemann_relative_error(z, n)
        print(f"n={n:2d}  error={err:.8e}  2^n*error={2**n*err:.8f}")


if __name__ == "__main__":
    main()
