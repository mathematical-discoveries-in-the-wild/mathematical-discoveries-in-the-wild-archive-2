"""High-precision sanity checks for the K_p+K_q classification packet."""

import mpmath as mp


mp.mp.dps = 80


def mittag_leffler(alpha, beta, x):
    """Evaluate E_{alpha,beta}(-x) from its defining series."""
    total = mp.mpf("0")
    for n in range(2000):
        term = (-x) ** n / mp.gamma(alpha * n + beta)
        updated = total + term
        if n > 12 and abs(term) < mp.mpf("1e-65") * max(1, abs(updated)):
            return updated
        total = updated
    raise RuntimeError("Mittag-Leffler series did not converge")


def density(alpha, beta, t):
    return t ** (beta - 1) * mittag_leffler(alpha, beta, t**alpha)


def close(a, b, tol=mp.mpf("1e-55")):
    return abs(a - b) <= tol * max(1, abs(a), abs(b))


def main():
    # r=1.5: beta=1.75 lies below phi(1.5)=1.79365; beta=1.8 lies above.
    below_15 = density(mp.mpf("1.5"), mp.mpf("1.75"), mp.mpf("5"))
    above_15 = density(mp.mpf("1.5"), mp.mpf("1.8"), mp.mpf("5"))
    assert below_15 < 0
    assert above_15 > 0

    # r=1.8: beta=2.4 lies below phi(1.8)=2.46779; beta=2.5 lies above.
    below_18 = density(mp.mpf("1.8"), mp.mpf("2.4"), mp.mpf("6"))
    above_18 = density(mp.mpf("1.8"), mp.mpf("2.5"), mp.mpf("6"))
    assert below_18 < 0
    assert above_18 > 0

    # Endpoint r=2, m=1, M=3: h(t)=1-cos(t).
    for t in map(mp.mpf, ["0.2", "1", "2", "5", "10"]):
        assert close(density(mp.mpf("2"), mp.mpf("3"), t), 1 - mp.cos(t))

    # A point below the r=2 threshold and a representative r>2 sign change.
    below_2 = density(mp.mpf("2"), mp.mpf("2.9"), mp.mpf("6"))
    gap_over_2 = density(mp.mpf("2.2"), mp.mpf("3.4"), mp.mpf("20"))
    assert below_2 < 0
    assert gap_over_2 < 0

    print("r=1.5 below/above:", mp.nstr(below_15, 14), mp.nstr(above_15, 14))
    print("r=1.8 below/above:", mp.nstr(below_18, 14), mp.nstr(above_18, 14))
    print("r=2 below threshold:", mp.nstr(below_2, 14))
    print("r=2.2 oscillatory sample:", mp.nstr(gap_over_2, 14))
    print("all classification sanity checks passed")


if __name__ == "__main__":
    main()
