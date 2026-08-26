"""Exact scale checks for the sparse log-frequency construction."""

for j in range(1, 13):
    n_j = 2 ** (6 * j)
    k_j = 2 ** j
    weighted_cost = k_j ** 4 / n_j
    assert weighted_cost == 2 ** (-2 * j)
    oscillation_lower_count = max(0, k_j // 4 - 2)
    print(j, n_j, k_j, weighted_cost, oscillation_lower_count)

assert sum(2 ** (-2 * j) for j in range(1, 100)) < 1
print("PASS: weighted costs are geometric while oscillation counts diverge")
