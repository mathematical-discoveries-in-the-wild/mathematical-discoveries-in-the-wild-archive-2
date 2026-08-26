# Property-(wU) is stable under Bochner Lp and C(K)

Status: `candidate_full_solution_likely_valid`

This packet answers both converse questions after Theorems 2.2.2 and 2.2.3 of
Soumitra Daptari and Tanmoy Paul, *Uniqueness of Hahn--Banach extensions and some
of its variants*, arXiv:2202.00947.

Under the standing assumptions in the source (real Banach spaces, a probability
space, `1 < p < infinity`, compact Hausdorff `K`, and `X*` having the
Radon--Nikodym property), for every closed subspace `Y` of `X`:

1. `Y` has property-(wU) in `X` if and only if `Lp(mu;Y)` has property-(wU) in
   `Lp(mu;X)`.
2. `Y` has property-(wU) in `X` if and only if `C(K;Y)` has property-(wU) in
   `C(K;X)` (for nonempty `K`).

The new directions follow by representing functionals by pointwise dual
densities. Norm attainment forces those densities to be norm-attaining almost
everywhere, while equality of the global extension norms forces pointwise
norm preservation. Property-(wU) then gives pointwise uniqueness.

Files:

- `solution_packet.pdf`: human-review packet.
- `main.tex`: packet source.
- `source_paper.pdf`: local render of the exact ingested arXiv source.
- `figures/open_problem_crop.png`: source page 7 with the standing RNP
  hypothesis, Theorems 2.2.2--2.2.3, and the open converse question.
- `VERIFICATION.md`: adversarial proof review and novelty-search record.

Human review should focus on the standard dual representation theorems and on
the passage from equality of total variation norms to equality of the
variation measures in the `C(K)` argument.

