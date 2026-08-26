# Verification report

Verified at: 2026-08-11T16:27:57Z

## Mathematical checks

- Confirmed against `source_paper.pdf` that Remark 4.3 (PDF page 18) asks
  exactly whether the `GL(n,R)` action is continuous for the unit-Lipschitz-ball
  norm used in the packet.
- Confirmed source Proposition 4.4: restriction to support functions is
  injective and `GL(n,R)`-equivariant in every homogeneous degree.
- Re-derived the degree-one step: McMullen polynomiality makes every
  continuous translation-invariant one-homogeneous convex-body valuation
  Minkowski additive; the standard support-function representation then gives
  a finite measure. Translation invariance is its zero-first-moment condition,
  and source injectivity identifies the resulting integral on all Lipschitz
  functions with the original valuation.
- Rechecked the uniform orbit estimate on the Lipschitz unit ball and the
  local input bound `||g dot f||_Lip <= 2||g||_op ||f||_Lip`.
- Corrected the homogeneous-projection estimate during audit: the displayed
  interpolation formulas give the safe uniform bound `||mu_k|| <= 12||mu||`;
  no sharp constant is needed.
- In dimension two, checked that the displayed quadratic functional restricts
  to a nonzero multiple of area, so source injectivity makes the degree-two
  space one-dimensional and equivariance gives the factor
  `|det g|^{-1}`.
- Checked the degree-two matrix transformation directly from source Lemma
  3.11 and the substitution `y=Phi_h(x)`: the transformed coefficient is
  `J_g(y) h^T phi(Phi_g(y)) h`, for `h=g^{-1}`.
- Confirmed source Theorem 3 identifies every smooth degree-two valuation with
  the smooth special case of the packet's matrix-density formula.
- The unresolved `n>=3` residual is stated explicitly; the packet does not
  claim norm density of smooth valuations or a full answer in those dimensions.

## Source and novelty checks

- The exact source question is embedded as `figures/source_question.png` and
  remains legible in the rendered packet.
- The bounded novelty audit is described in the packet and ledger. No later
  answer was found in the run's cheap indexes or the bounded external checks.
- Bibliographic metadata was cross-checked for arXiv:2401.05913,
  McMullen (1980), arXiv:2302.00416, and arXiv:2005.05419.

## PDF checks

- `latexmk` completed successfully after two passes.
- Final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Ghostscript text extraction contains Theorem 1, Proposition 2, the stated
  residual limitation, and the bibliography.
- Rendered all five pages at 150 dpi and visually inspected each page. Margins,
  source crop, equations, theorem breaks, page numbers, and bibliography are
  clean, with no clipping or overlap.
- SHA-256:
  `f1eee20f28d9c7ec201d51140af083cf17ddad1dee6e9b498fe25ba9cba677a6`.

Disposition: `likely_valid_substantial_partial`; suitable for human
mathematical review.
