# Verification report

Status: `candidate_full_likely_valid`.

## Mathematical audit

1. The exact source statement was checked in arXiv:2505.14132v3, PDF p. 14,
   Remark 3.8.  It asks whether compactness/order-density of conditionally
   almost-periodic vectors implies discrete spectrum for arbitrary
   KH-dynamical systems.
2. A finite orbit net spans a finite-rank KH-submodule.  Its orthogonal
   projection has the required uniform error by the Pythagorean identity.
3. Conjugation orientation was checked explicitly:
   `Q_t=T_{t^{-1}}PT_t` satisfies
   `x-Q_t x=T_{t^{-1}}(I-P)T_t x`.
4. The cyclic convex fixed-point lemma was proved internally.  Finite mixing
   realizes lattice meets of squared norms; the parallelogram identity makes
   the minimizing net order-Cauchy; covariance and uniqueness give
   invariance.
5. The Hilbert--Schmidt hull is bounded by `sqrt(#F)`, and the evaluation map
   `B -> Bx` is order-continuous under
   `|Bx| <= |B|_HS |x|`.  Hence the approximate-fixing constraint survives
   cyclic convexification and order closure.
6. The final use of the Edeko--Haase--Kreidler decomposition theorem is exact:
   ranges of invariant Hilbert--Schmidt operators generate `E_ds` in order.
7. Ordinary Hilbert spaces, finite-rank modules, atomic shift bases, and
   moving-support examples were used as sanity checks.  The rank-one averaging
   route can fail under support escape, but the projection-orbit proof does
   not share that defect.

No computational verifier is relevant: the argument is structural and uses no
finite numerical claim.

## Novelty audit

- Run indexes and local parsed sources were searched for arXiv:2505.14132 and
  the central phrases.
- The February 2026 source revision still marks the implication unknown.
- Bounded web/arXiv searches on 13 August 2026 found no exact later solution.
- The possibility that the fixed-point lemma is known under different
  Banach--Kantorovich terminology is recorded; novelty confidence is moderate.

## Rendering audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully after two passes.
- The final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- `solution_packet.pdf` has five letter-size pages.  All five rendered pages
  were visually inspected at full resolution; text, formulas, bibliography,
  and the full-width source screenshot are legible and unclipped.
- SHA-256:
  - packet: `caafdef29daacb92effb6d371743c4f92430f72b0bb0df5cc1e444c8b17a20ae`
  - source PDF: `735d4a1d2273b5ef927b3821d8e20bac93b73466e06ea4092080bd8373e96e29`
  - LaTeX source: `067bd3e6355c7175838dff92cb05ad0638e388e32870284eca082480dbbfccee`
  - problem crop: `eef865da37128e1e259444d32ae852cc19e302daa12807135c2214c3c4620c2e`
