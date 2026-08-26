# Verification report

Date: 2026-08-11  
Status: candidate full solutions, likely valid

## Source integrity

- Cached source PDF SHA-256:
  `db5f87d84f1863d0b59431109b622bc1c2a87c8b2293e1f89f1212d5fe4967c5`.
- Packet copy `source_paper.pdf` has the identical hash.
- `figures/problem_crop.png` was rendered directly from source PDF page 6 and
  contains the full text of Questions 6.1 and 6.2.

## Mathematical audit

1. The comparison lemma was checked in both directions. The contrapositive
   construction uses disjoint tail blocks with `v`-mass in `[1,2]`; the upper
   bound is justified by `v_n -> 0`. It produces finite `u`-mass and infinite
   `v`-mass exactly as required.
2. Backward-shift invariance is correctly translated to
   `I_x subset I_v` for `v_n=x_{n-1}` (the first coordinate contributes only
   a finite term).
3. For the envelope `y_n=max(x_n,kappa*y_{n-1})`, the error recurrence
   `d_n <= kappa*d_{n-1}+kappa*x_{n-1}*1_S(n)` was checked separately on and
   off the exceptional set. Summation gives a globally summable error, so the
   generated ideal is unchanged.
4. The nonincreasing rearrangement in Theorem 2 exists because a positive
   null sequence has only finitely many terms above any fixed positive level.
   At its factor-two drops, predecessor weights decrease geometrically, so
   their sum is finite. This supplies one regular summand after an ideal
   isomorphism.
5. The witness set for analyticity is Borel: convergence of a nonnegative
   subseries is an `F_sigma` condition in the continuous partial sums, and
   divergence of the shifted subseries is `G_delta`. Its projection is
   analytic.
6. The interpretation of Question 6.1 is explicitly limited to ideal
   isomorphism, matching the convention in the source paragraph immediately
   preceding the question.

No unresolved logical dependency or unproved external theorem beyond the
standard definition of an analytic set as a projection of a Borel set remains
in the argument.

## Build and visual QA

- Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final packet: 5 letter-size pages.
- Final packet SHA-256:
  `2299dbb68dcaeaeab151a5cd62d3082b87f54ab8d3d245846b51d80f659a45a9`.
- The final log contains no undefined references, overfull boxes, underfull
  boxes, or LaTeX errors.
- All five pages were rendered to PNG and visually inspected. The source
  excerpt, formulas, theorem breaks, margins, and references are legible; no
  clipping, overlap, or raster artifact remains.
