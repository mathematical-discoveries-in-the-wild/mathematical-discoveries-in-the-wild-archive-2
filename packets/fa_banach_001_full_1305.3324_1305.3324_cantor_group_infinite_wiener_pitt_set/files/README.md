# arXiv:1305.3324 — infinite Wiener–Pitt set for the Cantor group

Status: `candidate_full_solution` (affirmative), pending expert review.

Source: Przemysław Ohrysko and Michał Wojciechowski, *On the
relationships between Fourier–Stieltjes coefficients and spectra of
measures*, arXiv:1305.3324 / Studia Mathematica 221 (2014), Final Remarks
item 5.

## Result

For the Cantor group `D = product_N Z/2Z`, the packet constructs a strictly
decreasing positive sequence `a_n -> 0` such that

`K = {0} union {a_n : n >= 1}`

is a Wiener–Pitt set for the full measure algebra `M(D)`. Thus every measure
whose Fourier–Stieltjes range lies in `K` has natural spectrum. No norm bound
and no strong-continuity assumption is imposed.

## Main mechanism

The 2026 continuation arXiv:2510.24578 supplies a quantitative theorem for
rounding almost integer-valued functions on finite abelian groups. Since the
dual of the Cantor group is an increasing union of finite groups, finite
roundings can be lifted from finite quotients and passed to a weak-star limit.
This produces the full level-set idempotent without requiring the level set to
be finite.

A recursive diagonal construction handles all possible measure norms. For a
given measure, its finite prefix is isolated at a stage above its norm, and the
tail admits idempotents `e_n` with controlled norms. Both

`mu^2 = sum a_n^2 e_n` and `mu^3 = sum a_n^3 e_n`

converge in measure norm. Orthogonality then forces every Gelfand value of
`mu` to be an actual Fourier value or a limit of such values. The cube removes
the negative square-root ambiguity left by the square.

## Files

- `solution_packet.pdf`: rendered proof and verification notes.
- `main.tex`: packet source.
- `source_paper.pdf`: original paper containing the question.
- `supporting_paper_2510.24578.pdf`: decisive 2026 finite-rounding input.
- `figures/open_problem_crop.png`: source-page crop of Final Remarks item 5.
- `verification.md`: audit checklist and novelty-search bounds.
- `evidence_sources/README.md`: source metadata and precise supporting scope.

The associated ledger is
`ledger/results/1305.3324_cantor_group_infinite_wiener_pitt_set.json`.
