"""Independent checks for the critical-damping sign correction."""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 70


def ml(alpha: mp.mpf, beta: mp.mpf, z: mp.mpf, terms: int = 400) -> mp.mpf:
    return mp.fsum(z**k / mp.gamma(alpha * k + beta) for k in range(terms))


def pml2(alpha: mp.mpf, beta: mp.mpf, z: mp.mpf, terms: int = 400) -> mp.mpf:
    return mp.fsum((k + 1) * z**k / mp.gamma(alpha * k + beta) for k in range(terms))


def main() -> None:
    alpha = mp.mpf(3) / 4
    beta = mp.mpf(2)
    z = -mp.mpf(3) / 10

    lhs = alpha * pml2(alpha, beta, z)
    corrected = ml(alpha, beta - 1, z) + (1 + alpha - beta) * ml(alpha, beta, z)
    printed = ml(alpha, beta - 1, z) - (1 + alpha - beta) * ml(alpha, beta, z)

    assert mp.almosteq(lhs, corrected)
    assert not mp.almosteq(lhs, printed)

    for k in range(13):
        lhs_coeff = alpha * (k + 1)
        corrected_coeff = alpha * k + beta - 1 + (1 + alpha - beta)
        printed_coeff = alpha * k + beta - 1 - (1 + alpha - beta)
        assert lhs_coeff == corrected_coeff
        if beta != alpha + 1:
            assert lhs_coeff != printed_coeff

    a = mp.mpf(13) / 10
    s = mp.mpf(11) / 5
    q = a / s**alpha
    partial = mp.fsum((k + 1) * (-q) ** k for k in range(700)) / s**beta
    closed = s ** (2 * alpha - beta) / (s**alpha + a) ** 2
    assert mp.almosteq(partial, closed)

    printed_velocity_factor = (2 - alpha) / alpha
    corrected_velocity_factor = (1 + (alpha - 1)) / alpha
    assert corrected_velocity_factor == 1
    assert printed_velocity_factor != 1

    print(f"alpha={mp.nstr(alpha, 12)} beta={mp.nstr(beta, 12)} z={mp.nstr(z, 12)}")
    print(f"alpha*E2              = {mp.nstr(lhs, 40)}")
    print(f"correct plus formula  = {mp.nstr(corrected, 40)}")
    print(f"printed minus formula = {mp.nstr(printed, 40)}")
    print(f"Laplace series check  = {mp.nstr(partial, 40)}")
    print(f"Laplace closed form   = {mp.nstr(closed, 40)}")
    print(f"printed velocity factor  = {mp.nstr(printed_velocity_factor, 20)}")
    print(f"corrected velocity factor = {mp.nstr(corrected_velocity_factor, 20)}")
    print("all checks passed")


if __name__ == "__main__":
    main()
