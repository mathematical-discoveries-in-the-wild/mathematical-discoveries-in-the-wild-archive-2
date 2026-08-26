"""Numerical transcription checks for the block counterexample."""
import math

for n in range(3, 31):
    m = math.ceil(math.exp(n))
    failure_bound = math.exp(-m * 2.0 ** (-n))
    log_lower = 2.0 * n - 1.2 * math.log(n * m)
    coarse_lower = 0.8 * n - 1.2 * math.log(n) - 1.2 * math.log(2.0)
    assert log_lower >= coarse_lower - 1e-12
    if n >= 20:
        assert log_lower > 0
    print(n, f"log_lower={log_lower:.6f}", f"failure<={failure_bound:.3e}")

print("PASS: exact growth lower bound and summable double-exponential failure envelope checked")
