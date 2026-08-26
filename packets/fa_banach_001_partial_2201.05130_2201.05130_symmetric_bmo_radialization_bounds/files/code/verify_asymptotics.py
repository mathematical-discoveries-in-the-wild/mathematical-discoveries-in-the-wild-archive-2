"""Numerical sanity checks for the logarithmic-cusp lower-bound asymptotics.

This script is not part of the proof.  It samples X_i ~ Uniform[1,2] and
checks that

  n/2 * MAD(log(sum_i X_i^2)) / sqrt(n)

approaches sigma/(mu*sqrt(2*pi)), where mu=E[X_i^2] and
sigma^2=Var(X_i^2).
"""

from math import pi, sqrt

import numpy as np


def run(n: int, samples: int, rng: np.random.Generator) -> float:
    # Chunk to keep memory bounded.
    values = []
    left = samples
    while left:
        count = min(left, 25_000)
        x = rng.uniform(1.0, 2.0, size=(count, n))
        values.append(0.5 * n * np.log(np.square(x).sum(axis=1)))
        left -= count
    y = np.concatenate(values)
    return float(np.mean(np.abs(y - y.mean())) / sqrt(n))


if __name__ == "__main__":
    mu = 7.0 / 3.0
    sigma2 = 34.0 / 45.0
    limit = sqrt(sigma2) / (mu * sqrt(2.0 * pi))
    print(f"predicted_limit={limit:.9f}")
    rng = np.random.default_rng(220105130)
    for n in (10, 25, 50, 100, 200):
        estimate = run(n, 200_000, rng)
        print(f"n={n:3d} estimate={estimate:.9f} error={estimate-limit:+.9f}")
