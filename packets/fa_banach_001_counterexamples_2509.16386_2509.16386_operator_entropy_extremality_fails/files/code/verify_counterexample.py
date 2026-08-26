#!/usr/bin/env python3
"""Symbolic/numerical audit of the operator-level Stokes counterexample."""

import mpmath as mp
import sympy as sp


def main() -> None:
    x = sp.symbols("x", real=True)
    epsilon = sp.Rational(1, 2)
    a = 1 + epsilon * (1 - sp.cos(2 * sp.pi * x)) / (2 * sp.pi * x)
    ax = sp.simplify(a * x)
    rho = sp.simplify(sp.diff(ax, x))

    assert sp.simplify(rho - (1 + epsilon * sp.sin(2 * sp.pi * x))) == 0
    assert sp.limit(a, x, 0, dir="+") == 1
    assert sp.simplify(a.subs(x, 1)) == 1
    assert sp.integrate(rho, (x, 0, 1)) == 1

    # The source entropy is integral rho*log(C/rho), with C=1+epsilon.
    mp.mp.dps = 50
    eps = mp.mpf("0.5")
    entropy = mp.quad(
        lambda t: (1 + eps * mp.sin(2 * mp.pi * t))
        * mp.log((1 + eps) / (1 + eps * mp.sin(2 * mp.pi * t))),
        [0, 1],
    )
    assert entropy > 0

    print("a(0) = a(1) = 1")
    print("D_epsilon(x) density:", rho)
    print("integral density:", sp.integrate(rho, (x, 0, 1)))
    print("S*(D_epsilon x,[0,1]) at epsilon=1/2:", mp.nstr(entropy, 18))
    print("S*(d x,[0,1]) = 0")
    print("all checks passed")


if __name__ == "__main__":
    main()
