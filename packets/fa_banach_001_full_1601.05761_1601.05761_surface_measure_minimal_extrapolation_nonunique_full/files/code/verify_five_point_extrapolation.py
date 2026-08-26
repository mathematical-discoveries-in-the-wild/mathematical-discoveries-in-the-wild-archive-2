#!/usr/bin/env python3
"""Check the explicit five-point-per-circle extrapolation in Example 3.9."""

import cmath


def mu_hat(m1, m2):
    return (1 if m1 == 0 else 0) * (1 + (-1) ** m2)


def nu_hat(m1, m2, q=5):
    horizontal = sum(cmath.exp(-2j * cmath.pi * m1 * j / q) for j in range(q)) / q
    return horizontal * (1 + (-1) ** m2)


def main():
    worst = 0.0
    for m1 in range(-2, 3):
        for m2 in range(-10, 11):
            error = abs(mu_hat(m1, m2) - nu_hat(m1, m2))
            worst = max(worst, error)
            assert error < 1e-12
    print("checked m1=-2,...,2 and m2=-10,...,10")
    print("maximum Fourier mismatch:", worst)
    print("mass(mu)=mass(nu)=2, so both have total variation 2")
    print("all checks passed")


if __name__ == "__main__":
    main()
