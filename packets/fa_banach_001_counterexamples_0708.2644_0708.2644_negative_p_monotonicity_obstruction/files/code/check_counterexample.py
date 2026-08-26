#!/usr/bin/env python3
"""High-precision numerical QA for the negative-p counterexample packet.

The packet proof is analytic.  This script only checks the displayed moment
identity and one illustrative reversed pair.
"""

import mpmath as mp


mp.mp.dps = 80
ETA = mp.mpf("0.5")


def g(t: mp.mpf) -> mp.mpf:
    """The C^1 hazard-drop profile used in the proof."""
    if t <= 1:
        return mp.mpf("0")
    if t >= 2:
        return ETA
    u = t - 1
    return ETA * (3 * u**2 - 2 * u**3)


def normalized_moment(p: mp.mpf) -> mp.mpf:
    """Return Y_p/Gamma(p+1) from the exact integration identity."""
    integral = mp.quad(
        lambda t: g(t) * t ** (p - 1) * mp.exp(-t),
        [mp.mpf("1"), mp.mpf("2"), mp.inf],
    )
    return 1 - p * integral / mp.gamma(p + 1)


if __name__ == "__main__":
    p1 = mp.mpf("-0.99")
    p2 = mp.mpf("-0.5")
    for p in (p1, p2, mp.mpf("-0.1"), mp.mpf("-0.01")):
        print(f"p={mp.nstr(p, 8):>8}  M(p)={mp.nstr(normalized_moment(p), 60)}")
    assert normalized_moment(p1) < normalized_moment(p2)
    print("PASS: M(-0.99) < M(-0.5), reversing the conjectured inequality.")
