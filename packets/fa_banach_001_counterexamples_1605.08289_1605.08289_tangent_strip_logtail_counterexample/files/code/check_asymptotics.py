"""Numerical sanity checks for the strip log-tail counterexample.

This is not part of the proof.  It checks the boundary asymptotic of the
p-th derivative for p=0,1,2,3 and the growth of the positive-arc contribution
to the outer Cauchy projection in one normalized tangent-disc geometry.
"""

import mpmath as mp
import sympy as sp


mp.mp.dps = 50

RADIUS = mp.mpf("0.5")
A = mp.mpf("0.5")
B = 1 / (2 * RADIUS)
WIDTH = B - A
KAPPA = mp.mpf("2")

w = sp.symbols("w")
aa = sp.Rational(1, 2)
bb = sp.Integer(1)
width = bb - aa
kappa = sp.Integer(2)
E = sp.exp(sp.pi * sp.I * (w - aa) / width)
chi = 1 / (1 - sp.I * E)
Lambda = sp.log(kappa - sp.I * w)


def boundary_w(t):
    return 1 / (1 - mp.e ** (1j * t))


def derivative_function(p):
    expr = w ** (-p) * chi / Lambda
    for _ in range(p):
        expr = w**2 * sp.diff(expr, w)
    return sp.lambdify(w, expr, "mpmath")


def kernel(rho, t):
    zeta = mp.e ** (1j * t)
    return zeta / (zeta - rho)


def main():
    print(f"normalized geometry: r={RADIUS}, strip=({A},{B})")
    for p in range(4):
        q = derivative_function(p)
        leading = (-1) ** p * mp.factorial(p)
        print(f"p={p}, expected leading coefficient={leading}")
        for t in (mp.mpf("0.08"), mp.mpf("0.04"), mp.mpf("0.02"), mp.mpf("0.01")):
            pos = q(boundary_w(t))
            ratio = pos * mp.log(1 / t) / leading
            neg = abs(q(boundary_w(-t)))
            print(
                "  t={}  positive_ratio={}  negative_abs={}".format(
                    mp.nstr(t, 4), mp.nstr(ratio, 10), mp.nstr(neg, 6)
                )
            )

        # Only the positive shrinking arc is integrated.  The proof shows
        # that all other arcs contribute a uniformly bounded quantity.
        epsilon = mp.mpf("0.08")
        for delta in (mp.mpf("1e-3"), mp.mpf("1e-5"), mp.mpf("1e-7")):
            rho = 1 - delta

            def integrand(t):
                return mp.im((q(boundary_w(t)) / leading) * kernel(rho, t)) / (2 * mp.pi)

            value = mp.quad(integrand, [4 * delta, mp.sqrt(delta), epsilon])
            model = -(
                mp.log(mp.log(1 / (4 * delta))) - mp.log(mp.log(1 / epsilon))
            ) / (2 * mp.pi)
            print(
                "  delta={}  positive_arc_im={}  loglog_model={}".format(
                    mp.nstr(delta, 3), mp.nstr(value, 9), mp.nstr(model, 9)
                )
            )


if __name__ == "__main__":
    main()
