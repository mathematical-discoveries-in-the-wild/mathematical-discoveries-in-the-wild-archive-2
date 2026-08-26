"""Exact-formula checks for the packet's two small-ball obstructions."""

from math import erf, exp, sqrt


eps = 0.1

# Same trace on a Hilbert Sobolev space, but ranks one and two.
rank_one = erf(eps / sqrt(2))
rank_two = 1 - exp(-(eps**2))
assert rank_one > rank_two > 0

# Same L2 covariance spectrum for rank-one fields e_0 and e_N, but different
# H1 norms and hence different H1 small-ball probabilities.
N = 10
low_frequency = erf(eps / sqrt(2))
high_frequency = erf(eps / (sqrt(2) * sqrt(1 + N**2)))
assert low_frequency > high_frequency > 0

print(f"epsilon: {eps}")
print(f"same trace, rank-one probability: {rank_one:.12f}")
print(f"same trace, rank-two probability: {rank_two:.12f}")
print(f"same L2 spectrum, frequency 0:    {low_frequency:.12f}")
print(f"same L2 spectrum, frequency {N}:   {high_frequency:.12f}")
