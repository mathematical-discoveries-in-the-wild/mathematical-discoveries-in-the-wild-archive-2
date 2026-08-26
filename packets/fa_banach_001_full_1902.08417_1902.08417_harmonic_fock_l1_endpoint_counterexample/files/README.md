# 1902.08417 — Critical harmonic-Fock projection counterexample

## Outcome

Candidate new full counterexample, likely valid and requiring specialist review.

Vujadinovic conjectures that the harmonic Fock projection
`P_alpha` is bounded on `L^p(R^n,dmu_beta)` for `p >= 1` exactly when
`p beta = 2 alpha`.  The paper also claims this in every even dimension.
The packet disproves both statements at the critical endpoint

    n = 4,  p = 1,  beta = 2 alpha.

The proof is elementary once the exact four-dimensional kernel is written
down.  After scaling to `alpha=1`, put `y=R e_1` and
`x=y+(u,v)`, with `u` real and `v` in `R^3`.  The absolute kernel column
relative to `dmu_2` becomes

    pi^(-2) integral exp(-(u^2+|v|^2)/2)
      |(R+u) sin(R|v|)/|v| + cos(R|v|)| du dv.

Restricting to `|u| <= 1` and `1 <= |v| <= 2` shows that this is bounded
below by `c R - C`.  A bounded integral operator on `L^1` must have
uniformly bounded absolute columns, so `P_1` is unbounded on
`L^1(R^4,dmu_2)`.

## Files

- `main.tex` — exact target, definitions, theorem, proof, source-proof audit,
  verification, literature check, and limitations.
- `solution_packet.pdf` — compiled review packet.
- `source_paper.pdf` — arXiv source paper.
- `figures/open_problem_crop.png` — source theorem, open problem, and conjecture.
- `verify_column_growth.py` — deterministic symbolic/numerical checks.
- `tmp/` — build and render artifacts.

## Verification

Run:

    conda run --no-capture-output -n sandbox python verify_column_growth.py

The checker compares the closed kernel with its zonal-harmonic series,
checks the exact Gaussian cancellation, evaluates the absolute column by
quadrature for increasing `R`, and verifies the analytic lower bound.

## Novelty and review

Targeted searches for the exact paper title, conjecture, endpoint theorem,
counterexamples, corrections, and errata found the 2019 arXiv paper and its
2022 journal publication, but no correction or later resolution.  A
specialist should independently verify the normalization and closed kernel,
check the approximate-identity column argument, and search MathSciNet,
zbMATH, and citation databases before any public claim.  If confirmed, the
author and journal should be notified because the argument also contradicts
the published even-dimensional endpoint theorem.

