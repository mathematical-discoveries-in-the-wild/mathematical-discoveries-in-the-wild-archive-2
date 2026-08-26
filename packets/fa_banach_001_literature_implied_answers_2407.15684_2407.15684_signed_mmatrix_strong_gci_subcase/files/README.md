# Signed-M-matrix Gaussian boxes satisfy the strong correlation inequality

Status: `literature_implied_answer (partial subcase)`.

Source target: Rotem Assouline, Arnon Chor, and Shay Sadovsky,
*A refinement of the Sidak-Khatri inequality and a strong Gaussian correlation
conjecture*, arXiv:2407.15684, Conjectures 2 and 4 on PDF page 2.

## Identification

Karlin--Rinott's 1981 total-positivity theorem, restated explicitly on page 2
of Thomas Royen's arXiv:2410.04143, says that for a nonsingular centered
Gaussian vector with covariance `Sigma`, the absolute-value vector is MTP2
exactly when a diagonal sign matrix makes `Sigma^{-1}` an M-matrix. Its
lower-orthant cdf `F` is therefore MTP2:

```text
F(s meet t) F(s join t) >= F(s) F(t).
```

Since `s+t >= s join t`, this implies the source conjecture's Gaussian-box
inequality for every signed-M-matrix precision matrix. The condition is
automatic for two Gaussian coordinates.

Geometrically, this proves the conjecture for two parallelotopes with common
facet directions `P_A(s)` and `P_A(t)` whenever `(AA^T)^{-1}` is sign-similar
to an M-matrix. In dimension two this includes every pair of coaxial
parallelograms.

## Scope

The full conjecture remains open. General precision matrices can have
sign-frustrated cycles, the folded Gaussian law then need not be MTP2, and a
numerical audit found that the stronger max/min inequality is genuinely false
outside the MTP2 class. Eight proof/counterexample routes are recorded in
`runs/fa_banach_001/attempts/2407.15684_strong_gaussian_correlation_full_push.md`.

## Files

- `main.tex` and `solution_packet.pdf`: exact implication and scope note.
- `source_paper.pdf`: arXiv:2407.15684.
- `supporting_paper_2410.04143.pdf`: Royen's restatement of the
  Karlin--Rinott criterion.
- `figures/`: rendered source and supporting pages.
- `VERIFICATION.md`: proof, provenance, computation, and PDF audit.

This is an agent-identified implication of known literature, not a claim that
the supporting authors were answering Tehranchi's conjecture.
