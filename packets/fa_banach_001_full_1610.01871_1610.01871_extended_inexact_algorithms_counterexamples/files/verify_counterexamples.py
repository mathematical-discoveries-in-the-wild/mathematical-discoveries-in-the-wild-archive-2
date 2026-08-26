"""Exact verification of the scalar counterexamples in the solution packet."""

from fractions import Fraction


def boundary_data(n: int) -> tuple[Fraction, Fraction]:
    a = Fraction(1) - Fraction(1, (n + 2) ** 2)
    x = Fraction(n + 2, 2 * (n + 1))
    return a, x


def verify(iterations: int = 100) -> None:
    x = Fraction(1)
    for n in range(iterations):
        a, expected_x = boundary_data(n)
        assert x == expected_x

        # Algorithm 9.1, sigma=1, mu=1, A=identity.
        y = xi = a * x
        eta = x - 2 * y
        assert xi + (y - x) + eta == 0
        assert abs(eta) <= max(abs(xi), abs(y - x))
        assert xi != 0 and y != x
        ss_next = x - (xi * (x - y) / (xi * xi)) * xi
        assert ss_next == a * x

        # Algorithm 10.1, nu=1, lambda=1, Z=R.
        ips_y = (1 - a) * x
        ips_eta = 2 * ips_y - x
        assert ips_eta == ips_y + ips_y - x
        assert abs(ips_eta) <= abs(ips_y - x)
        assert ips_y - ips_eta == a * x

        # Algorithm 11.1, c=M=tau=1, epsilon=0.
        pls_y = pls_xi = a * x
        pls_eta = 2 * pls_y - x
        lhs = pls_eta * pls_eta
        rhs_base = pls_xi * pls_xi + (pls_y - x) * (pls_y - x)
        assert 0 <= lhs < rhs_base  # sigma_n^2=lhs/rhs_base<1
        alpha = pls_xi * (x - pls_y) / (pls_xi * pls_xi)
        assert x - alpha * pls_xi == a * x

        x = a * x

    assert x == Fraction(iterations + 2, 2 * (iterations + 1))
    assert x > Fraction(1, 2)

    # Formula (10.1): lambda_hat=1, rho=1/6, sigma=3 gives nu=1.
    # The square-root argument is 25/9, so its positive root is 5/3.
    rho = Fraction(1, 6)
    sigma = Fraction(3)
    ratio = 2 * rho
    radicand = sigma + (1 - sigma) * ratio * ratio
    assert radicand == Fraction(25, 9)
    nu = (Fraction(5, 3) - ratio) / (1 + ratio)
    assert nu == 1

    print(f"verified {iterations} boundary iterations exactly; x_n={x}")
    print("verified formula (10.1) parameters give nu=1 exactly")


if __name__ == "__main__":
    verify()

