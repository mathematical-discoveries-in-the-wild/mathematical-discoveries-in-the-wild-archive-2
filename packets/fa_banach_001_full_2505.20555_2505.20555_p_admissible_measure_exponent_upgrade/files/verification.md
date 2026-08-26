# Verification report

Verdict: `candidate_full_likely_valid`

## Exact target audit

- Question 2.21 is on PDF page 14.
- Proposition 8.1 answers it for p-admissible weights.
- Remark 8.2, PDF page 32, explicitly proposes the extension to arbitrary
  p-admissible measures, without absolute continuity.
- The packet proves exactly that extension for arbitrary open domains.
- Open Problem A.18 on absolute continuity of p-admissible measures remains
  outside the claim.

## Dependency audit

1. The source p-Poincare inequality extends from smooth approximants to
   `H^{1,p}` functions on compactly contained cubes using only finite cube
   measure and Holder.  Absolute continuity is not involved.
2. Doubling compares each active grid cube with its comparable enclosing cube,
   giving the difference-of-averages estimate.
3. The identity `sum grad(phi_k)=0` gives the gradient estimate directly at
   every point.  It does not assume that grid boundaries are `mu`-null.
4. Since `s>p>=1`, `s>1`; hence the Hardy--Littlewood maximal operator is
   strongly bounded on `L^s(mu)` for doubling `mu`.
5. Doubling differentiation plus comparable off-center cubes gives
   `u_h -> u` almost everywhere.  Maximal domination gives strong `L^s`
   convergence.
6. The graph closure defining `H^{1,s}` is a closed subspace of a reflexive
   `L^s` product.  Mazur convexification supplies a genuine strong graph-norm
   approximating sequence.
7. On finite cubes, strong `L^s` convergence implies strong `L^p`
   convergence.  Uniqueness of the p-gradient therefore identifies the new
   s-gradient with the gradient in the hypothesis.
8. The local-to-global construction uses locally supported smooth
   approximants with summable error budgets.  Its derivative error includes
   the partition-gradient term explicitly.

## Source-proof comparison

The source appendix estimates `||u_h-u||_s` by applying an s-Poincare
inequality to `u` before `u in H^{1,s}` has been concluded.  The present proof
does not use that step.  Its maximal-function argument only assumes
`u in L^s`, and the gradient bound only assumes the already known
`u in H^{1,p}` with `grad u in L^s`.

## Edge cases

- `p=1`: still valid because `s>1`, which is exactly what the strong maximal
  inequality and reflexivity require.
- Singular measures: no convolution with respect to Lebesgue measure,
  Rademacher theorem, Fubini theorem, or weak distributional derivative is
  used.
- Cube boundaries of positive measure: the algebraic gradient identity avoids
  any almost-everywhere partition by cube interiors.
- Unbounded `Omega`: the global smooth approximants have finite graph norm
  because their error from the given global `L^s` pair is summable.

## Novelty bounds

Checked on 2026-08-11:

- the run registry and solution/attempt/proof-gap indexes for arXiv:2505.20555
  and the core exponent-upgrade wording;
- the final Springer version of the source paper, published 2025-12-10, which
  retains Remark 8.2;
- exact web/arXiv searches for the wording of Remark 8.2 and combinations of
  `p-admissible measure`, `H^{1,p}`, `H^{1,s}`, and `discrete convolution`.

No later resolution or equivalent maximal-function proof was found.  Novelty
confidence is moderate pending specialist review.

## Recommendation

Send to a specialist in weighted/metric Sobolev spaces.  The most important
checks are the off-center differentiation argument and whether the source's
gradient-uniqueness statement indeed applies to its exact smooth-test
definition of p-admissibility without an unstated absolute-continuity
hypothesis.

## Artifact audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully on 2026-08-11.
- The final log contains no warnings, undefined references, or overfull or
  underfull boxes.
- All six pages of `solution_packet.pdf` were rendered at 120 dpi and visually
  inspected.  The two source-evidence crops are complete and readable; no text,
  formulas, or references are clipped.
