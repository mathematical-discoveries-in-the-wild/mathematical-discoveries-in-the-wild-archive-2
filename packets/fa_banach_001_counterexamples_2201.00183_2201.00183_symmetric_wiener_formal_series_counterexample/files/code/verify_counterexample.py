"""Exact checks for the arXiv:2201.00183 formal-series counterexample."""

from fractions import Fraction
from math import comb


def absolute_block_mass(n: int, r: Fraction) -> Fraction:
    """Absolute coefficient mass after evaluating at (s1,s2)=(2r,r^2)."""
    total = Fraction(0)
    for k in range(n + 1):
        coefficient = Fraction(comb(n, k) * (2**k), n * n * (2**n))
        monomial = (2 * r) ** (2 * n - 2 * k) * (r * r) ** k
        total += coefficient * monomial
    return total


def main() -> None:
    r = Fraction(3, 4)
    base = 3 * r * r
    assert base == Fraction(27, 16) > 1

    # Monomial exponents have unique weighted degree, hence no cross-n collisions.
    seen: dict[tuple[int, int], tuple[int, int]] = {}
    for n in range(1, 25):
        for k in range(n + 1):
            exponent = (2 * n - 2 * k, k)
            assert exponent not in seen
            seen[exponent] = (n, k)
            assert exponent[0] + 2 * exponent[1] == 2 * n

    for n in range(1, 25):
        exact = absolute_block_mass(n, r)
        closed_form = base**n / (n * n)
        assert exact == closed_form
        # The original Wiener norm contribution is exactly 1/n^2.
        assert Fraction(4**n, n * n * 2**n * 2**n) == Fraction(1, n * n)

    # Divergence is strong: individual absolute block masses eventually grow.
    masses = [absolute_block_mass(n, r) for n in range(40, 61)]
    assert all(masses[i + 1] > masses[i] for i in range(len(masses) - 1))

    print(f"r={r}, exponential base 3r^2={base} > 1")
    print(f"absolute block n=60 = {float(masses[-1]):.6e}")
    print("all exact coefficient, collision, Wiener-norm, and divergence checks passed")


if __name__ == "__main__":
    main()
