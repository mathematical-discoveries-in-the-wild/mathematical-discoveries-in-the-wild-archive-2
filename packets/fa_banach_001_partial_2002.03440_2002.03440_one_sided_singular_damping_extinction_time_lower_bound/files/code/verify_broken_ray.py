#!/usr/bin/env python3
"""Finite sanity checks for the broken-ray geometry; not a proof."""

from fractions import Fraction


def choose_x0(T: Fraction) -> Fraction:
    upper = min(Fraction(1), Fraction(2) - T)
    for denominator in (3, 4, 5, 7, 11):
        x0 = upper / denominator
        if x0 != Fraction(1) - T:
            return x0
    raise AssertionError("failed to avoid the unique reflection-time value")


def ray(T: Fraction, x0: Fraction) -> tuple[Fraction, bool]:
    reflection_time = Fraction(1) - x0
    if T < reflection_time:
        return x0 + T, False
    if T > reflection_time:
        return Fraction(2) - x0 - T, True
    raise AssertionError("target time is exactly the reflection time")


checked = 0
for k in range(1, 400):
    T = Fraction(k, 200)
    x0 = choose_x0(T)
    x, reflected = ray(T, x0)
    assert 0 < x < 1
    assert T < 2 - x0

    # For a(x)=1/x and unit initial jump, the amplitude is x0/(x0+T)
    # before reflection and -x0*x after reflection.
    amplitude = -x0 * x if reflected else x0 / (x0 + T)
    assert amplitude != 0
    checked += 1

print(f"PASS: {checked} times in (0,2); all rays and critical amplitudes survive")
