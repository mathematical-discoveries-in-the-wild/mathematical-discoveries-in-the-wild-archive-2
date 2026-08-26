# Pointwise covariance determines the projective Dunford moment

Result type: `full`

Status: candidate full affirmative answer to Problem 9.5, likely valid pending
expert review.

Source paper:

- Svante Janson, “The space D in several variables: random variables and
  higher moments,” *Mathematica Scandinavica* 127(3) (2021), 544–584,
  arXiv:2004.00237, DOI `10.7146/math.scand.a-128971`.
- Open-question location: Problem 9.5, source PDF page 31.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

Problem 9.5 has an affirmative answer.  For every finite `m`, if two
D-measurable `D([0,1]^m)`-valued random variables have uniformly bounded
pointwise second moments and equal covariances at every pair of points of the
split compactum, then their projective Dunford second moments are equal.

The missing observation is that every finite Baire measure on a finite power
of the split interval has separable `L^2`.  Proposition A.1 reduces each
coordinate sigma-field, modulo the corresponding marginal measure, to the
pullback of the countably generated Borel sigma-field of `[0,1]` plus only
countably many positive atoms.  The source's Baire-Fubini theorem then makes
the random functions strongly measurable and square integrable in the
separable Hilbert space supplied by Grothendieck factorization.  Pointwise
covariance equality becomes equality of the Hilbert trace-class covariance
operators, so every bounded bilinear expectation agrees.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Problem 9.5.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the run registry, solution, attempt, and proof-gap indexes
were searched by arXiv id, exact title, and the terms “projective Dunford
moment” and “split interval”.  Targeted web searches for the quoted problem,
the title together with the core terms, and the arXiv id found the source paper
and the older Janson–Kaijser background paper, but no later resolution.  This
is a bounded search, so novelty confidence is moderate rather than definitive.

## Scope and human review focus

The packet solves the displayed second-moment Problem 9.5.  It does not settle
the broader question in Remark 8.10 asking whether the canonical map on full
tensor biduals is injective.  Review should focus on the measure-algebra
separability lemma and the application of Theorem 6.1 to the quadratic random
function on the doubled split compactum.
