"""Independent QA for the analytic formulas in the proof packet."""

import math

import mpmath as mp
import sympy as sp


mp.mp.dps = 60


def fourier_coefficient(xi: mp.mpf, k: int) -> mp.mpf:
    return ((-1) ** k * 2 ** (1 - xi) * mp.gamma(xi + 1) /
            (mp.gamma(xi / 2 - k + 1) * mp.gamma(xi / 2 + k + 1)))


def check_symbolic_expansions() -> None:
    z = sp.symbols("z")
    g = sp.series(2 * sp.log(sp.cos(z)), z, 0, 8)
    assert sp.expand(g.removeO()).coeff(z, 2) == -1
    assert sp.expand(g.removeO()).coeff(z, 4) == -sp.Rational(1, 6)

    a = sp.symbols("a", positive=True)
    s_base = sp.Rational(2, 3) + sp.Rational(1, 3) * sp.cos(sp.sqrt(6 * a))
    s_log = sp.series(sp.log(s_base), a, 0, 5)
    assert sp.expand(s_log.removeO()).coeff(a, 1) == -1
    assert sp.expand(s_log.removeO()).coeff(a, 2) == 0
    assert sp.expand(s_log.removeO()).coeff(a, 3) == sp.Rational(1, 15)


def check_fourier_formula() -> None:
    for xi in map(mp.mpf, ("0.25", "0.5", "1", "1.5", "3", "4.5")):
        for k in range(1, 6):
            exact = (2 / mp.pi) * mp.quad(
                lambda x: mp.sin(x) ** xi * mp.cos(2 * k * x), [0, mp.pi]
            )
            formula = fourier_coefficient(xi, k)
            assert mp.almosteq(exact, formula, rel_eps=mp.mpf("1e-45"),
                               abs_eps=mp.mpf("1e-45"))


def check_coefficient_tail() -> None:
    for xi in map(mp.mpf, ("0.25", "0.5", "1", "1.5", "3", "4.5")):
        constant = abs(2 ** (1 - xi) * mp.gamma(xi + 1) *
                       mp.sin(mp.pi * xi / 2) / mp.pi)
        for k in (1000, 10000):
            # Reflection form avoids gamma poles/sign loss at large k.
            ak = constant * mp.gamma(k - xi / 2) / mp.gamma(k + xi / 2 + 1)
            ratio = ak * k ** (xi + 1) / constant
            assert abs(ratio - 1) < mp.mpf("0.01")


def check_fixed_mode_constants() -> None:
    t = mp.mpf("0.5")
    heat = mp.exp(-4 * t)
    target_g = -(mp.mpf(8) / 3) * t ** 2 * heat
    target_s = (mp.mpf(64) / 15) * t ** 3 * heat
    for n in (10000, 100000):
        g = mp.cos(2 * mp.sqrt(t / n)) ** (2 * n)
        s = (mp.mpf(2) / 3 + mp.cos(2 * mp.sqrt(6 * t / n)) / 3) ** n
        assert abs(n * (g - heat) / target_g - 1) < mp.mpf("0.001")
        assert abs(n ** 2 * (s - heat) / target_s - 1) < mp.mpf("0.001")


def check_first_revivals() -> None:
    for t in map(mp.mpf, ("0.1", "0.5", "2")):
        for n in (100, 1000, 10000):
            kg = int(mp.nint(mp.pi * mp.sqrt(n) / (2 * mp.sqrt(t))))
            ks = int(mp.nint(mp.pi * mp.sqrt(n) / mp.sqrt(6 * t)))
            mg = mp.cos(2 * kg * mp.sqrt(t / n)) ** (2 * n)
            ms = (mp.mpf(2) / 3 +
                  mp.cos(2 * ks * mp.sqrt(6 * t / n)) / 3) ** n
            # The proof only needs a positive bound depending on t.
            assert mg > mp.exp(-4 * t - 1)
            assert ms > mp.exp(-4 * t - 1)


if __name__ == "__main__":
    check_symbolic_expansions()
    check_fourier_formula()
    check_coefficient_tail()
    check_fixed_mode_constants()
    check_first_revivals()
    print("all symbolic identities and numerical asymptotic checks passed")
