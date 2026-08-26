# Degenerate full resolution of the stated non-Archimedean Zauner problem

Status: `candidate_full_likely_valid`

Source: K. Mahesh Krishna, *Non-Archimedean Welch Bounds and
Non-Archimedean Zauner Conjecture*, arXiv:2210.07062, Section 3, PDF pages
4--6.

## Full result

Equation (FU) in the source implies `|r|=1` for every positive integer `r`:
substitute `r` copies of `1`. The source does not require distinct vectors or
distinct lines. Therefore, for every `d` and every `n >= 2`, take

`tau_1 = ... = tau_n = e_1`.

Then all self- and cross-inner-products equal `1`, while the frame operator is
the already diagonal matrix `diag(n,0,...,0)`. Both sides of the equality in
Question 3.1 are `1`. Thus every well-posed pair `(d,n)` is admissible, and the
stated non-Archimedean Zauner conjecture follows by taking `n=d^2`.

The same construction attains equality in every higher-order Welch bound from
the paper. It also shows that the vector formulation of Question 3.6 has no
finite Gerzon-type maximum: `n(K,1,d,1)` is unbounded.

## Scope

This is a full resolution only of the exact source statements. If one adds a
requirement that the vectors span distinct one-dimensional subspaces, or that
the frame operator be a nonzero scalar multiple of the identity, the argument
does not apply. Conjecture 3.2 contains an undefined `|n|`; the construction
satisfies both the natural reading `n=d^2` and the likely alternative `|d|`,
because both absolute values are `1` under (FU).

## Novelty

Cheap run indexes and bounded official-arXiv searches on 2026-08-09 by exact
title, arXiv id, conjecture phrase, distinctness, and solution terms found no
later amendment or matching resolution. Expert bibliographic review remains
required.

## Files

- `solution_packet.pdf`: source evidence, theorem, complete proof, consequences,
  limitations, and novelty record.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/`: readable crops of Questions 3.1 and 3.6 and Conjecture 3.2.
- `VERIFICATION.md`: proof audit and reviewer focus.
- `novelty_search.md`: bounded novelty-search record.

Human review should focus on the literal admissibility of repeated vectors.
