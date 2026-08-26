#!/usr/bin/env python3
"""High-precision sanity checks for the gamma-product limit packet.

This script is not part of the proof.  It checks the exact finite-correction
identity numerically, the predicted first-order logarithmic error, and the
asymptotic of the recursive Bohnenblust--Hille upper estimates.
"""

import mpmath as mp


mp.mp.dps = 80
LOG2 = mp.log(2)
LOGPI = mp.log(mp.pi)
GAMMA = mp.euler
LIMIT_LOG = 1 - GAMMA / 2 - LOG2 / 2
LIMIT = mp.e**LIMIT_LOG
TRIGAMMA = mp.polygamma(1, mp.mpf(3) / 2)


def log_r_old(n: int) -> mp.mpf:
    assert n % 2 == 0 and n >= 4
    m = (n - 2) // 2
    product_log = mp.fsum(
        (2 * k + 1) * mp.loggamma(mp.mpf(3) / 2 - mp.mpf(1) / (2 * k + 1))
        for k in range(1, m + 1)
    )
    return (
        mp.mpf(n * n - 4) / (8 * n) * LOGPI
        - mp.mpf(n - 2) / 4 * LOG2
        - product_log / n
    )


def log_r_corrected(n: int) -> mp.mpf:
    assert n % 2 == 0 and n > 14
    m = (n - 2) // 2
    product_log = mp.fsum(
        (2 * k + 1) * mp.loggamma(mp.mpf(3) / 2 - mp.mpf(1) / (2 * k + 1))
        for k in range(7, m + 1)
    )
    exponent_two = mp.mpf(n * n - 2 * n - 192) / (4 * n)
    return (
        mp.mpf(n * n - 196) / (8 * n) * LOGPI
        - exponent_two * LOG2
        - product_log / n
    )


KAPPA = (
    48 * LOG2
    - 24 * LOGPI
    + mp.fsum(
        (2 * k + 1) * mp.loggamma(mp.mpf(3) / 2 - mp.mpf(1) / (2 * k + 1))
        for k in range(1, 7)
    )
)


def log_a_p(p: mp.mpf, p0: mp.mpf) -> mp.mpf:
    if p <= p0:
        return (mp.mpf(1) / 2 - 1 / p) * LOG2
    return LOG2 / 2 + mp.loggamma((p + 1) / 2) / p - LOGPI / (2 * p)


def recurrence_logs(max_n: int) -> list[mp.mpf]:
    p0 = mp.findroot(lambda p: mp.gamma((p + 1) / 2) - mp.sqrt(mp.pi) / 2, 1.85)
    logs = [mp.nan] * (max_n + 1)
    logs[2] = LOG2 / 2
    logs[3] = mp.mpf(5) * LOG2 / 6
    for n in range(4, max_n + 1):
        p = mp.mpf(2 * n - 4) / (n - 1)
        logs[n] = LOG2 / 2 + mp.mpf(n - 2) / n * (
            logs[n - 2] - 2 * log_a_p(p, p0)
        )
    return logs


def main() -> None:
    print("conjectured limit =", mp.nstr(LIMIT, 30))
    print("-psi_1(3/2)/4 =", mp.nstr(-TRIGAMMA / 4, 30))
    print("kappa =", mp.nstr(KAPPA, 30))
    print("\nfinite-correction and asymptotic checks")
    for n in (16, 30, 100, 1000, 10000):
        old = log_r_old(n)
        corrected = log_r_corrected(n)
        correction_residual = corrected - old - KAPPA / n
        scaled_error = n * (corrected - LIMIT_LOG) / mp.log(n)
        print(
            f"n={n:5d}",
            "r_n=", mp.nstr(mp.e**corrected, 18),
            "correction residual=", mp.nstr(correction_residual, 5),
            "scaled error=", mp.nstr(scaled_error, 16),
        )
        assert abs(correction_residual) < mp.mpf("1e-70")

    max_n = 100000
    logs = recurrence_logs(max_n)
    target_scaled_log = 1 - GAMMA / 2 - LOG2 / 4
    print("\nrecursive estimate checks")
    for n in (100, 1000, 10000, 100000):
        scaled = mp.e ** (logs[n] - mp.mpf(n) * LOG2 / 8)
        ratio = mp.e ** (logs[n] - logs[n - 1])
        normalized_error = n * (
            logs[n] - mp.mpf(n) * LOG2 / 8 - target_scaled_log
        ) / mp.log(n)
        print(
            f"n={n:6d}",
            "C_n/2^(n/8)=", mp.nstr(scaled, 18),
            "C_n/C_(n-1)=", mp.nstr(ratio, 18),
            "scaled log error=", mp.nstr(normalized_error, 16),
        )

    print("target C scaling =", mp.nstr(mp.e**target_scaled_log, 30))
    print("target ratio =", mp.nstr(mp.power(2, mp.mpf(1) / 8), 30))
    print("all exact-identity assertions passed")


if __name__ == "__main__":
    main()
