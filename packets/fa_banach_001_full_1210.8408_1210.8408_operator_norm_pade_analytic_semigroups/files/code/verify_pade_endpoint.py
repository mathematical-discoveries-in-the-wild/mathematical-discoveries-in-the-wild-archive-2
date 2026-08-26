"""Exact and numerical sanity checks for the Padé endpoint proof.

The exact checks mirror algebraic steps in the proof.  The sampled scalar
checks are regression tests only and are not substitutes for the proof.
"""

from fractions import Fraction
from math import factorial, log, pi

import mpmath as mp


mp.mp.dps = 70


def coefficients(n: int) -> tuple[list[Fraction], list[Fraction]]:
    p = [
        Fraction(
            factorial(2 * n + 1 - j) * factorial(n),
            factorial(2 * n + 1) * factorial(j) * factorial(n - j),
        )
        for j in range(n + 1)
    ]
    q = [
        Fraction(
            factorial(2 * n + 1 - j) * factorial(n + 1),
            factorial(2 * n + 1)
            * factorial(j)
            * factorial(n + 1 - j),
        )
        for j in range(n + 2)
    ]
    return p, q


def horner(values: list[Fraction], z: mp.mpc) -> mp.mpc:
    out = mp.mpc(0)
    for value in reversed(values):
        out = out * z + mp.mpf(value.numerator) / value.denominator
    return out


def r_minus(n: int, z: mp.mpc) -> mp.mpc:
    """Return r_n(-z)."""
    p, q = coefficients(n)
    return horner(p, -z) / horner(q, z)


def exact_checks() -> None:
    for n in range(1, 21):
        n_cap = n + 1
        p, q = coefficients(n)
        for j in range(n + 1):
            assert p[j] == Fraction(n_cap - j, n_cap) * q[j]

    for n in range(1, 201):
        n_cap = n + 1
        _, q = coefficients(n)
        for j in range(n_cap):
            assert q[j] / q[j + 1] <= 2 * n_cap * n_cap


def log_grid(lo: float, hi: float, count: int) -> list[mp.mpf]:
    step = mp.mpf(hi - lo) / (count - 1)
    return [mp.e ** (mp.mpf(lo) + k * step) for k in range(count)]


def sampled_checks() -> None:
    print("n  positive/max_bound  imaginary_tail/max_bound")
    for n in (1, 2, 5, 10, 20):
        n_cap = n + 1
        positive_ratio = mp.mpf(0)
        tail_ratio = mp.mpf(0)
        for radius in log_grid(-18.0, 18.0, 1201):
            positive_error = abs(r_minus(n, radius) - mp.e ** (-radius))
            positive_ratio = max(
                positive_ratio, positive_error * (2 * n_cap)
            )
            tail_ratio = max(
                tail_ratio,
                radius * abs(r_minus(n, 1j * radius))
                / (4 * n_cap * n_cap),
            )
        assert positive_ratio <= mp.mpf("1.000000000001")
        assert tail_ratio <= mp.mpf("1.000000000001")
        print(
            f"{n:2d} {mp.nstr(positive_ratio, 10):>19}"
            f" {mp.nstr(tail_ratio, 10):>26}"
        )

    print("\nstrict-sector logarithmic integrals (finite-window samples)")
    for theta in (0.4, 0.8, 1.2):
        delta = 1 - 2 * theta / pi
        print(f"theta={theta:.1f}, delta={delta:.6f}")
        previous = None
        for n in (2, 5, 10, 20):
            count = 1801
            lo, hi = mp.mpf(-20), mp.mpf(20)
            step = (hi - lo) / (count - 1)
            values = []
            phase = mp.e ** (1j * theta)
            for k in range(count):
                radius = mp.e ** (lo + k * step)
                z = radius * phase
                values.append(abs(r_minus(n, z) - mp.e ** (-z)))
            integral = step * (
                mp.fsum(values) - (values[0] + values[-1]) / 2
            )
            scaled = integral * (n + 1) ** delta / (1 + log(n + 1))
            assert mp.isfinite(integral)
            print(
                f"  n={n:2d} I~{mp.nstr(integral, 10):>12}"
                f" scaled={mp.nstr(scaled, 10):>12}"
            )
            previous = integral


def main() -> None:
    exact_checks()
    print("exact coefficient checks: PASS")
    sampled_checks()
    print("\nall checks: PASS")


if __name__ == "__main__":
    main()
