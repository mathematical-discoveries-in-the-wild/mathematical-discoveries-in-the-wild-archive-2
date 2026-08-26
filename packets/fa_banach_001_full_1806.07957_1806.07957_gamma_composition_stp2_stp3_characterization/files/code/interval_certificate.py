"""Interval certificate for the explicit negative 3x3 minor.

Uses the positive power series for the regularized lower incomplete gamma
function and mpmath's outward-rounded interval arithmetic.
"""

import mpmath as mp

mp.mp.dps = 120
mp.iv.dps = 80


def lower_gamma_ratio_mp(s, x):
    return mp.gammainc(s, 0, x) / mp.gamma(s)


def inverse_lower_gamma_ratio(s, p):
    center = mp.gammaincinv(s, p) if hasattr(mp, "gammaincinv") else None
    if center is None:
        # Wide monotone bisection in log(x).
        lo = (mp.log(p) + mp.loggamma(s + 1)) / s - 100
        hi = max(mp.mpf(100), lo + 200)
        for _ in range(500):
            mid = (lo + hi) / 2
            if lower_gamma_ratio_mp(s, mp.exp(mid)) < p:
                lo = mid
            else:
                hi = mid
        center = mp.exp((lo + hi) / 2)
    return center


def lower_gamma_ratio_iv(s_text, x_text):
    """Certified enclosure of P(s,x), using a positive series."""
    s = mp.iv.mpf([s_text, s_text])
    x = mp.iv.mpf([x_text, x_text])
    term = mp.iv.mpf(1)
    total = mp.iv.mpf(1)
    term_point = mp.mpf(1)
    total_point = mp.mpf(1)
    s_point = mp.mpf(s_text)
    x_point = mp.mpf(x_text)
    n = 0
    while True:
        n += 1
        term *= x / (s + n)
        total += term
        term_point *= x_point / (s_point + n)
        total_point += term_point
        # From this point on, all successive ratios are at most rho.
        rho = x_point / (s_point + n + 1)
        next_point = term_point * rho
        if (
            n > 20
            and rho < mp.mpf("0.5")
            and next_point / (1 - rho) < total_point * mp.mpf("1e-72")
        ):
            next_term = term * x / (s + n + 1)
            # Successive ratios decrease and the present one is < 1/2,
            # so the full remaining tail is bounded by 2*next_term.
            tail = 2 * next_term
            total += mp.iv.mpf([0, 1]) * tail
            break
        if n > 10000:
            raise RuntimeError("series did not enter a geometric tail")
    prefactor = (x**s) * mp.iv.exp(-x) / mp.iv.gamma(s + 1)
    return prefactor * total


def endpoints(interval):
    lo_raw, hi_raw = interval._mpi_
    return mp.mpf(lo_raw), mp.mpf(hi_raw)


def certified_kernel(c, u, v):
    p = 1 - v
    root = inverse_lower_gamma_ratio(u, p)
    relative_width = mp.mpf("1e-35")
    x_lo = root * (1 - relative_width)
    x_hi = root * (1 + relative_width)
    p_lo = lower_gamma_ratio_iv(mp.nstr(u, 120), mp.nstr(x_lo, 120))
    p_hi = lower_gamma_ratio_iv(mp.nstr(u, 120), mp.nstr(x_hi, 120))
    p_lo_bounds = endpoints(p_lo)
    p_hi_bounds = endpoints(p_hi)
    if not (p_lo_bounds[1] < p and p_hi_bounds[0] > p):
        print("bracket diagnostic", p, p_lo_bounds, p_hi_bounds, root)
    assert p_lo_bounds[1] < p
    assert p_hi_bounds[0] > p

    shifted_lo = lower_gamma_ratio_iv(mp.nstr(u + c, 120), mp.nstr(x_lo, 120))
    shifted_hi = lower_gamma_ratio_iv(mp.nstr(u + c, 120), mp.nstr(x_hi, 120))
    # C = 1-P(u+c,x), and P is increasing in x.
    lower = 1 - endpoints(shifted_hi)[1]
    upper = 1 - endpoints(shifted_lo)[0]
    assert lower < upper
    return lower, upper, x_lo, x_hi


def determinant_3_by_3(m):
    positive = ((0, 0, 1, 1, 2, 2), (0, 1, 1, 2, 2, 0), (0, 2, 1, 0, 2, 1))
    negative = ((0, 2, 1, 1, 2, 0), (0, 1, 1, 0, 2, 2), (0, 0, 1, 2, 2, 1))

    def product(index_tuple):
        result = mp.iv.mpf(1)
        for k in range(0, 6, 2):
            lo, hi = m[index_tuple[k]][index_tuple[k + 1]]
            entry = mp.iv.mpf([mp.nstr(lo, 100), mp.nstr(hi, 100)])
            result *= entry
        return result

    result = mp.iv.mpf(0)
    for term in positive:
        result += product(term)
    for term in negative:
        result -= product(term)
    return endpoints(result)


if __name__ == "__main__":
    c = mp.mpf(1) / 8
    us = [mp.mpf(100), mp.mpf(18) / 5, mp.mpf(6) / 25]
    vs = [mp.mpf(99) / 100, mp.mpf(63) / 100, mp.mpf(3) / 20]
    matrix = []
    for u in us:
        row = []
        for v in vs:
            lower, upper, x_lo, x_hi = certified_kernel(c, u, v)
            row.append((lower, upper))
            print("u,v", u, v)
            print("x interval", mp.nstr(x_lo, 30), mp.nstr(x_hi, 30))
            print("C interval", mp.nstr(lower, 30), mp.nstr(upper, 30))
        matrix.append(row)
    det = determinant_3_by_3(matrix)
    print("determinant interval", mp.nstr(det[0], 40), mp.nstr(det[1], 40))
    assert det[1] < 0
