"""Sanity checks for countable-fibre local-dimension universality.

The proof is analytic.  This script checks parameter margins and the closed
form logarithmic slopes used in the three constructions.
"""

from math import exp, lgamma, log


def beta_function(a: float, b: float) -> float:
    return exp(lgamma(a) + lgamma(b) - lgamma(a + b))


def geometric_weights(q: float, count: int) -> list[float]:
    return [(1.0 - q) * q**n for n in range(count)]


# The truncated normalization agrees with the exact geometric tail formula.
q = 1.0 / 64.0
p = geometric_weights(q, 80)
tail = q**80
assert abs(sum(p) + tail - 1.0) < 1e-14


print("symmetric packet targets")
for target in (1.0 / 3.0, 0.75, 1.0):
    tau = 1e-2
    log_widths = [log(tau) + 2.0 * log(mass) / target for mass in p]
    log_centres = [log(mass) for mass in p]
    for n in range(30):
        assert log_widths[n] <= log_centres[n] - log(16.0)
        # Each width is at most x_n/16 and x_(n+1)=q*x_n, so their
        # sum is strictly smaller than the centre gap.
        assert (1.0 + q) / 16.0 < 1.0 - q

    # At a packet scale, the aligned mass is p_n^2 and the slope tends to beta.
    slopes = [2.0 * log(p[n]) / log_widths[n] for n in (10, 30, 50, 70)]
    assert abs(slopes[-1] - target) < 0.01
    print(f"beta={target:.6g} slopes=" + " ".join(f"{x:.8f}" for x in slopes))


print("zero target every-scale envelope")
tau0 = 1e-6
for n in (10, 20, 40, 80, 160):
    # If ell_n <= r < ell_(n-1), the aligned tail is at least p_n^2.
    # The largest possible exponent in that interval is asymptotic to O(1/n).
    log_pn = log(1.0 - q) + (n - 1) * log(q)
    log_ell_previous = log(tau0) - (n - 1) ** 2
    exponent_upper = (2.0 * log_pn) / log_ell_previous
    assert exponent_upper > 0
    if n >= 80:
        assert exponent_upper < 0.12
    print(f"n={n:3d} exponent_upper={exponent_upper:.10f}")


print("one-sided power packet targets")
lam = 0.75
for target in (1.5, 2.0, 4.0):
    d_tail = max(lam, target / 2.0) + 1.0
    q_high = exp(-8.0 * d_tail)
    tau = 1e-5
    a = lam
    b = target - lam
    beta_constant = a * beta_function(a, b + 1.0)
    assert beta_constant > 0
    assert 2.0 * d_tail > target
    assert q_high ** (1.0 / d_tail) < 1.0 / 16.0

    slopes = []
    for n in (20, 60, 120, 240):
        log_pn = log(1.0 - q_high) + (n - 1) * log(q_high)
        log_xn = log_pn / d_tail
        log_elln = log(tau) + 2.0 * log_pn / target
        assert log_elln < log_xn - log(16.0)
        # At r=ell_n the aligned beta-integral contributes c*p_n^2.
        slope = (log(beta_constant) + 2.0 * log_pn) / log_elln
        slopes.append(slope)
    assert abs(slopes[-1] - target) < 0.02
    print(
        f"beta={target:.6g} D={d_tail:.6g} c_beta={beta_constant:.8g} slopes="
        + " ".join(f"{x:.8f}" for x in slopes)
    )


print("all_checks_passed")
