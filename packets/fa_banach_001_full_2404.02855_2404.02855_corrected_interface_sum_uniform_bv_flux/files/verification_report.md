# Verification report

Verdict: `candidate full solution, likely valid`

## Target and version match

- arXiv v1 states a mass-ratio coefficient. It is false for a uniform source
  on `[0,1]`, target atoms `0,1`, and masses `delta,1-delta`, where the
  quantity is `-log(delta(1-delta))`.
- The 2025 published normalization, reproduced in the author's thesis,
  defines the shifted dual potential and states the corrected coefficient
  `log(2) sum_ij ||y_i-y_j|| h_ij(0)` as a conjecture.
- The packet proves the corrected, fixed-common-support formulation used by
  the source's stability theorems.

## Proof audit

1. The polyhedral Brenier potential is the maximum of affine functions with
   slopes `y_j`; it is convex and `R_y`-Lipschitz.
2. Its gradient is a piecewise-constant BV map. Across an `i,j` facet, the
   jump vector and oriented normal are parallel, so the trace of the Hessian
   jump measure is `||y_i-y_j|| H^(d-1)|F_ij`.
3. The source's `H_ij(0)` is precisely the trace of that common facet on
   `L_i`. Summing ordered pairs counts each facet twice.
4. Since the density is at most `M`, the conjectured sum without `log(2)` is
   at most twice `M` times the Laplacian mass in any ball containing the
   source support.
5. Mollification preserves convexity and the gradient bound. The divergence
   theorem bounds the Laplacian mass in `B(0,r)` by
   `R_y H^(d-1)(partial B(0,r))`.
6. Weak convergence of the mollified Laplacians at continuity radii, followed
   by `r downarrow R_x`, gives the claimed constant.
7. Multiple-tie sets are lower dimensional after inactive affine pieces are
   removed and have zero `(d-1)`-measure. Repeated atoms contribute zero after
   merging.

## Scope and reviewer focus

- Confirm the intended common-support radius in the phrase "uniformly
  bounded for all discrete measures." Without it, target dilation is an
  immediate counterexample.
- Check the factor of two caused by ordered pairs.
- Check the transition between the v1 and published potential
  normalizations; the theorem itself depends only on the corrected `log(2)`
  expression.

## Literature audit

Cheap run indexes contained no duplicate. Exact searches for the corrected
formula and conjecture sentence, plus searches of later semi-discrete
entropic-map literature through 2026-08-09, found no resolution. The author's
later thesis still prints the corrected expression as a conjecture.

## Artifact QA

- LaTeX compiled twice without errors, overfull boxes, or underfull boxes.
  The only warning is the harmless conversion of float specifier `h` to `ht`.
- The final PDF has four letter-sized pages and is unencrypted.
- All four pages were rendered at 150 dpi and visually inspected. Text,
  equations, the source crop, references, margins, and page numbers are clean
  and unclipped.
- Ghostscript text extraction recovers the theorem, explicit constant,
  independence statement, and proof conclusion.
