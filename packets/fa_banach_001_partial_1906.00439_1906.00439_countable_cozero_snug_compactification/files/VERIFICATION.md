# Verification

Status: `candidate_partial_likely_valid_needs_human_review`

## Source checks

- The arXiv v1 conjecture signal is genuine.
- The 2021 published paper changes the snugness definition from the erroneous
  displayed `g in bar G` to `g in G`, and states the intended question as
  Conjecture 6.1.4.
- Proposition 6.1.1 of the published paper explains why taking all of `E_0 q`
  is not a general solution.

## Construction checks

- The cozero neighborhoods are replaced by finite intersections, so they are
  decreasing without changing their intersection.
- Each `h_n` takes values in `[0,1]`, is positive at the designated point, and
  has cozero set `U_n`.
- `R_1=1/h_1` and `R_{n+1}=R_n^2/h_{n+1}` are continuous into
  `[1,infinity]` and are finite exactly on `U_n`.
- For `i<j`, `R_i/R_j` extends continuously by zero on `X\U_j`; this follows
  first from `R_n/R_{n+1}=h_{n+1}/R_n` and then by multiplication.
- In a finite linear form, the largest-index nonzero pole coefficient controls
  the sign at every point outside its finite domain.
- A finite lattice polynomial is a finite supremum of finite infima of linear
  forms. The reversed pole-coefficient vectors order those forms
  lexicographically at each boundary stratum. Ties leave only bounded
  continuous remainders, so maxima and minima also extend continuously.
- Every generated function is finite on the dense subspace and vanishes at the
  designated point; its lift is therefore an element of `D_0 X` and drops to
  `E_0 q`.
- Clamping an extended lift by `t -> min(max(t,0),1)` is bounded continuous on
  `X` and vanishes at the point. Hence the generated vector lattice is closed
  under the truncation operation.

## Snugness checks

- Bounded continuous pointed functions are included. Their cozero sets away
  from the point and their con sets around the point form a base for `O(X)` by
  compact Hausdorff normality.
- The centered pole `g_n` has finite domain exactly `U_n`.
- Every generated element is finite on the image sublocale, while the domains
  of the `g_n` already intersect to that sublocale. Thus the intersection over
  all finite domains is exact.

## Scope checks

- The theorem is explicitly spatial and countably cozero-presented.
- It does not claim that every Lindelof sublocale has a countable cozero
  presentation in an arbitrary compactification.
- It does not promote the superseded arXiv v1 overline as a counterexample to
  the corrected published conjecture.

## Artifact checks

- `main.tex` compiled without errors.
- `solution_packet.pdf` was rendered to page images and every page was visually
  inspected.
- Both official source PDFs open as valid PDFs.
