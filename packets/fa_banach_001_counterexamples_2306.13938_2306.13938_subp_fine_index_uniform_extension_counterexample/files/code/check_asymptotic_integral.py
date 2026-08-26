"""Check the Laplace-integral asymptotic used in the counterexample.

This is a numerical sanity check only.  The proof uses the elementary change
of variables and the Gamma-integral asymptotic.
"""

import mpmath as mp


def main() -> None:
    mp.mp.dps = 50
    n = mp.mpf(3)
    theta = mp.mpf(3) / 2
    a = mp.mpf(7) / 12
    b = a * theta
    u0 = mp.mpf(4)

    print("delta integral ratio_to_delta^(a*theta-1)")
    for k in range(2, 9):
        delta = mp.power(10, -k)
        lam = theta * delta / n
        integral = mp.power(lam, b - 1) * mp.gammainc(1 - b, lam * u0, mp.inf)
        ratio = integral / mp.power(delta, b - 1)
        print(
            f"1e-{k:<2d} {mp.nstr(integral, 12):>16s} "
            f"{mp.nstr(ratio, 12):>20s}"
        )

    expected = mp.power(theta / n, b - 1) * mp.gamma(1 - b)
    print("predicted limiting ratio", mp.nstr(expected, 15))


if __name__ == "__main__":
    main()

