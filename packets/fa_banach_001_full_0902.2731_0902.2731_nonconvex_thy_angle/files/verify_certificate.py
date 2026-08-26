#!/usr/bin/env python3
"""Exactly verify the monotonicity certificate for arXiv:0902.2731."""

from __future__ import annotations

from fractions import Fraction
import math
import time

import sympy as sp


x, z = sp.symbols("x z", nonnegative=True)


def stamp(message: str) -> None:
    print(f"[{time.monotonic():.1f}] {message}", flush=True)


def direction(t):
    return ((1 - t**2) / (1 + t**2), 2 * t / (1 + t**2))


def cos4(c, s):
    return c**4 - 6 * c**2 * s**2 + s**4


def unit_half_angle(t):
    denominator = 11 + 12 * t**2 + 130 * t**4 + 12 * t**6 + 11 * t**8
    common = 10 * (1 + t**2) ** 3
    return (sp.cancel(common * (1 - t**2) / denominator),
            sp.cancel(common * 2 * t / denominator))


def q2_common_fraction(nx, ny, denominator):
    """Evaluate q^2 on (nx,ny)/denominator using 2-homogeneity."""
    r2 = sp.expand(nx**2 + ny**2)
    quartic = sp.expand(11 * nx**4 + 14 * nx**2 * ny**2 + 11 * ny**4)
    return quartic**2 / (100 * r2**3 * denominator**2)


stamp("building rational unit directions")
ua = unit_half_angle(x)
y = sp.cancel((x + z) / (1 - x * z))
ub = tuple(sp.cancel(component.subs(x, y)) for component in unit_half_angle(x))


def common_numerators(sign):
    first = sp.together(ua[0] + sign * ub[0])
    second = sp.together(ua[1] + sign * ub[1])
    n1, d1 = sp.fraction(first)
    n2, d2 = sp.fraction(second)
    common_denominator = sp.lcm(sp.Poly(d1, x, z), sp.Poly(d2, x, z)).as_expr()
    n1 = sp.cancel(n1 * common_denominator / d1)
    n2 = sp.cancel(n2 * common_denominator / d2)
    p1 = sp.Poly(sp.expand(n1), x, z, domain=sp.QQ)
    p2 = sp.Poly(sp.expand(n2), x, z, domain=sp.QQ)
    pd = sp.Poly(sp.expand(common_denominator), x, z, domain=sp.QQ)
    common_factor = sp.gcd(sp.gcd(p1, p2), pd)
    stamp(f"vector gcd degree={common_factor.degree_list()}")
    return p1.exquo(common_factor), p2.exquo(common_factor), pd.exquo(common_factor)


def q2_polys(px, py, pd):
    r2 = px * px + py * py
    quartic = 11 * px**4 + 14 * px**2 * py**2 + 11 * py**4
    numerator = quartic**2
    denominator = 100 * r2**3 * pd**2
    common_factor = sp.gcd(numerator, denominator)
    stamp(f"Q gcd degree={common_factor.degree_list()}")
    return numerator.exquo(common_factor), denominator.exquo(common_factor)

stamp("building Thy cosine")
xp, yp, dp = common_numerators(1)
stamp(f"plus vector degrees={xp.degree_list()}/{yp.degree_list()}/{dp.degree_list()}")
xm, ym, dm = common_numerators(-1)
stamp(f"minus vector degrees={xm.degree_list()}/{ym.degree_list()}/{dm.degree_list()}")
np_, dp_ = q2_polys(xp, yp, dp)
nm_, dm_ = q2_polys(xm, ym, dm)
stamp(f"Q+ degrees={np_.degree_list()}/{dp_.degree_list()}")
stamp(f"Q- degrees={nm_.degree_list()}/{dm_.degree_list()}")
stamp("forming rational Thy cosine")
nC = np_ * dm_ - nm_ * dp_
dC = 4 * dp_ * dm_
common_factor = sp.gcd(nC, dC)
stamp(f"C gcd degree={common_factor.degree_list()}")
nC = nC.exquo(common_factor)
dC = dC.exquo(common_factor)
stamp(f"C degrees={nC.degree_list()}/{dC.degree_list()} terms={len(nC.terms())}/{len(dC.terms())}")

stamp("differentiating and normalizing by sin(delta)")
one_plus_z2_sq = sp.Poly((1 + z**2) ** 2, x, z, domain=sp.QQ)
z_poly = sp.Poly(z, x, z, domain=sp.QQ)
pR = -one_plus_z2_sq * (nC.diff(z) * dC - nC * dC.diff(z))
qR = 4 * z_poly * dC**2
stamp("cancelling normalized derivative gcd")
common_factor = sp.gcd(pR, qR)
stamp(f"R gcd degree={common_factor.degree_list()}")
pR = pR.exquo(common_factor)
qR = qR.exquo(common_factor)
stamp(
    f"R degrees={pR.degree_list()}/{qR.degree_list()} "
    f"terms={len(pR.terms())}/{len(qR.terms())}"
)

# Strip the visibly positive factor from the numerator and certify both the
# resulting numerator and the reduced denominator on [0,1]^2.
positive_factor = sp.Poly((1 + z**2) ** 4, x, z, domain=sp.QQ)
core = pR.exquo(positive_factor)
numerator_content, core = core.primitive()
denominator_content, denominator_core = qR.primitive()
assert numerator_content > 0
assert denominator_content > 0
stamp(
    f"primitive contents numerator={numerator_content} "
    f"denominator={denominator_content}"
)
assert core.degree_list() == (128, 104)
assert len(core.terms()) == 6773
assert denominator_core.degree_list() == (128, 112)
assert len(denominator_core.terms()) == 7289

def bernstein_extrema(poly):
    """Return exact extrema, their indices, and the nonpositive count."""
    n, m = poly.degree_list()
    power = [[0] * (m + 1) for _ in range(n + 1)]
    for (i, j), coefficient in poly.terms():
        assert coefficient.q == 1
        power[i][j] = int(coefficient)

    # Convert first in x, then in z.  If p(t)=sum_k a_k t^k has degree n,
    # then b_i=sum_{k<=i} a_k*C(i,k)/C(n,k) is its i-th Bernstein
    # coefficient.
    after_x = [[Fraction(0) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for k in range(i + 1):
            multiplier = Fraction(math.comb(i, k), math.comb(n, k))
            for j, coefficient in enumerate(power[k]):
                if coefficient:
                    after_x[i][j] += coefficient * multiplier

    minimum = maximum = None
    minimum_index = maximum_index = None
    nonpositive = 0
    for i in range(n + 1):
        for j in range(m + 1):
            coefficient = sum(
                (
                    after_x[i][ell]
                    * Fraction(math.comb(j, ell), math.comb(m, ell))
                    for ell in range(j + 1)
                ),
                Fraction(0),
            )
            if minimum is None or coefficient < minimum:
                minimum, minimum_index = coefficient, (i, j)
            if maximum is None or coefficient > maximum:
                maximum, maximum_index = coefficient, (i, j)
            if coefficient <= 0:
                nonpositive += 1
    return minimum, minimum_index, maximum, maximum_index, nonpositive


stamp("converting the numerator core to the tensor Bernstein basis")
nmin, nargmin, nmax, nargmax, nnonpositive = bernstein_extrema(core)
assert nnonpositive == 0
assert nmin == 12531744508246953
assert nargmin == (0, 0)

stamp("converting the denominator core to the tensor Bernstein basis")
dmin, dargmin, dmax, dargmax, dnonpositive = bernstein_extrema(denominator_core)
assert dnonpositive == 0
assert dmin == Fraction(1285453186679270785, 28)
assert dargmin == (1, 1)

stamp("CERTIFIED: all 13,545 numerator Bernstein coefficients are positive")
stamp(f"numerator minimum={nmin} at {nargmin}; maximum={nmax} at {nargmax}")
stamp("CERTIFIED: all 14,577 denominator Bernstein coefficients are positive")
stamp(f"denominator minimum={dmin} at {dargmin}; maximum={dmax} at {dargmax}")
