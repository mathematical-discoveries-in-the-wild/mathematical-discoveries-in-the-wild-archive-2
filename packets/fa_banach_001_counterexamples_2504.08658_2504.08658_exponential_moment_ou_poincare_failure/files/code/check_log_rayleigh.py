"""Check the explicit logarithmic upper bound for the Poincare quotients."""

from math import exp, log


def log_bound(k: int, t: float) -> float:
    """Log of the k-dependent part of C*Z*exp(a_k-(r*2^(k-2)-1)^2/2)."""
    r = exp(-t)
    a_k = 2.0**k
    distance = r * 2.0 ** (k - 2) - 1.0
    return a_k - 0.5 * distance * distance


for time in (0.0, 1.0, 3.0, 6.0):
    values = [(k, log_bound(k, time)) for k in (8, 12, 16, 20, 24, 28)]
    print(f"t={time:.1f}: " + ", ".join(f"k={k}: {value:.3e}" for k, value in values))
    # At large times the centers first need a larger k to separate beyond the
    # fixed unit transition width; the asymptotic quadratic term then wins.
    assert log_bound(32, time) < log_bound(30, time) < 0.0

print("All checked finite-time log bounds eventually decrease to -infinity.")
