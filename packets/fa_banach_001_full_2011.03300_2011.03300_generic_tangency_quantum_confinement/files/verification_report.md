# Verification report

## Mathematical audit

- Located the exact open question on page 5 of arXiv:2011.03300v2 and
  included a readable source crop.
- Checked the generic tangency normal form against arXiv:2104.07745:
  `X_1=d_x`, `X_2=(y-x^2 psi(x)) exp(Psi(x,y)) d_y`, with `psi(0) != 0`.
- Re-derived the upper-component transverse scaling and completion of
  squares.  The exact remainder is `3/(1-r^2)^3`.
- Re-derived the upper gauge gradient.  After `x^2=z*y`, it is
  `(y(1-z^2)^2+16z)/4`, giving a strict margin on `z<3/4`.
- Re-derived the lower horizontal-cone completion of squares.  Relative to
  `x^-2 d omega`, its coefficient is
  `3(3x^2-b)/(4(x^2+b))`, hence at least `33/20` on `b<=x^2/4`.
- Checked that the lower vertical sector has bounded horizontal gradient for
  `-log b` and hence admits a complete-end exhaustion.
- Audited the angular IMS costs: they are of order `y^-1` above and
  `x^-2` plus a bounded term below; the former is dominated on fixed
  transition cones by the upper Hardy weight, while the latter can be made
  arbitrarily small by logarithmically separating the cone thresholds.
- The main reviewer focus remains the boundary-local Agmon lemma and the
  uniform stability passage from the canonical model to the smooth normal
  form.  Both are written out in the packet and use strict constants.

## Symbolic sanity check

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_tangency_hardy.py
```

Output:

```text
upper square remainder: -3/((r - 1)**3*(r + 1)**3)
lower Hardy ratio: 3*(-b + 3*x**2)/(4*(b + x**2))
upper gauge gradient after x^2=z*y: (y*z**4 - 2*y*z**2 + y + 16*z)/4
on b <= x^2/4, lower ratio >= 33/20 > 1
on z <= 1/2 and y small, |grad rho|^2 < 3
PASS
```

The first displayed expression equals `3/(1-r^2)^3`.  The script checks
algebra only and is not a substitute for the analytic proof.

## Build and visual QA

- Built `main.tex` with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -outdir=tmp`.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- Rendered all five pages at 150 dpi and visually inspected every page.  No
  clipping, overlap, broken formula, or layout defect was found.
- `solution_packet.pdf`: 5 pages, letter size.
- SHA-256 `solution_packet.pdf`:
  `9a94adc18705d43a7d99db8df130a0d3fa75d9c70c91723ffdb014d1ca1ed378`.
- SHA-256 `source_paper.pdf`:
  `aa685671734f32b2133ea6fb48d2b2d1464930bda815e8a84c1db984f1d449bc`.

## Literature audit

Focused primary-source searches through 13 August 2026 used the exact
tangency/self-adjointness phrases, the canonical `y-x^2` model, and the
authors of the source and later closure paper.  arXiv:2104.07745 treats
inverse-square perturbations at tangencies but explicitly leaves the bare
Laplacian outside its polynomial-weight method.  arXiv:2305.08280 treats
alpha-Grushin hypersurfaces, not tangency points.  No exact answer to the
generic tangency question was found.  This is a bounded search, not an
exhaustive novelty guarantee.
