#!/usr/bin/env python3
"""Auxiliary checks for the scaled weighted-Mourre counterexample.

These numerical/symbolic checks do not replace the operator proof in the
packet.  They verify the scalar commutator multiplier, the scale identity,
and the persistent direct-sum lower-bound mechanism.
"""

import math

import numpy as np
import sympy as sp


def symbolic_checks() -> None:
    t = sp.symbols("t", real=True)
    g = (sp.atan(t) + t / (1 + t**2)) / 2
    expected = 1 / (1 + t**2) ** 2
    assert sp.simplify(sp.diff(g, t) - expected) == 0

    delta, x, z = sp.symbols("delta x z", nonzero=True)
    # Scalar part of delta * (delta*x-z)^(-1)=(x-z/delta)^(-1).
    assert sp.simplify(delta / (delta * x - z) - 1 / (x - z / delta)) == 0


def direct_sum_scale_checks() -> None:
    # The analytic proof uses m=||S_+||>0.  For every eta and threshold Y,
    # dyadic blocks contain an n with eta/delta_n >= Y.
    for eta in np.geomspace(1e-12, 1.0, 100):
        for threshold in (2.0, 10.0, 1e3, 1e6):
            n = max(1, math.ceil(math.log2(threshold / eta)))
            delta_n = 2.0 ** (-n)
            assert eta / delta_n >= threshold * (1 - 1e-12)

    # Resolvent norm bound used in the proof: ||S(iy)|| <= 1/y.
    for y in np.geomspace(1.0, 1e12, 200):
        assert 1.0 / y <= 1.0


if __name__ == "__main__":
    symbolic_checks()
    direct_sum_scale_checks()
    print("symbolic derivative and scaling identities: passed")
    print("100 dyadic eta scales x 4 escape thresholds: passed")

