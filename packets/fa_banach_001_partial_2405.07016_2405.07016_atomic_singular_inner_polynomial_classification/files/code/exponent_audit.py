"""Audit the sharp exponent bound in the atomic singular-inner proof.

This is a finite mechanical check of an elementary formula, not a substitute
for the symbolic argument in the packet.
"""


def audit(limit: int = 50) -> None:
    cases = 0
    for m in range(1, limit + 1):
        for n in range(1, limit + 1):
            values = []
            for j in range(1, m + 1):
                for ell in range((m - j) * (n - 1) + 1):
                    r = n * (j - 1) + ell
                    values.append(r - j)
            expected = m * (n - 1) - n
            assert max(values) == expected, (m, n, max(values), expected)
            cases += 1
    print(f"verified {cases} (m,N) pairs; sharp maximum formula holds")


if __name__ == "__main__":
    audit()
