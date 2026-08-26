"""Finite interval certificate for a real/complex unconditionality gap.

The mathematical explanation of both parts is in the solution packet.  This
script uses exact integers/rationals plus outward-rounded interval evaluations
of roots of unity.  The stored atoms are rounded dual LP certificates; their
tiny moment residuals are repaired analytically by a six-root DFT measure.
"""

from __future__ import annotations

import math
from fractions import Fraction

from mpmath import iv


FREQUENCIES = (0, 1, 2, 3, 5)
DENOMINATOR = 10**12

# (point index t, phase index p, numerator a) denotes the atom
# (a/10^12) exp(-2 pi i p/120) delta_{exp(2 pi i t/120)}.
CERTIFICATES = {
    "+----": [(60, 0, 341617504606), (89, 6, 24749261726), (89, 7, 266280701432), (108, 26, 72145282934), (109, 28, 402368897176), (11, 92, 402368897176), (12, 94, 72145282934), (31, 113, 266280701432), (31, 114, 24749261726)],
    "+---+": [(60, 0, 333333333333), (100, 20, 666666666667), (20, 100, 666666666667)],
    "+--+-": [(90, 15, 707106781187), (30, 105, 707106781187)],
    "+--++": [(45, 7, 60762459198), (46, 9, 401592342112), (46, 10, 29133245778), (98, 26, 1615730470), (98, 27, 382817816602), (22, 93, 382817816602), (22, 94, 1615730470), (74, 110, 29133245778), (74, 111, 401592342112), (75, 113, 60762459198)],
    "+-+--": [(60, 0, 1000000000000)],
    "+-+-+": [(24, 6, 145308505601), (72, 18, 615536707435), (48, 102, 615536707435), (96, 114, 145308505601)],
    "+-++-": [(60, 0, 364554730235), (8, 13, 225283543884), (85, 23, 150651222941), (86, 25, 166140320214), (86, 26, 219591257699), (34, 94, 219591257699), (34, 95, 166140320214), (35, 97, 150651222941), (112, 107, 225283543884)],
    "+-+++": [(0, 0, 333333333333), (80, 20, 666666666667), (40, 100, 666666666667)],
    "++---": [(105, 7, 60762459198), (106, 9, 401592342112), (106, 10, 29133245778), (38, 26, 1615730470), (38, 27, 382817816602), (82, 93, 382817816602), (82, 94, 1615730470), (14, 110, 29133245778), (14, 111, 401592342112), (15, 113, 60762459198)],
    "++--+": [(30, 15, 707106781187), (90, 105, 707106781187)],
    "++-+-": [(0, 0, 333333333333), (40, 20, 666666666667), (80, 100, 666666666667)],
    "++-++": [(0, 0, 341617504606), (29, 6, 24749261726), (29, 7, 266280701432), (48, 26, 72145282934), (49, 28, 402368897176), (71, 92, 402368897176), (72, 94, 72145282934), (91, 113, 266280701432), (91, 114, 24749261726)],
    "+++--": [(60, 0, 333333333333), (20, 20, 666666666667), (100, 100, 666666666667)],
    "+++-+": [(0, 0, 364554730235), (68, 13, 225283543884), (25, 23, 150651222941), (26, 25, 166140320214), (26, 26, 219591257699), (94, 94, 219591257699), (94, 95, 166140320214), (95, 97, 150651222941), (52, 107, 225283543884)],
    "++++-": [(84, 6, 145308505601), (12, 18, 615536707435), (108, 102, 615536707435), (36, 114, 145308505601)],
    "+++++": [(0, 0, 1000000000000)],
}


def interval_upper(x) -> float:
    """Safely turn an interval upper endpoint into a binary upper bound."""
    return math.nextafter(float(x.b), math.inf)


def verify_complex_witness() -> tuple[float, float]:
    # Coefficients of p(z), indexed from degree 0 through 5.
    coeff = ((19563, 0), (18666, 0), (-6125, -28872), (18692, 10604), (0, 0), (-5823, 9055))

    # Exact lower and upper integer bounds for the three nontrivial moduli.
    modulus_bounds = (
        ((-6125, -28872), 29514, 29515),
        ((18692, 10604), 21490, 21491),
        ((-5823, 9055), 10765, 10766),
    )
    for (a, b), lower, upper in modulus_bounds:
        square = a * a + b * b
        assert lower * lower <= square <= upper * upper

    l1_lower = Fraction(19563 + 18666 + 29514 + 21490 + 10765, 100000)
    derivative_upper = Fraction(18666 + 2 * 29515 + 3 * 21491 + 5 * 10766, 100000)
    assert l1_lower == Fraction(99998, 100000)
    assert derivative_upper < Fraction(49, 25)

    # Outward-rounded values at the 4096th roots of unity.
    iv.dps = 40
    grid_size = 4096
    grid_upper = 0.0
    for k in range(grid_size):
        t = 2 * iv.pi * k / grid_size
        re = iv.mpf(0)
        im = iv.mpf(0)
        for degree, (a, b) in enumerate(coeff):
            cosine = iv.cos(degree * t)
            sine = iv.sin(degree * t)
            re += (a * cosine - b * sine) / 100000
            im += (a * sine + b * cosine) / 100000
        grid_upper = max(grid_upper, interval_upper(abs(iv.mpc(re, im))))

    assert grid_upper < 0.52631
    # Nearest-grid-point distance is at most pi/4096.  Use pi<22/7.
    global_bound = Fraction(52631, 100000) + Fraction(49, 25) * Fraction(22, 7) / grid_size
    assert global_bound == Fraction(3378009, 6400000)
    assert global_bound < Fraction(66, 125)

    complex_lower = l1_lower / Fraction(66, 125)
    assert complex_lower == Fraction(49999, 26400)
    return grid_upper, float(complex_lower)


def verify_real_certificates() -> tuple[str, float]:
    iv.dps = 40
    worst_sign = ""
    worst_bound = 0.0
    for sign_string, atoms in CERTIFICATES.items():
        signs = tuple(1 if char == "+" else -1 for char in sign_string)
        mass = Fraction(sum(numerator for _, _, numerator in atoms), DENOMINATOR)
        residual_sum = iv.mpf(0)

        for frequency, target in zip(FREQUENCIES, signs):
            real = iv.mpf(0)
            imag = iv.mpf(0)
            for point_index, phase_index, numerator in atoms:
                angle = 2 * iv.pi * (frequency * point_index - phase_index) / 120
                weight = iv.mpf(numerator) / DENOMINATOR
                real += weight * iv.cos(angle)
                imag += weight * iv.sin(angle)
            residual_sum += abs(iv.mpc(real - target, imag))

        # A six-root DFT measure repairs the five moment residuals with total
        # variation at most their l1 sum.
        corrected_interval = (
            iv.mpf(mass.numerator) / mass.denominator + residual_sum
        )
        corrected_bound = interval_upper(corrected_interval)
        if corrected_bound > worst_bound:
            worst_sign = sign_string
            worst_bound = corrected_bound
        assert corrected_bound < 1.888

    assert set(CERTIFICATES) == {
        "+" + "".join(tail)
        for tail in __import__("itertools").product("+-", repeat=4)
    }
    return worst_sign, worst_bound


if __name__ == "__main__":
    grid_upper, complex_lower = verify_complex_witness()
    worst_sign, real_upper = verify_real_certificates()
    exact_gap = Fraction(49999, 26400) - Fraction(236, 125)
    assert exact_gap == Fraction(779, 132000)
    print(f"complex witness grid upper: {grid_upper:.15f}")
    print(f"certified complex constant lower bound: {complex_lower:.15f}")
    print(f"worst normalized real sign: {worst_sign}")
    print(f"worst corrected real certificate: {real_upper:.15f}")
    print("CERTIFIED: K_C > 49999/26400 > 1.89 > 1.888 > K_R")
    print("certified gap lower bound: 779/132000")
