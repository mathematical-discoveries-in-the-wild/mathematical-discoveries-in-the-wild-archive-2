# Verification Report

Status: `candidate_full_solution_likely_valid`.

## Source

- `source_paper.pdf` is the 30-page arXiv PDF for arXiv:1804.00204.
- The exact question is Remark 1 on PDF page 12.
- `figures/question_crop.png` is a direct readable crop of the full remark.

## Proof checks

1. A positive homogeneous polynomial has even degree, since
   `F(-x)=(-1)^d F(x)`.
2. A minimum `u` of `F` on the unit sphere exists and has `F(u)>0`.
3. For the constraint `(||x||^2-1)/2=0`, Lagrange multipliers give
   `grad F(u)=lambda u`; Euler's identity gives `lambda=d F(u)>0`.
4. The constrained second-order necessary condition is
   `v^T(H_F(u)-lambda I)v>=0` for `v` orthogonal to `u`, hence the tangential
   Hessian block is bounded below by `lambda I`.
5. Differentiated Euler homogeneity gives
   `H_F(u)u=(d-1)lambda u`; symmetry then kills all radial--tangential cross
   terms. Thus `H_F(u)` is positive definite.
6. The inertia of a continuous nonsingular symmetric matrix family is locally
   constant. For `n>=2`, `R^n\{0}` is connected, so the positive inertia at
   `u` propagates to every nonzero point.
7. For `n=1`, the form is `a x^d` with `a>0` and even `d`, and its second
   derivative is positive away from zero.
8. On a nontrivial segment the one-variable second derivative is positive
   except possibly where the segment crosses the origin, at most once. Its
   integral on every nontrivial subinterval is positive, so the restriction
   is strictly convex.
9. The argument does not use tensor nonnegativity or weak irreducibility and
   covers the printed source question as a special case.

## Novelty check

The cheap run indexes have no exact-id or core-question result. Bounded web and
arXiv searches through 2026-08-13 used the exact source sentence and
combinations of `positive definite homogeneous polynomial`, `nonsingular
Hessian`, and `strict convexity`. They found no matching answer. This supports,
but does not establish, novelty; confidence is moderate pending specialist
review.

## Rendering checks

- `latexmk` completed after two `pdflatex` passes with no warnings,
  unresolved references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` has 2 US-letter pages. PyMuPDF extracted 4,206
  characters, including text from both pages.
- Both pages were rasterized at 170 dpi and inspected at original resolution.
  The source question is readable, and no text, equation, footer, or reference
  is clipped, overlapped, or off-page.
- SHA-256: `source_paper.pdf`
  `776d847d9db71ed0bc371b40f53c4eb07282ff9042bd902a8ae829f9fba57cf7`;
  `figures/question_crop.png`
  `4aab3c8f528aef7b0954588746b04c308d42744e512e1cd19059f9e45b7290d3`;
  `solution_packet.pdf`
  `0621bab9a718acfae3366e084f1f43e0e83071f98c5b6ccec065ade88197668d`.
