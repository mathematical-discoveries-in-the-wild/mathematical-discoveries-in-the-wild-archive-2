#!/usr/bin/env python3
"""Finite smoke check for the explicit Z instance in the proof packet.

This does not prove the compactness/Hartman arguments.  It constructs a
rapidly growing subsequence of Pell denominators, verifies the return-time
and unique-sum inequalities, and checks a finite upper-triangular translate
matrix exactly.
"""

from decimal import Decimal, getcontext


getcontext().prec = 120
SQRT2 = Decimal(2).sqrt()


def pell_convergents():
    p_prev, q_prev = 1, 1
    p, q = 3, 2
    yield p_prev, q_prev
    while True:
        yield p, q
        p_prev, p = p, 2 * p + p_prev
        q_prev, q = q, 2 * q + q_prev


def select_return_times(count):
    selected = []
    total = 0
    convergents = pell_convergents()
    for j in range(1, count + 1):
        while True:
            p, q = next(convergents)
            error = abs(SQRT2 * q - p)
            if q > 2 * total and error < Decimal(1) / j:
                selected.append((p, q, error))
                total += q
                break
    return selected


def main():
    pairs = 8
    data = select_return_times(2 * pairs)
    r = [q for _, q, _ in data]

    running = 0
    for j, (p, q, error) in enumerate(data, start=1):
        assert q > 2 * running
        assert error < Decimal(1) / j
        running += q

    two_sums = {}
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            value = r[i] + r[j]
            assert value not in two_sums, (i, j, two_sums[value])
            two_sums[value] = (i, j)

    x = r[0::2]
    y = r[1::2]
    upper = {x[n] + y[m] for n in range(pairs) for m in range(pairs) if n <= m}
    matrix = [[int(x[n] + y[m] in upper) for m in range(pairs)] for n in range(pairs)]
    expected = [[int(n <= m) for m in range(pairs)] for n in range(pairs)]
    assert matrix == expected

    print("PASS")
    print(f"selected_return_times={len(r)}")
    print(f"checked_two_term_sums={len(two_sums)}")
    print(f"checked_translate_matrix={pairs}x{pairs}")
    print(f"largest_return_time_digits={len(str(r[-1]))}")


if __name__ == "__main__":
    main()
