# Verification report

Status: complete; candidate full counterexample, likely valid, with the two
specified steps prioritized for independent human review.

## Adversarial proof audit

- **Martingale boundedness.** The process is stopped after reaching level
  `1/2`.  Its overshoot is at most `epsilon_1`, so the terminal function is
  bounded.  Doob's `L^2` inequality and the square-summability of the
  increments leave at least `3/4` of `[0,1]` active at every stage.
- **Divergent exponent.** For `q=alpha/2<2`, one can choose
  `1/2<p<1/q`; then `epsilon_j=c j^{-p}` is square summable while
  `sum epsilon_j^q` diverges.
- **Current-scale lower bound.** On the outer eighths of the two children of
  an active dyadic parent, the current Haar increment contributes at least
  `(9/64) epsilon_j |I|^2` to the trapezoidal error.
- **Descendant contamination.** Update levels are separated by eight dyadic
  generations.  Every later detail has mean zero on its parent cells; pairing
  it with the affine weight costs one cell length.  Summing full and boundary
  cells gives at most `3 epsilon_k |I|^2 2^{-8(k-j)}`.  The total is less
  than half of the current-scale contribution.
- **No ancestor contamination.** All earlier martingale details are constant
  on the current parent interval, and the trapezoidal-error functional
  annihilates constants.
- **Disjointness.** A pair in the selected rectangle lies in opposite
  immediate children of its current parent.  That parent is the pair's
  unique smallest dyadic common ancestor, so rectangles from different
  stages or parents are disjoint.
- **Regular curve.** The terminal martingale `g` is bounded; hence its
  primitive `f` is Lipschitz.  The horizontal lift built from `f` has metric
  increments comparable to the parameter difference, so its restriction to
  `[0,1]` is a compact regular curve.
- **Kernel comparison.** The vertical group coordinate is exactly the
  trapezoidal error, while the Koranyi norm is at most a fixed multiple of
  the parameter gap.  Therefore `K_alpha` is bounded below on each selected
  rectangle by a constant times `epsilon_j^(alpha/2)/|I|`.
- **Operator contradiction.** The kernel is nonnegative.  Pairing a truncated
  operator against the indicator of the whole curve bounds its positive
  double integral by the operator norm times the curve measure.  The disjoint
  rectangles make these integrals diverge, so the truncation norms cannot be
  uniform.

## Literature and novelty check

- Cheap run indexes were searched for arXiv:1911.03223, the exact title, the
  `K_alpha` family, and the Heisenberg regular-curve question; no duplicate
  packet was found.
- Bounded arXiv searches used the exact source question, kernel formula,
  author names, and phrases `nonnegative kernels`, `regular curves`, and
  `alpha 4`.
- The decisive current source is Chousionis--Li--Zhang,
  arXiv:2605.17680.  Its Theorem 1.5 covers only `0<alpha<2`, and the
  following paragraph explicitly says that extension to `[2,4)` may be
  possible.  No primary source explicitly resolving `[2,4)` was found.

## Computational check

`code/verify_martingale_curve.py` checks the exact Haar formula, exponent
choices, Doob variance budget, and finite stopped-martingale trapezoidal
lower bounds.  It passed for `alpha=2,3,3.8`; the adversarial finite graph
used only four generations of scale separation rather than the proof's eight.
These checks are diagnostic and are not used as proof.

## Artifact checks

- Source and supporting PDFs: downloaded from official arXiv endpoints.
- Open-question crop: rendered from source PDF page 4 and visually checked.
- LaTeX compilation: passed with `latexmk`; final packet has five pages.
- Warning scan: no undefined references, warnings, overfull boxes, or
  underfull boxes in the final log.
- Visual QA: all five pages rendered at 144 dpi and inspected.  The source
  crop and all proof equations are readable, with no clipping or overlap.
- Text extraction: passed with Ghostscript `txtwrite`; status, lemma,
  theorem, descendant estimate, curve proof, limitations, and references are
  present.  An initially exposed missing backslash before five `qquad`
  commands was corrected, followed by a clean rebuild and second full-page
  visual inspection.

## Human-review focus

Check the descendant tail bound with partial boundary cells and the passage
from the dyadic parametric double integral to Hausdorff measure on the lifted
curve.  These are the two places where constants are suppressed.
