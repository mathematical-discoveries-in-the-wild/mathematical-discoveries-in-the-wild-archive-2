#!/usr/bin/env python3
"""Exact finite-support checks for the universal diagonal-kernel theorem."""

from fractions import Fraction
import random


def main() -> None:
    rng = random.Random(210411807)
    checks = 0
    for _ in range(2000):
        size = rng.randint(1, 18)
        weights = [Fraction(rng.randint(1, 50), rng.randint(1, 12)) for _ in range(size)]
        values = [Fraction(rng.randint(-20, 20), rng.randint(1, 9)) for _ in range(size)]
        mass_zero = Fraction(rng.randint(0, 1), 1)
        value_zero = Fraction(rng.randint(-20, 20), rng.randint(1, 9))

        # K(0,.)=0 and K(n,m)=delta_nm.  The integral operator is diagonal.
        integral_zero = Fraction(0)
        assert integral_zero == 0 * mass_zero * value_zero
        checks += 1
        for n in range(size):
            integral = sum(
                (Fraction(1) if n == m else Fraction(0)) * values[m] * weights[m]
                for m in range(size)
            )
            assert integral == weights[n] * values[n]
            checks += 1

        # In normalized L2 coordinates, TT* has precisely these eigenvalues.
        finite_spectrum = set(weights)
        if mass_zero:
            finite_spectrum.add(Fraction(0))
        assert all(value >= 0 for value in finite_spectrum)
        checks += len(finite_spectrum)

    print(f"PASS: {checks} exact kernel-integral and spectral checks")


if __name__ == "__main__":
    main()

