#!/usr/bin/env python3
"""Finite-word sanity checks for the coefficientwise Brown--Halmos converse.

This is not part of the proof.  It checks word reversal, negative-binomial
path weights, the boundary-defect identity, comparability, and the exact
weighted Toeplitz recurrence for asymmetric nonlinear positive coefficients.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb, sqrt


ALPHABET = "01"
MAX_LEN = 4
TOL = 2.0e-11

# Deliberately asymmetric and nonlinear; the one-letter coefficients are
# positive, as required for a positive regular free holomorphic function.
A = {
    "0": 1.0,
    "1": 1.3,
    "00": 0.4,
    "01": 0.2,
    "10": 0.7,
    "111": 0.1,
}


def words(max_len: int) -> list[str]:
    return [""] + ["".join(w) for n in range(1, max_len + 1) for w in product(ALPHABET, repeat=n)]


WORDS = words(MAX_LEN)


def factorizations(word: str, parts: int):
    """All ordered factorizations into the requested nonempty contiguous parts."""
    if parts == 1:
        yield (word,)
        return
    for cuts in combinations(range(1, len(word)), parts - 1):
        endpoints = (0,) + cuts + (len(word),)
        yield tuple(word[endpoints[j] : endpoints[j + 1]] for j in range(parts))


def b(word: str, m: int) -> float:
    if not word:
        return 1.0
    total = 0.0
    for p in range(1, len(word) + 1):
        inner = 0.0
        for blocks in factorizations(word, p):
            term = 1.0
            for block in blocks:
                term *= A.get(block, 0.0)
            inner += term
        total += comb(p + m - 1, m - 1) * inner
    return total


def boundary_value(out_word: str, in_word: str) -> complex:
    if out_word and in_word:
        return 0.0j
    out_code = sum((j + 2) * (int(ch) + 1) for j, ch in enumerate(out_word))
    in_code = sum((j + 3) * (int(ch) + 1) for j, ch in enumerate(in_word))
    return complex((3 + out_code - 2 * in_code) / 17.0, (1 + 2 * out_code + in_code) / 19.0)


def phi(matrix: dict[tuple[str, str], complex], m: int) -> dict[tuple[str, str], complex]:
    result: dict[tuple[str, str], complex] = {}
    for out_word in WORDS:
        for in_word in WORDS:
            value = 0.0j
            # An index alpha of Phi has coefficient a_reverse(alpha), while
            # Lambda_alpha appends reverse(alpha).  Iterating over eta in the
            # support of f therefore strips the actual suffix eta.
            for eta, coeff in A.items():
                alpha = eta[::-1]
                suffix = alpha[::-1]
                assert suffix == eta
                if out_word.endswith(suffix) and in_word.endswith(suffix):
                    out_prefix = out_word[: -len(suffix)]
                    in_prefix = in_word[: -len(suffix)]
                    weight = sqrt(b(out_prefix, m) / b(out_word, m))
                    weight *= sqrt(b(in_prefix, m) / b(in_word, m))
                    value += coeff * weight * matrix[(out_prefix, in_prefix)]
            result[(out_word, in_word)] = value
    return result


def lincomb(powers, coefficients):
    return {
        key: sum(coefficients[j] * powers[j][key] for j in range(len(coefficients)))
        for key in powers[0]
    }


def expected_toeplitz(out_word: str, in_word: str, m: int) -> complex:
    if out_word.endswith(in_word):
        prefix = out_word[: len(out_word) - len(in_word)] if in_word else out_word
        factor = sqrt(b(prefix, m) * b(in_word, m) / b(out_word, m))
        return factor * boundary_value(prefix, "")
    if in_word.endswith(out_word):
        prefix = in_word[: len(in_word) - len(out_word)] if out_word else in_word
        factor = sqrt(b(prefix, m) * b(out_word, m) / b(in_word, m))
        return factor * boundary_value("", prefix)
    return 0.0j


def check_m(m: int) -> tuple[float, float, float]:
    defect = {(w, g): boundary_value(w, g) for w in WORDS for g in WORDS}
    defect_powers = [defect]
    for _ in range(MAX_LEN):
        defect_powers.append(phi(defect_powers[-1], m))

    inverse_coeffs = [comb(p + m - 1, m - 1) for p in range(MAX_LEN + 1)]
    reconstructed = lincomb(defect_powers, inverse_coeffs)

    recurrence_error = max(
        abs(reconstructed[(w, g)] - expected_toeplitz(w, g, m)) for w in WORDS for g in WORDS
    )

    reconstructed_powers = [reconstructed]
    for _ in range(m):
        reconstructed_powers.append(phi(reconstructed_powers[-1], m))
    recovered_defect = lincomb(
        reconstructed_powers,
        [(-1) ** j * comb(m, j) for j in range(m + 1)],
    )
    defect_error = max(abs(recovered_defect[key] - defect[key]) for key in defect)

    path_error = 0.0
    for delta in WORDS:
        path_sum = 1.0 if not delta else 0.0
        for p in range(1, len(delta) + 1):
            for blocks in factorizations(delta, p):
                coeff = 1.0
                for block in blocks:
                    coeff *= A.get(block, 0.0)
                path_sum += comb(p + m - 1, m - 1) * coeff
        path_error = max(path_error, abs(path_sum - b(delta, m)))

    assert recurrence_error < TOL, (m, "recurrence", recurrence_error)
    assert defect_error < TOL, (m, "defect", defect_error)
    assert path_error < TOL, (m, "paths", path_error)
    return recurrence_error, defect_error, path_error


def main() -> None:
    print(f"binary words through length {MAX_LEN}: {len(WORDS)}")
    print(f"matrix coefficients per test: {len(WORDS) ** 2}")
    for m in (1, 2, 3):
        recurrence_error, defect_error, path_error = check_m(m)
        print(
            f"m={m}: recurrence={recurrence_error:.3e}, "
            f"defect={defect_error:.3e}, paths={path_error:.3e}"
        )
    print("PASS: all finite-word Brown--Halmos converse checks succeeded")


if __name__ == "__main__":
    main()
