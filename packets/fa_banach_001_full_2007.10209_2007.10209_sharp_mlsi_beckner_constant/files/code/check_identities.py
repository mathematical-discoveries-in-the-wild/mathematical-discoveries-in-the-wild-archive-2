"""Numerical smoke checks for the two integral identities and sharp example."""

import mpmath as mp


mp.mp.dps = 60


def log_kernel_integral(a, b, p):
    value = mp.quad(
        lambda s: s ** (p - 2) * mp.log((a + s) / (b + s)),
        [0, 1, mp.inf],
    )
    exact = mp.pi * (a ** (p - 1) - b ** (p - 1)) / (
        (p - 1) * mp.sin(mp.pi * (p - 1))
    )
    return value, exact


def shifted_entropy_integral(a, b, p):
    mean = (a + b) / 2

    def bregman(x, s):
        z = mean + s
        t = (x - mean) / z
        return z * ((1 + t) * mp.log1p(t) - t)

    value = mp.quad(
        lambda s: s ** (p - 2) * (bregman(a, s) + bregman(b, s)) / 2,
        [0, 1, mp.inf],
    )
    cp = mp.pi / (p * (p - 1) * mp.sin(mp.pi * (p - 1)))
    exact = cp * ((a**p + b**p) / 2 - mean**p)
    return value, exact


for p0 in (1.1, 1.37, 1.8):
    p = mp.mpf(str(p0))
    a, b = mp.mpf("2.3"), mp.mpf("0.4")
    lhs, rhs = log_kernel_integral(a, b, p)
    elhs, erhs = shifted_entropy_integral(a, b, p)
    # Infinite-tail quadrature converges slowly when p is close to 1; this is
    # only a smoke check, while the packet proves the identities analytically.
    assert mp.almosteq(lhs, rhs, rel_eps=mp.mpf("2e-5")), (p, lhs, rhs)
    assert mp.almosteq(elhs, erhs, rel_eps=mp.mpf("2e-5")), (p, elhs, erhs)
    print(
        f"p={float(p):.2f}: log-kernel relerr={float(abs(lhs-rhs)/rhs):.3e}; "
        f"entropy relerr={float(abs(elhs-erhs)/erhs):.3e}"
    )

print("all identity checks passed")
