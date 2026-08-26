"""Numerical audit of the universal constants in the partial theorem."""

from math import gamma, pi, sqrt


def delta(k: int) -> float:
    mean_q = gamma(k / 2) ** 2 / (
        gamma((k - 1) / 2) * gamma((k + 1) / 2)
    )
    return 1.0 - (k / (k - 1)) * mean_q**2


def main() -> None:
    for k in range(2, 11):
        value = delta(k)
        assert 0.0 < value < 1.0
        print(f"k={k:2d}  delta_k={value:.12f}  eta_k={sqrt(value):.12f}")

    expected = 1.0 - 3.0 * pi**2 / 32.0
    assert abs(delta(3) - expected) < 1e-14
    print("k=3 closed form verified: delta_3 = 1 - 3*pi^2/32")


if __name__ == "__main__":
    main()

