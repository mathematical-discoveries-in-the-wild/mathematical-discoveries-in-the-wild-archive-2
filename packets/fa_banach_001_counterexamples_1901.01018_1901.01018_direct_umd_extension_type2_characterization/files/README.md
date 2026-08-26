# Direct UMD extension: counterexample and type-2 characterization

Result type: `counterexamples`

Status: candidate scoped counterexample and full characterization, likely
valid, pending expert review.

## Source problem

Martin Ondrejat and Mark Veraar, *On temporal regularity of stochastic
convolutions in 2-smooth Banach spaces*, arXiv:1901.01018, Introduction,
published in *Annales de l'Institut Henri Poincare (B) Probabilites et
Statistiques* 56 (2020), 1792-1808.

The authors ask whether their results extend to UMD Banach spaces and suggest
an analogue for UMD-valued continuous local martingales with a suitable
quadratic variation.

## Contribution

The direct extension with the paper's original
`L^infinity_t gamma(H,X)` data class is false. For every `1 < r < 2`, the UMD
space `ell^r` admits deterministic scalar-Brownian integrands of pointwise
norm one whose finite truncations have unbounded expected
`B^(1/2)_(Phi_2,infinity)` norm. The infinite integrand does not even produce
an `ell^r`-valued stochastic integral at the accumulation time.

The packet also proves the exact positive boundary among separable UMD spaces:
the direct endpoint estimate, and hence the full same-data suite of the source
paper, holds exactly when the space has type 2. UMD plus type 2 implies
martingale type 2, hence an equivalent 2-smooth norm; the source theorem then
applies and equivalent norms transfer its conclusions back.

This does **not** rule out a different UMD theorem whose hypotheses directly
control the Gaussian characteristic of the full quadratic variation. That
broader reformulation remains open here.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 3 open-question evidence.
- `verification.md`: proof audit, scope, and novelty notes.
- `tmp/`: build products and rendered pages used for visual QA.

## Novelty check

A bounded search of the run indexes and arXiv/web results used the exact paper
title and combinations of `UMD`, `Besov-Orlicz`, `temporal regularity`,
`stochastic convolution`, `continuous local martingale`, and `quadratic
variation`. It found the source, Yaroslavtsev's UMD quadratic-variation/BDG
work, and later applications still using the 2-smooth theorem, but no exact
statement of this counterexample or characterization. The ingredients are
standard enough that novelty confidence is only moderate; the mathematical
claim is the review target, not a claim of publication novelty.

## Human review focus

Check the interpretation of "extension of the results" as retaining the
source paper's data class, the lower bound from the inhomogeneous
Besov-Orlicz norm, and the UMD-plus-type-2 implication to martingale type 2.

