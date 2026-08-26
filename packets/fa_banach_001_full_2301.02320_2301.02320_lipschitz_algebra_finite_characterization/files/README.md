# Full solution packet: Lipschitz algebras are classified by finiteness

## Source

- Tomasz Kania and Natalia Maślany, *Differential embeddings into algebras of
  topological stable rank 1*, arXiv:2301.02320 (2023; revised 2024),
  DOI: 10.1017/prm.2024.108.
- Question 1, printed page 21: “What about algebras of Lipschitz functions on
  zero-dimensional compact spaces?”  The intended property is Definition 2.3,
  approximability by jointly non-degenerate products.

## Classification

- Status: `candidate_full_solution_likely_valid`.
- Result: complete metric-space classification, with a stronger openness
  theorem and a Hölder-order extension.
- Ordinary Lipschitz case: `alpha=1`.

## Result

For every compact metric space `X` and `0 < alpha <= 1`, let
`Lip_alpha(X)` be the complex big Hölder-Lipschitz algebra with its standard
norm.  The following are equivalent:

1. `X` is finite.
2. `Lip_alpha(X)` is approximable by jointly non-degenerate products.
3. Pointwise multiplication on `Lip_alpha(X)` is open.

Consequently, every infinite zero-dimensional compact metric space answers the
source question negatively; finite spaces are exactly the positive cases.

## Proof idea

Every infinite compact metric space contains a sequence `x_n -> o` whose
radii decrease geometrically.  On this sequence, prescribe two functions that
alternate values `d(x_n,o)^alpha` and zero.  Their Hölder seminorms are bounded,
and McShane extends them to all of `X`.

An exact factorization of their product by a jointly non-degenerate nearby
pair must choose one nonzero factor at `o`.  Continuity forces that same factor
to stay nonzero along the tail, hence the other factor must vanish there.  On
one alternating parity its Hölder error quotient at `o` is exactly 1.

For the stronger non-openness result, perturb the product by a tiny nonzero
constant.  Even and odd subsequences yield two mutually contracting
inequalities for the factor values at `o`; when the factor-ball radius is less
than `1/2`, both base values must be zero, contradicting their nonzero product.

## Scope

- The theorem is for the standard **big** Hölder-Lipschitz algebras on compact
  metric spaces and includes the usual Lipschitz algebra.
- It is invariant under the standard sum/max norm conventions.
- The constructed functions need not lie in the little-Lipschitz subalgebra,
  so that distinct question is not claimed.
- Nonmetrizable compact spaces require additional metric data and are outside
  the formulation.

## Verification and novelty

- Six focused attempts upgraded one shrinking-star example to all infinite
  compact metric spaces, proved the finite converse, strengthened failure to
  non-open multiplication, extended to every Hölder order, and audited scope.
- `code/verify_alternating_obstruction.py` checks the Hölder estimates on
  80-level models for five orders and the contraction inequality.  It is a
  sanity check; the packet proof is exact.
- Bounded searches on 2026-08-11 used the exact question, title/authors,
  `jointly non-degenerate products`, `Lip(X)`, `Hölder algebra`, and `open
  multiplication`.  They found only the source/published version, talks
  repeating the question, and general background.  No later answer or this
  classification was found.  Novelty confidence is bounded, not exhaustive.

## Human review

Prioritize the geometric-subsequence selection, the McShane extension in the
metric `d^alpha`, the forced-zero tail argument, and the two limiting
inequalities in the non-openness upgrade.  Also confirm that the source's
“algebras of Lipschitz functions” means the standard big Lipschitz algebra.

## Files

- `main.tex`: self-contained expert-facing packet.
- `solution_packet.pdf`: compiled and visually inspected proof.
- `source_paper.pdf`: locally compiled original arXiv source.
- `figures/open_problem_crop.png`: full-width crop of Question 1.
- `code/verify_alternating_obstruction.py`: deterministic sanity check.
- `verification_report.md`: commands, hashes, and page-by-page QA.

