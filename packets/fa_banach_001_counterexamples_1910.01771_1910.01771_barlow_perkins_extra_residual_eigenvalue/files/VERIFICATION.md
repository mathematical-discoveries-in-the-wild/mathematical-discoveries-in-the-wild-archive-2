# Verification report

Status: `candidate_counterexample_likely_valid`

## Mathematical checks

- Checked the exact Barlow--Perkins question against arXiv:1910.01771, PDF
  page 14.
- Checked `R(3-sqrt(3)) = 3+sqrt(3)` and
  `R(3+sqrt(3)) = 3-sqrt(3)`.
- Checked the source midpoint extension formula at both points. The endpoint
  coefficient is exactly one and the opposite-corner coefficients are
  `sqrt(3)-1` and `-(1+sqrt(3))`.
- Checked the nine two-level child matrices symbolically.
- Checked that `P = I-(sqrt(3)/6)J` has eigenvalues
  `1,1,1-sqrt(3)/2` and is positive definite.
- Checked `M^T P M <= 9P` for all nine matrices. The diagonal representative
  has an explicit positive-semidefinite defect; the off-diagonal
  representative has three positive leading principal minors.
- Checked the nesting identity `M_00(0,1,1)^T = -3(0,1,1)^T`.
- Checked that every finite vertex value is controlled by the common
  quadratic norm after multiplication by `3^-n`.
- Checked that odd reflection satisfies the eigenvalue equation at the common
  vertex by pairwise cancellation.
- Checked that the two-cycle does not meet the defining seeds for
  `Sigma_4`, `Sigma_5`, or `Sigma_6`.
- Checked the residual-spectrum step: the bounded eigenfunction lies in the
  adjoint kernel, while an `ell^1` eigenfunction would be in `ell^2`, contrary
  to source Theorem 3.10.

## Computational checks

Run:

`conda run --no-capture-output -n sandbox python code/verify_matrix_certificate.py`

The script verifies the exact algebra over `Q(sqrt(3))`, including all nine
matrix inequalities and the nesting identity.

Run:

`conda run --no-capture-output -n sandbox python code/finite_level_probe.py
--mode symmetric --max-level 8`

Levels 1 through 8 contain up to 9843 vertices. The inner pair remains
`(1,1)` and the observed supremum is `2/sqrt(3)` at every tested level. This
is a consistency check only; the proof uses the exact quadratic certificate.

## Literature check

A bounded search covered arXiv:1910.01771, the exact open-question sentence,
and combinations of `Barlow--Perkins`, `Sierpinski lattice`, `ell^1 spectrum`,
`ell^infinity eigenvalue`, `generating sequence`, and `3-sqrt(3)`. Later arXiv
work on Sierpinski lattice spectra and spectral dimension did not answer this
question. No exact match was located.

## Rendering check

Compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error
-outdir=tmp main.tex`. The final log has no overfull boxes, underfull boxes,
undefined references, or warnings. All six final pages were rendered at 150
DPI and visually inspected for clipping, broken formulas, page transitions,
and readability of the source screenshot.

## Human-review recommendation

Review as a likely valid full negative answer. Focus on the correspondence
between the matrices and two successive spectral-decimation extensions, the
nested finite-gasket consistency, and the residual-spectrum duality step.
